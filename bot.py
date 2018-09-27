import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

startup_extensions = [
  'message'
]

bot = commands.Bot(command_prefix='claire ')
bot.remove_command('help')
ownerID = "274298631517896704"

# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")
  
  # Make me say stuff
@bot.command(pass_context=True)
async def say(ctx, *args):
    """Make me say your message"""
    if ctx.message.author.id in ownerID:
        channel = ctx.message.channel
        mesg = ' '.join(args)
        await bot.delete_message(ctx.message)
        await bot.send_typing(channel)
        await asyncio.sleep(1)
        await bot.say(mesg)
        print (ctx.message.author.id + " or " + ctx.message.author.name + " made me say '{}'".format(mesg))
        
@bot.command(pass_context=True)
async def invite(ctx):
  """Invite Me"""
  await bot.say("here's my invite link")
  await bot.say("https://discordapp.com/api/oauth2/authorize?client_id=493204973685964830&permissions=8&scope=bot")
  
@bot.command(pass_context=True)
async def help(ctx):
  embed = discord.Embed(name='help', description=None, color=0x426ef4)
  embed.set_author(name=ctx.message.author.name)
  embed.add_field(name='Owner Only', value='not finished', inline=False)
  embed.add_field(name='cmds', value='not finished', inline=False)
  
  await bot.say(embed=embed)
  
  @bot.command(pass_context=True)
async def cmds(ctx):
  embed = discord.Embed(name='cmds', description=None, color=0x426ef4)
  embed.set_author(name=ctx.message.author.name)
  embed.add_field(name='say', value='says your message', inline=False)
  embed.add_field(name='invite', value='Invite Me', inline=False)
  
  
  await bot.say(embed=embed)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
         
  



bot.run(os.environ.get('Token'))
