import discord

class message():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if 'pervert' in message.content:
            await self.bot.send_message(message.channel, "I'll burn him to cinders")
            
    async def on_message(message):
        if not message.author.bot and (message.server == None or client.user in message.mentions):
            await client.send_typing(message.channel)
            txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, r['response'] )



def setup(bot):
    bot.add_cog(message(bot))
