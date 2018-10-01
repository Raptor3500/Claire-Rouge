import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
import asyncio
import os

startup_extensions = [
  'message'
]

bot = commands.Bot(command_prefix='claire ')
bot.remove_command('help')
ownerID = "274298631517896704"

user = 'rZuTJlFKDZF5oi0T'
key = 'jiaN5JDdXrvjRNFng4t9rlMF47pjazst'

# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")
  
@bot.event
async def on_message(message):
  if not message.author.bot and (message.server == None or client.user in message.mentions):
    await client.send_typing(message.channel)
    txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
    r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'claire', 'text':txt}).text)
    if r['status'] == 'success':
      await client.send_message(message.channel, r['response'] )
  
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
  embed.add_field(name='owner', value='not finished', inline=False)
  embed.add_field(name='cmds', value='List of commands (so far)', inline=False)
  
  await bot.say(embed=embed)
  
@bot.command(pass_context=True)
async def owner(ctx):
  embed = discord.Embed(name='owner', description=None, color=0x426ef4)
  embed.set_author(name=ctx.message.author.name)
  embed.add_field(name='setgame', value='Sets my game', inline=False)
  
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
            
@bot.command(pass_context=True)
async def playing(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= (mesg)))
    await bot.say("I am now playing " + mesg)
    
@bot.command(pass_context=True)
async def watching(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= mesg, type=3))
    
@bot.command(pass_context=True)
async def listening(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= mesg, type=2))
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
  
  embed = discord.Embed(title="{}'s info".format(user.name), description='Here is what I could find:', color=ctx.message.author.color)
  embed.add_field(name='Name', value='{}'.format(user.name))
  embed.add_field(name='ID', value='{}'.format(user.id), inline=True)
  embed.add_field(name='Status', value='{}'.format(user.status), inline=True)
  embed.add_field(name='Highest Role', value='<@&{}>'.format(user.top_role.id), inline=True)
  embed.add_field(name='Joined at', value='{:%d/%h/%y at %H:%M}'.format(user.joined_at), inline=True)
  embed.add_field(name='Created at', value='{:%d/%h/%y at %H:%M}'.format(user.created_at), inline=True)
  embed.add_field(name='Discriminator', value='{}'.format(user.discriminator), inline=True)
  embed.add_field(name='Playing', value='{}'.format(user.game))
  embed.set_footer(text="{}'s Info".format(user.name), icon_url='{}'.format(user.avatar_url))
  embed.set_thumbnail(url=user.avatar_url)
  
  await bot.say(embed=embed)
  
  

         
  


requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'claire'})
bot.run(os.environ.get('Token'))
