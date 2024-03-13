import discord
import os
from discord.ext import commands
from googletrans import Translator
from dotenv import load_dotenv
import asyncio
import yt_dlp

# Carrega as variáveis do arquivo .env
load_dotenv()

permission = discord.Intents.default() # permissões para o bot
permission.message_content = True # permitir mensagens
permission.members = True # permitir que os membros utilizem

bot = commands.Bot(command_prefix="/", intents=permission) # inicializando o bot

voice_clients = {}
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)

ffmpeg_options = {'options': '-vn'}

@bot.command()
async def comandos(ctx: commands.Context):
    await ctx.reply('COMANDOS:\n\n 1°  "/traduzir + seu texto": Esse comando traduz o texto ou palavra para o português\n\n2°  "/perfil": Mostra sua foto de perfil\n\n3° "/banir + nickname": Banir usuário\n\n4° "/play + link do youtube": Toca o vídeo MP3 no canal que você está\n\n5° "/pause": Pausa a música atual\n\n6° "/resume": Despausa a música\n\n7° "/stop": Para de tocar a música')

@bot.command()
async def traduzir(ctx: commands.Context, *, text):
    translator = Translator()
    detect = translator.detect(f"{text}")
    if detect.lang == "pt":
        translation = translator.translate(text, src=detect.lang, dest="en")
        await ctx.reply(f"Tradução para o inglês: {translation.text}")
    else:
        translation = translator.translate(text, src=detect.lang, dest="pt")
        await ctx.reply(f"Tradução para o português: {translation.text}")

@bot.command()
async def perfil(ctx: commands.Context, *, member: discord.Member):
    user = member
    await ctx.reply(user.avatar)

@bot.command()
async def banir(ctx, *, member: discord.Member):
    ID = os.getenv("PERSONAL_ID")
    if str(ctx.author.id) == ID:
        try:
            await member.ban(reason="Muito tempo inativo")
            await ctx.send(f"{member.mention} foi banido com sucesso.")
        except discord.Forbidden:
            await ctx.send("Não tenho permissão para banir membros.")
        else:
            await ctx.send("Você não tem permissão para usar este comando.")

@bot.command()
async def play(ctx: commands.Context, *, url):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except Exception as e:
        print(e)

    try:
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

        song = data['url']
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

        voice_clients[ctx.guild.id].play(player)
    except Exception as e:
      await ctx.reply("Você precisa estar em um canal de voz")

@bot.command()
async def pause(ctx: commands.Context):
    try:
        voice_clients[ctx.guild.id].pause()
    except Exception as e:
        print(e)

@bot.command()
async def resume(ctx: commands.Context):
    try:
        voice_clients[ctx.guild.id].resume()
    except Exception as e:
        print(e)

@bot.command()
async def stop(ctx: commands.Context):
    try:
        voice_clients[ctx.guild.id].stop()
        await voice_clients[ctx.guild.id].disconnect()
    except Exception as e:
        print(e)

@bot.event
async def on_ready():
    print("Estou pronto")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.reply("Esse comando não existe.\n\nPara ver a lista de comandos digite: /comandos")

token = os.getenv('ACESS_TOKEN')
bot.run(token)
