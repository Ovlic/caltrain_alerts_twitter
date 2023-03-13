
import discord
from bot import CaltrainAlerts
from discord.errors import NotFound
from discord.ext.commands import Bot, CommandNotFound
from discord.app_commands.errors import CommandNotFound as AppCommandNotFound, CommandInvokeError
from dotenv import load_dotenv
from os import getenv
from utils import setupLogger

load_dotenv()
TOKEN = getenv('TOKEN')
logger = setupLogger()

client = CaltrainAlerts()

@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error:Exception) -> None: # : discord.app_commands.AppCommandError
    print(f"main: {type(error)}")
    if isinstance(error, AppCommandNotFound): return
    if isinstance(error, NotFound): return
    if interaction.user.id == 675559827425984582: 
        err_str = f"`{getattr(error, '__module__')}:  {error.args[0]}`"
        try:
            await interaction.response.send_message(err_str)
        except discord.errors.InteractionResponded:
            pass

    if isinstance(error, CommandInvokeError):
        #return
        logger.exception(error.__cause__)
        return

    # logger.exception(error)


@client.tree.command()
async def reload(interaction = discord.Interaction):
    await client.reload_extension("twitteralerts")
    await client.reload_extension("status")
    embed = discord.Embed(title='Reloaded', description=f'Status successfully reloaded', color=0xff00c8)
    await interaction.response.send_message(embed=embed, ephemeral=True)
    logger.info("Reloaded TwitterAlerts")
    print(client.cogs)


client.run(TOKEN)
