import discord
from discord.ext import commands, tasks
import os
from flask import Flask
from threading import Thread

# Variables d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", "1272908129323057152"))
ROLE_ID = int(os.getenv("DISCORD_ROLE_ID", "1310177296539189309"))
SERVER_LINK = os.getenv("DISCORD_SERVER_LINK", "discord.gg/GjgDWsT3B9")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Keep-alive pour Railway si nécessaire
app = Flask('')

@app.route('/')
def home():
    return "Bot actif !"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

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
            # Hypothétiquement : vérifier une bio
            # Impossible avec l'API actuelle de Discord
            pass
        except Exception as e:
            print(f"Erreur pour {member.name} : {e}")

# Démarrage
keep_alive()
bot.run(TOKEN)
