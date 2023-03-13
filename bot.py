
import discord
import logging
from discord.ext.commands import Bot, CommandNotFound
from discord.app_commands.errors import CommandInvokeError

#\u001b[38;5;82;1m
log = logging.getLogger("CaltrainAlerts.\u001b[38;5;82;1mBot\u001b[0m")


class CaltrainAlerts(Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix="!"
            )
        self.MY_GUILD = discord.Object(id=1017455527577530409)

    async def on_ready(self):
        log.info("CaltrainAlerts bot is ready!")

    async def on_command_error(self, ctx, ex):
        print(f"main.on_command_error: {type(ex)}")
        if isinstance(ex, CommandNotFound): return
        if ctx.author.id == 675559827425984582: 
            err_str = f"`{getattr(ex, '__module__')}:  {ex.args[0]}`"
            await ctx.reply(err_str)
        if isinstance(ex, CommandInvokeError):
            log.exception(ex.__cause__)
            raise ex.__cause__
        else:
            log.exception(ex)
            raise ex.__cause__

    async def setup_hook(self):
        await self.load_extension('status')
        await self.load_extension('twitteralerts')
        self.tree.copy_global_to(guild=self.MY_GUILD)
        await self.tree.sync(guild=self.MY_GUILD)