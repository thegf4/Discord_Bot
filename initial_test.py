import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
    
    async def on_member_join(member):
        print(f'{member} has joined the server!')
         
    async def on_member_remove(member):
        print(f'{member} has left the server!')

client = MyClient()
client.run('CODE')