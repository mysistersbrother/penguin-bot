import discord
import mystbin


intents = discord.flags.Intents().default()
intents.members = True

bot = discord.ext.commands.bot.Bot(command_prefix='d,', intents=intents)

@bot.event
async def on_ready():
    print(
        "Logged in! \n"
        f"{'-' * 20}\n"
        f"Bot Name: {bot.user} \n"
        f"Bot ID: {bot.user.id} \n"
        f"{'-' * 20}"
    )

bot.mystbin = mystbin.Client()


@bot.event
async def on_error(event, *args, **kwargs):
    ignored_events = ["on_member_join", "on_message", "on_raw_reaction_add"]
    if event in ignored_events:
        return
    else:
        raise

if __name__ == "__main__":
    bot.run('NzUzMDM3NDY0NTk5NTI3NDg1.YBD56Q.qmgGknZe2r4dx2Vsm3aunlugbE2')
