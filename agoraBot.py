import discord
import requests
import json
from random import randrange

client = discord.Client()

animalApis = [
    #{"link" : "https://elephant-api.herokuapp.com/elephants/random", "animal" : "elephant"}
    {"link" : "https://dog.ceo/api/breeds/image/random", "animal": "dog"}
    #{"link" : "https://random-d.uk/api/random", "animal" : "duck"},
    #{"link" : "https://some-random-api.ml/img/red_panda", "animal" : "red panda"}

]

keyPhrases = [
    "dark thoughts", "self harm", "suicide", "hurting myself", "I feel lost", "feeling lost", "cutting myself",
    "I feel worthless", "feeling worthless", "kill myself", "killing myself", "I want to die", "everything sucks"

]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # sync bot
    if message.content.upper() == "!SYNC":
        img = sync()
        try:
            await message.channel.send(embed=img)
        except:
            await message.channel.send(embed=img)

    # self harm bot
    for phrase in keyPhrases:
        if  phrase.upper() in message.content.upper():
            quote = get_quote()
            animal = get_animal()
            user = str(message.author).split("#")[0]
            #print(user)
            quoteMsg = "Hey, " + user + "! " + quote 
            await message.channel.send(quoteMsg)
            try:
                await message.channel.send(embed=animal)
            except:
                await message.channel.send(embed=animal)

def get_quote():
    quotes = requests.get("https://type.fit/api/quotes")
    quotesJsonData = json.loads(quotes.text)
    index = randrange(len(quotesJsonData))
    author = quotesJsonData[index]["author"]
    quoteText = quotesJsonData[index]['text'] 

    res = author + " once said: " + quoteText + " I hope this helps!"
    return res

def get_animal():
    index = randrange(len(animalApis))
    animalJsonData = json.loads(requests.get(animalApis[index]["link"]).text)
    
    #elephant
    #animal = animalJsonData[0]['image']
    #dog
    animal = animalJsonData['message']

    e = discord.Embed()
    e.set_image(url=animal)

    return e

def sync():
    link = "https://media1.tenor.com/images/09b9b6974b3935f31140e573ffaeebdc/tenor.gif"
    e = discord.Embed()
    e.set_image(url=link)
    return e

client.run('ODAwNTAzNjk0MjYxMDkyNDEz.YATFKQ.yzCrStAdUVcWERvyPSjeEWocoKI')