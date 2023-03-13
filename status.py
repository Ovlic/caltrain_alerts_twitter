
import discord
import logging
from bot import CaltrainAlerts
from datetime import datetime
from discord import app_commands
from discord.ext import commands, tasks
#from main import CaltrainAlerts
from zone import Zone_1, Zone_2, Zone_3, Zone_4, Zone_5, Zone_6

log = logging.getLogger("CaltrainAlerts.\u001b[38;5;208;1mStatus\u001b[0m")

class Status(commands.Cog):
    def __init__(self, client):
        self.client: CaltrainAlerts = client
        self.recent_tweet = {}
        
    async def cog_command_error(self, ctx, error):
        channel = self.client.get_channel(1017455639578030161)
        await channel.send("```py\n"+str(error)+"\n```")

    async def cog_unload(self) -> None:
        """Cancel the init task and scheduled tasks when the cog unloads."""
        log.debug("Cog unload: cancelling all tasks")
        for task in self.queue_tasks:
            task.cancel()
            log.debug(task.is_running())

        if self.update_status.is_running():
            log.debug("Cog unload: cancelling update_status")
            self.update_status.cancel()


    @app_commands.command(name="status_test")
    async def start_tracker(self, interaction: discord.Interaction):
        """Testing statuses"""

        status_embed = discord.Embed(
            title="Caltrain Status",
            description=f"Last updated: <t:{int(datetime.now().timestamp())}:F>"
        )

        def zone_txt(zone):
            z = ""
            # Structure: <emoji of train type> <Limiteds> <Name in bold>: <Events>
            for station in zone.stations:
                s = ""
                if station.is_baby_bullet_stop:
                    s += "🔴 "
                if station.is_reduced_hours:
                    s += "🔵 "
                if station.is_limited_stop != []:
                    if s == "":
                        s += "🟡 "
                    s += f"{str(station.is_limited_stop)} "
                else:
                    if s == "":
                        s += "⚪ "
                s += f"**{station.name}**: \n\tSingle Tracking: {'No' if not station.single_tracking else station.single_tracking}\n\tDelays: {'No' if not station.delays else 'Yes'}"
                s += "\n\n"
                z += s
            z += "\n\n "
            return z

        status_embed.add_field(name="Zone 1", value=zone_txt(Zone_1), inline=False)
        status_embed.add_field(name="Zone 2", value=zone_txt(Zone_2), inline=False)
        status_embed.add_field(name="Zone 3", value=zone_txt(Zone_3), inline=False)
        status_embed.add_field(name="Zone 4", value=zone_txt(Zone_4), inline=False)
        status_embed.add_field(name="Zone 5", value=zone_txt(Zone_5), inline=False)
        status_embed.add_field(name="Zone 6", value=zone_txt(Zone_6), inline=False)

        await interaction.response.send_message(embed=status_embed)


    @tasks.loop(seconds=30)
    async def update_status(self):
        await self.client.wait_until_ready()
        await self.update_embed()

    async def update_embed(self):
        channel = self.client.get_channel(1026939626084122624)
        msg = await channel.fetch_message(1026940285558722570)

        #status_embed = msg.embeds[0]
        status_embed = discord.Embed(
            title="Caltrain Status",
            description=f"Last updated: <t:{int(datetime.now().timestamp())}:F>"
        )

        def zone_txt(zone):
            z = ""
            # Structure: <emoji of train type> <Limiteds> <Name in bold>: <Events>
            for station in zone.stations:
                s = ""
                if station.is_baby_bullet_stop:
                    s += "🔴 "
                if station.is_reduced_hours:
                    s += "🔵 "
                if station.is_limited_stop != []:
                    if s == "":
                        s += "🟡 "
                    s += f"{str(station.is_limited_stop)} "
                else:
                    if s == "":
                        s += "⚪ "
                s += f"**{station.name}**: \n\tSingle Tracking: {'No' if not station.single_tracking else station.single_tracking}\n\tDelays: {'No' if not station.delays else 'Yes'}"
                s += "\n\n"
                z += s
            z += "\n\n "
            return z

        status_embed.add_field(name="Zone 1", value=zone_txt(Zone_1), inline=False)
        status_embed.add_field(name="Zone 2", value=zone_txt(Zone_2), inline=False)
        status_embed.add_field(name="Zone 3", value=zone_txt(Zone_3), inline=False)
        status_embed.add_field(name="Zone 4", value=zone_txt(Zone_4), inline=False)
        status_embed.add_field(name="Zone 5", value=zone_txt(Zone_5), inline=False)
        status_embed.add_field(name="Zone 6", value=zone_txt(Zone_6), inline=False)
        status_embed.set_footer(text=f"Last updated: {datetime.now().strftime('%H:%M.%S %p')}")
        log.info("editing message")
        await msg.edit(embed=status_embed)
                

async def setup(bot):
    t = Status(bot)
    await bot.add_cog(t)#, guilds=[discord.Object(id=1017455527577530409)])
    t.update_status.start()
    log.info("Loaded Status")
