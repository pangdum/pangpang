import discord
import random
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print(client.user.id)
        print("동작중")
        game = discord.Game("국번없이 1336")
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
           to_send = '환영합니다. {0.mention}님이 {1.name} 에 오셨어요!'.format(member, guild)
           await guild.system_channel.send(to_send)

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!도박'):
            await message.channel.send('3초뒤 공개됩니다.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)
            answers = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=3.0)
            except asyncio.TimeoutError:
                return await message.channel.send('{} 와 {}'.format(answer,answers))

            if int(guess.content) == answer:
                await message.channel.send('정답!')
            else:
                await message.channel.send('기다리지..힝 {}.'.format(answer))


client = MyClient()
client.run('Njg3MzA5NjgxNjY4MTI4ODkx.Xmj5IA.lPGzw82Ce6W0u3zLXbi5ZcJhc4U')
