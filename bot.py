import json

import disnake
from disnake.ext import commands, tasks
import requests
from dotenv import load_dotenv
import os
import config

intents = disnake.Intents.all()

bot = commands.Bot(intents=intents)

load_dotenv()

@tasks.loop(seconds=10)
async def send():
    user = bot.get_user(config.user_id)

    comms = requests.get(config.URL + "/get_data")

    print(json.loads(comms.json()))

    for comm in json.loads(comms.json()):
        print(json.loads(comms.json()))
        embed = disnake.Embed(
            title="A new commission has appeared infront of your door!",
            description=f"Message: ``{json.loads(comms.json())[comm]}``"
        )

        embed.add_field(name="Contact:", value=f"Contact -> ``{comm}``", inline=False)
        embed.set_image(url="https://media1.tenor.com/m/t4we1lzoOsYAAAAd/roblox-robux.gif")
        await user.send(embed=embed)

@bot.event
async def on_ready():
    print("Bot is ready!")
    send.start()

bot.run(os.getenv("TOKEN"))