

import discord
import requests
import json

client = discord.Client()

def setFalse():
    global set
    set = False
    
def testid():
      id = id+1
      return id
      
def getid():
   global id
   id = 12
   return id

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if (message.content == '!reset') or (message.content == '!cookies'):
        id = itestid()
        await message.channel.send("Session resetted")
    id = message.author.id
    x = requests.get('http://0.0.0.0:8989/api/rest/v1.0/ask?question=' + message.content + '&userid=' + str(id))
    print(x)
    json_data = x.json()['response']
    question = json_data['question']
    answer = json_data['answer']
    await message.channel.send(answer)


client.run('ODExOTkwODMwMjAwOTE0MDAx.YC6PYw.JvgVOIsedmIyFCwlchinb9pXkqQ')
set = False
