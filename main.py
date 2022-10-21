
import discord
from discord import app_commands
from discord.errors import NotFound
from discord.ext.commands import Bot, CommandNotFound
from discord.app_commands.errors import CommandNotFound as AppCommandNotFound
from dotenv import load_dotenv
from os import getenv
from utils import setupLogger

load_dotenv()
TOKEN = getenv('TOKEN')

logger = setupLogger()

class CaltrainAlerts(Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix="!"
            )
        self.MY_GUILD = discord.Object(id=1017455527577530409)

    async def on_ready(self):
        logger.info("CaltrainAlerts bot is ready!")

    async def on_command_error(self, ctx, ex):
        if isinstance(ex, CommandNotFound): return
        if ctx.author.id == 675559827425984582: 
            err_str = f"`{getattr(ex, '__module__')}:  {ex.args[0]}`"
            await ctx.reply(err_str)
        raise ex

    async def setup_hook(self):
        await self.load_extension('status')
        await self.load_extension('twitteralerts')
        self.tree.copy_global_to(guild=self.MY_GUILD)
        await self.tree.sync(guild=self.MY_GUILD)

client = CaltrainAlerts()

@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError) -> None:
    if isinstance(error, AppCommandNotFound): return
    if isinstance(error, NotFound): return
    if interaction.user.id == 675559827425984582: 
        err_str = f"`{getattr(error, '__module__')}:  {error.args[0]}`"
        try:
            await interaction.response.send_message(err_str)
        except discord.errors.InteractionResponded:
            pass
    raise error


@client.tree.command()
async def reload(interaction = discord.Interaction):
    await client.reload_extension("twitteralerts")
    embed = discord.Embed(title='Reloaded', description=f'Status successfully reloaded', color=0xff00c8)
    await interaction.response.send_message(embed=embed, ephemeral=True)
    logger.info("Reloaded TwitterAlerts")
    print(client.cogs)


client.run(TOKEN)
