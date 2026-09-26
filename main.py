import os
import discord
from discord.ext import commands

# Configuration des permissions (Intents)
intents = discord.Intents.default()
intents.message_content = True

# Création du bot avec le préfixe '!'
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté avec succès en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Récupération du Token sécurisé depuis l'hébergeur
TOKEN = os.getenv("DISCORD_TOKEN")

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Erreur : La variable d'environnement DISCORD_TOKEN est introuvable.")
