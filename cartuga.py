import discord
from discord.ext import commands
import random

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


suits = ["Copas ♥️", "Paus ♣️", "Ouros ♦️", "Espadas ♠️"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Ás"]

cards = [
    {
        "name": "Falha",
        "value": "😣 Uma falha completa!",
        "weight": 20,
        "card_values": ["2", "3", "4"]
    },
    {
        "name": "Fraco",
        "value": "🃏 Resultado fraco, poderia ser melhor.",
        "weight": 30,
        "card_values": ["5", "6", "7"]
    },
    {
        "name": "Moderado",
        "value": "♠️ Um resultado sólido, nada mal!",
        "weight": 30,
        "card_values": ["8", "9", "10"]
    },
    {
        "name": "Sucesso",
        "value": "♥️ Sucesso notável, parabéns!",
        "weight": 15,
        "card_values": ["Valete", "Dama", "Rei"]
    },
    {
        "name": "Sucesso Crítico",
        "value": "♦️ Sucesso Crítico! Perfeito!",
        "weight": 5,
        "card_values": ["Ás"]
    }
]

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command(name='carta')
async def draw_card(ctx):
    category = random.choices(cards, weights=[c["weight"] for c in cards], k=1)[0]
    card_value = random.choice(category["card_values"])
    suit = random.choice(suits)
    card = f"{card_value} de {suit}"
    
    await ctx.send(f'**{card}**\n**{category["name"]}**: {category["value"]}')


bot.run('Chave do Bot aqui')