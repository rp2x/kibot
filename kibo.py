import random 
from discord.ext import commands 
import time

TOKEN = "" 
wacamole=0

bot = commands.Bot(command_prefix="#")
client = commands.Bot(command_prefix="#")

#control por terminal(en desarrollo)
@bot.command(name='@') #Nombre del comando
async def randomMeme(ctx): #Funcion del coma                                                             
    response=input()    
    await ctx.send(response)

#encuesta
@bot.command(name='votacion') #Nombre del comands
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
                    await ctx.send("los reaultados son",positive,"votos positivos y",negative2,"votos negativos")
                    




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
                                                                                                                                                                            o
    await ctx.send(response) #Enviamos la respuesta al usuario


@bot.command(name='ch')                                                                               
@commands.has_any_role('hacker','Staff')                                                           
async def ch(ctx,namme):
    guild = ctx.guild
    await guild.create_text_channel(namme)
    print ("canal creado nombre:",namme)


bot.run(TOKEN) #Start1|e0=
