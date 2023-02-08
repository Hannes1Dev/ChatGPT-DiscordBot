import openai
import discord

openai.api_key = ""

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} ist bereit!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('§'):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message.content[1:],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text

        await message.channel.send(response)

client.run('')
