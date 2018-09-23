startup_extensions = [
  'message'
]

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
            
import discord

class message():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if 'pervert' in message.content:
            await self.bot.send_message(message.channel, 'I`ll burn him to cinders')

def setup(bot):
    bot.add_cog(message(bot))
