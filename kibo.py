import random #Para poder seleccionar un random de nuestra lista
from discord.ext import commands # Importamos commands de la libreria
import time

TOKEN = "Nzk5MjkwODUwODE0NTkxMDA2.YABbnA.ra0bLZ311r2DsnFsXIebIxdzmYA" #El token secreto de nuestro BOT
wacamole=0

bot = commands.Bot(command_prefix='#') # Le Decimos con que prefijo el bot #va a empezar escuchar para saber cual es el comando
client = commands.Bot(command_prefix="#")


@bot.command(name='@') #Nombre del comando
async def randomMeme(ctx): #Funcion del coma                                                             
    response=input()    
    await ctx.send(response)

@bot.command(name='T') #Nombre del comands
async def randomMeme(ctx,votacion,t:int):
            vote_msg = await ctx.channel.send(votacion)
            await vote_msg.add_reaction('✅')
            await vote_msg.add_reaction('❎')
            vote_msg = await vote_msg.channel.fetch_message(vote_msg.id) # refetch message
            # default values
            positive = 0
            negative = 0
            for reaction in vote_msg.reactions:
                if reaction.emoji == '✅':
                    positive = reaction.count -1
                if reaction.emoji == '❎':
                    negative2 = reaction.count -1
                    time.sleep(t)
                    await ctx.send('los reaultados son ')
                    




@bot.command(name='randomMeme') #Nombre del comando
async def randomMeme(ctx): #Funcion del comando
    listGifs = [                                                                                              
            'https://media.giphy.com/media/EXHHMS9caoxAA/giphy.gif',
            'https://media.giphy.com/media/NQL7Wuo2JSQSY/giphy.gif',
            'https://media.giphy.com/media/myuLckXB7OjfGw1gSb/giphy.gif',
            'https://media.giphy.com/media/quO0X65yj6gw0/giphy.gif',
            'https://media.giphy.com/media/LYd7VuYqXokv20CaEG/giphy.gif',
            'https://media.giphy.com/media/JNgLZn7fWAjjW/giphy.gif',
            'htt ps://media.giphy.com/media/lFmmcqA4VBhMQ/giphy.gif',
            'https://media.giphy.com/media/V4NnsmEY7hsK4/giphy.gif'                                           
            ] 
    #La lista con los g ifs                                                                                                                                                                             o
    await ctx.send(response) #Enviamos la respuesta al usuario


@bot.command(name='ch')                                                                               
@commands.has_any_role('hacker','Staff')                                                           
async def ch(ctx,namme):
    guild = ctx.guild
    await guild.create_text_channel(namme)
    print ("canal creado nombre:",namme)


bot.run(TOKEN) #Start1|e0=
