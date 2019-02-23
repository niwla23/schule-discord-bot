import discord
import datetime
import settings

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("schule - für Hilfe: *7F hilfe*")
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("schule hilfe"):
        await message.channel.send("Verfügbare Befehle:")
        await message.channel.send("1. plan - zeigt den Stundenplan für den nächsten Schultag an")
        await message.channel.send("2. vertreter - Schickt einen Link zum Vertretungsplan")

    if message.content.startswith('vertreter'):
        await message.channel.send('deineVertretungsplansAdresse.de')
        print(datetime.datetime.today().weekday())

    if message.content.startswith('plan'):
#Hier den Stundenplan einbauen
        if datetime.datetime.today().weekday() == 5: #Samstag
            await message.channel.send("Hier ist der Stunden plan für übermorgen:")
            await message.channel.send(settings.montag1)
            await message.channel.send(settings.montag2)
            await message.channel.send(settings.montag3)

        if datetime.datetime.today().weekday() == 6: #Sonntag
            await message.channel.send("Hier ist der Stunden plan für morgen:")
            await message.channel.send(settings.montag1)
            await message.channel.send(settings.montag2)
            await message.channel.send(settings.montag3)

        if datetime.datetime.today().weekday() == 0: #montag
            await message.channel.send("Hier ist der Stunden plan für morgen:")
            await message.channel.send(settings.dienstag1)
            await message.channel.send(settings.dienstag2)
            await message.channel.send(settings.dienstag3)

        if datetime.datetime.today().weekday() == 1: #dienstag
            await message.channel.send("Hier ist der Stunden plan für morgen:")
            await message.channel.send(settings.mittwoch1)
            await message.channel.send(settings.mittwoch2)
            await message.channel.send(settings.mittwoch3)

        if datetime.datetime.today().weekday() == 2: #mittwoch
            await message.channel.send("Hier ist der Stunden plan für morgen:")
            await message.channel.send(settings.donnerstag1)
            await message.channel.send(settings.donnerstag2)
            await message.channel.send(settings.donnerstag3)

        if datetime.datetime.today().weekday() == 3: #donnerstag
            await message.channel.send("Hier ist der Stunden plan für Freitag:")
            await message.channel.send(settings.freitag1)
            await message.channel.send(settings.freitag2)
            await message.channel.send(settings.freitag3)

        if datetime.datetime.today().weekday() == 4: # freitag
            await message.channel.send("Hier ist der Stunden plan für Montag:")
            await message.channel.send(settings.montag1)
            await message.channel.send(settings.montag2)
            await message.channel.send(settings.montag3)



client.run(settings.token)
