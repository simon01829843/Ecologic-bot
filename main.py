import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("Bot conectado como bot ecologico", bot.user)

@bot.command()
async def hello(ctx):
    await ctx.send("Hola, soy tu bot!")

@bot.command()
async def consejo(ctx):
    await ctx.send("Recuerda apagar las luces cuando no las estés usando y reciclar siempre que sea posible. ¡Cada pequeño gesto cuenta para cuidar nuestro planeta!")

@bot.command()
async def clasificate(ctx, object):
    object = object.lower()
    if object == "plástico":
        await ctx.send("¡Eres un reciclador de plástico! Recuerda separar tus residuos y reciclar correctamente.")
    elif object == "papel":
        await ctx.send("¡Eres un reciclador de papel! Asegúrate de reciclar tus papeles y cartones en los contenedores adecuados.")
    elif object == "vidrio":
        await ctx.send("¡Eres un reciclador de vidrio! Recuerda depositar tus botellas y frascos de vidrio en los contenedores correspondientes.")
    else:
        await ctx.send("Lo siento, no puedo clasificar ese objeto. Por favor, ingresa 'plástico', 'papel' o 'vidrio'.")
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("Falta configurar DISCORD_TOKEN")

bot.run(token)

