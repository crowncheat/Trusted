import discord
from discord.ext import commands, tasks
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = "123456789012345678"
ROLE_ID = "1310177296539189309"
SERVER_LINK = "discord.gg/GjgDWsT3B9"

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    check_bios.start()

@tasks.loop(hours=1)
async def check_bios():
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print("Serveur introuvable")
        return

    for member in guild.members:
        try:
            user = await bot.fetch_user(member.id)
            # L'API Discord ne fournit pas la bio via fetch_user
            # Ceci est une limite actuelle de Discord
            # Hypothétiquement, si c'était possible :
            # if SERVER_LINK in user.bio:
            #     role = guild.get_role(ROLE_ID)
            #     if role and role not in member.roles:
            #         await member.add_roles(role)
            pass
        except Exception as e:
            print(f"Erreur pour {member.name} : {e}")

bot.run(TOKEN)
