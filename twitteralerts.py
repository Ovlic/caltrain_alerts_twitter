
import asyncio
import discord
import html
import logging
import stations
from discord import app_commands
import twttr
import traceback
from discord.ext import commands, tasks
from datetime import datetime
from utils import nowstr, timeConvert, toDateTime

log = logging.getLogger("CaltrainAlerts.\u001b[38;5;87;1mTwitterAlerts\u001b[0m")
# logging.root.setLevel(logging.NOTSET)

class TwitterAlerts(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue_tasks = []
        self.station_tasks = {}
        self.recent_tweet = {}
        self.twt_ids = {}
        self.status = self.client.cogs['Status']
        
    async def cog_command_error(self, ctx, error):
        channel = self.client.get_channel(1017455639578030161)
        await channel.send("```py\n"+str(error)+"\n```")

    """async def cog_load(self, ctx):
        log.debug("cog_load")
        channel = self.client.get_channel(1017455639578030161)
        async for message in self.client.logs_from(channel, limit=30):
            if channel in message.content:
                pass"""
                

    async def cog_unload(self) -> None:
        """Cancel the init task and scheduled tasks when the cog unloads."""
        log.debug("Cog unload: cancelling all tasks")
        for task in self.queue_tasks:
            task.cancel()
            log.debug(task.is_running())


    @app_commands.command(name="start")
    async def start_tracker(self, interaction: discord.Interaction):
        """Start the CaltrainAlerts tracker"""
        if not self.update_tweets.is_running():
            self.update_tweets.start()
            await interaction.response.send_message("Started CaltrainAlerts tracker.")
            log.info("Started CaltrainAlerts tracker.")
        else:
            await interaction.response.send_message("CaltrainAlerts tracker is already running!")

    @app_commands.command(name="stop")
    async def stop_tracker(self, interaction: discord.Interaction):
        """Stop the CaltrainAlerts tracker"""
        if self.update_tweets.is_running():
            self.update_tweets.stop()
            await interaction.response.send_message("Stopped CaltrainAlerts tracker.")
            print("Stopped CaltrainAlerts tracker.")
        else:
            await interaction.response.send_message("CaltrainAlerts tracker is not running!")

    @app_commands.command(name="test_twitteralerts")
    async def test_twitteralerts(self, interaction: discord.Interaction):
        # logging.root.setLevel(logging.DEBUG)
        # log.setLevel(logging.DEBUG)
        log.debug("this will get printed")
        log.info("this will get printed")
        log.warning("this will get printed")
        log.error("this will get printed")
        log.critical("this will get printed")
        await interaction.response.send_message("Test!", ephemeral=True)


    @tasks.loop(seconds=30)
    async def update_tweets(self):
        try:
            r = twttr.get_tweets()
            #print(r)
            if r['data'][0] != self.recent_tweet:
                log.debug("New tweet!")
                if self.recent_tweet == {}:
                    self.recent_tweet = r['data'][0]
                else: 
                    self.recent_tweet = r['data'][0]
                    print(r['data'][0])
                    tweettxt = html.unescape(r['data'][0]['text'])
                    user_embed = discord.Embed(
                        title="New Tweet",
                        description=tweettxt,
                        color=0x00acee,
                        url=f"https://twitter.com/CaltrainAlerts/status/{r['data'][0]['id']}"
                    )
                    user_embed.set_image(url="https://twitter.com/CaltrainAlerts/photo")
                    user_embed.set_author(name="CaltrainAlerts", icon_url="https://cdn.discordapp.com/attachments/1017455639578030161/1017486168876650576/caltrainlogo.jpg")
                    user_embed.set_footer(text=f"Time: {timeConvert(toDateTime(r['data'][0]['created_at']))}")
                    channel = self.client.get_channel(1017455639578030161)
                    if "https://t.co/" in tweettxt:
                        # Reply
                        sub = tweettxt.split("https://t.co/")[1]
                        theurl = twttr.tco_to_link(f"https://t.co/{sub}")
                        theid = theurl.split("status/")[1]
                        themsgid = self.twt_ids[theid]
                        themsg = await channel.fetch_message(int(themsgid))
                        await themsg.reply(embed=user_embed)
                    else:
                        sentmsg = await channel.send(embed=user_embed)
                    
                    self.twt_ids[r['data'][0]['id']] = sentmsg.id
                    await self.scan_tweet(r['data'][0])

        except Exception as e:
            t = traceback.format_exc()
            log.error(t)
            channel = self.client.get_channel(1017455639578030161)
            await channel.send(f"{nowstr()} - Error: ```py\n{t}\n```")
    

    @app_commands.command(name="testtask")
    async def testtask(self, interaction: discord.Interaction):
        text = "Single tracking at 22nd St and Bayshore beginning with NB407, all trains will board on southbound platform until 12:14pm."
        date = datetime.now()
        hours = int(text.split('until')[1].split(':')[0])
        if "pm" in text.lower() and hours != 12:
            hours += 12
        mins = int(text.split(':')[1].split('am' if 'am' in text.lower() else 'pm')[0])
        new_period=date.replace(hour=hours, minute=mins).strftime('%Y-%m-%d-%H:%M')
        stations.San_Antonio.single_tracking = "Hi!"
        s = await self.create_background_task(time=new_period, station=stations.San_Antonio)
        self.client.loop.create_task(s(new_period, stations.San_Antonio))
        log.debug("Created task!")


    async def create_background_task(self, time, station):
        async def background_task(self, time, station):
            try:
                task_index = len(self.queue_tasks)-1
            except IndexError:
                # Nothing in queue_tasks
                pass
            now = datetime.now().strftime('%Y-%m-%d-%H:%M')
            while time > now:
                now = datetime.now().strftime('%Y-%m-%d-%H:%M')
                log.debug(f"Hi {station.name}: {time} doesnt equal {now}")
                await asyncio.sleep(20)  # task runs every 60 seconds
            station.single_tracking = None
            log.debug("Done waiting.")
            # await self.status.update_embed()
            del self.queue_tasks[task_index]
            
        return background_task
    
    async def scan_tweet(self, tweet):
        text = (html.unescape(tweet['text']))
        log.debug(f"Tweet text: {text}")
        if "single tracking" in text.lower():
            # Single tracking
            text = text.replace("NBD", "northbound").replace("SBD", "southbound")
            station_checking = stations.search_for_station_name(text)
            if station_checking:
                for station_check in station_checking:
                    log.debug(f"Found station(s): {station_check}")
                    if "ended" in text:
                        stations.Stations[station_check].single_tracking = ""
                        try:
                            self.station_tasks[station_check].cancel()
                        except KeyError:
                            log.debug("KeyError in station_tasks, probably a 'until further notice' tweet")

                        log.debug("Cancelled task: {station_check}")
                    else:
                        if "beginning" in text.lower():
                            log.debug("Beginning")
                            amorpm = ""
                            if "am" in text.lower() or "pm" in text.lower():
                                amorpm = "am"
                                # Time, not date
                                date = datetime.now()
                                if ":" in text:
                                    hours = int(text.split('until')[1].split(':')[0])
                                    hours_raw = hours
                                    if "pm" in text.lower():
                                        amorpm = "pm"
                                        hours += 12
                                    mins_raw = (text.split(':')[1].split('am' if 'am' in text.lower() else 'pm')[0])
                                    mins = int(mins_raw)
                                    new_period=date.replace(hour=hours, minute=mins).strftime('%Y-%m-%d-%H:%M')
                            else:
                                if ":" in text:
                                    amorpm = "pm"
                                    date = datetime.now()
                                    ttime = text.split('until')[1].split('.')[0].split(":")
                                    hours = int(ttime[0])
                                    hours_raw = ttime[0]
                                    minutes = int(ttime[1])
                                    mins_raw = ttime[1]
                                    hours += 12
                                    new_period = date.replace(hour=hours, minute=minutes).strftime('%Y-%m-%d-%H:%M')                                    

                                else:
                                    stations.Stations[station_check].single_tracking = f"Boarding on {'southbound' if 'southbound' in text else 'northbound' if 'northbound' in text else 'none'} platform until further notice. **BETA TESTING**"
                                    # await self.status.update_embed()
                                    continue # Until further notice tweets

                        stations.Stations[station_check].single_tracking = f"Boarding on {'southbound' if 'southbound' in text else 'northbound' if 'northbound' in text else 'none'} platform until {hours_raw}:{mins_raw}{amorpm}."
                        s = await self.create_background_task(time=new_period, station=stations.Stations[station_check])
                        _task = self.client.loop.create_task(s(self, new_period, stations.Stations[station_check]))
                        self.queue_tasks.append(_task)
                        self.station_tasks[station_check] = _task
                        #await self.status.update_embed()
                await self.status.update_embed()
            else:
                log.warn("Station check is none :(")
        

    @app_commands.command(name="fake_st")
    @app_commands.describe(
        text='The fake tweet',
    )
    async def testtask(self, interaction: discord.Interaction, text: str):
        """Fake a single tracking event"""
        convert_hour = lambda h: h if h <= 12 else h+12
        datetxt = datetime.now()
        amorpm = "am" if int(datetxt.hour) <= 12 else "pm"
        hrs = int(datetxt.hour)
        if datetxt.minute+2 < 60:
            minutes = datetxt.minute+2
        else:
            hrs += 1
            minutes = datetxt.minute+2-60
        new_date_txt =  datetxt.replace(hour=hrs, minute=minutes).strftime('%H:%M')
        new_date_txt_12 = f"{int(new_date_txt.split(':')[0])-12}:{new_date_txt.split(':')[1]}" if int(new_date_txt.split(':')[0]) > 12 else new_date_txt

        # text = f"Single tracking at San Antonio beginning with NB407, all trains will board on southbound platform until {new_date_txt_12}{amorpm}."
        # status_text = f"Boarding on {'southbound' if 'southbound' in text else 'northbound' if 'northbound' in text else 'none'} platform until {new_date_txt}pm."
        await self.scan_tweet({'text': text})
        await interaction.response.send_message("Triggered fake single tracking event!", ephemeral=True)
        log.debug("Faked a single tracking event!")

    @app_commands.command(name="fake_end_st")
    @app_commands.describe(
        text='The fake tweet',
    )
    async def testtaskend(self, interaction: discord.Interaction, text: str):
        """Fake ending single tracking event"""
        
        # text = f"Single tracking SAT has ended. Beginning with SB122, all trains will board on their scheduled platforms"
        await self.scan_tweet({'text': text})
        await interaction.response.send_message("Triggered end fake single tracking event!", ephemeral=True)
        log.debug("Faked ending single tracking event!")

   
async def setup(bot):
    t = TwitterAlerts(bot)
    await bot.add_cog(t)
    log.info("Loaded TwitterAlerts")
