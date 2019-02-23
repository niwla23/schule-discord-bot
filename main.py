import discord
import datetime

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
            await message.channel.send("1/2: Spanisch bei Fr. X")
            await message.channel.send("3/4: Fach1 bei Hr. X")
            await message.channel.send("5/6: Kunst bei Herr X")

        if datetime.datetime.today().weekday() == 6: #Sonntag
            await message.channel.send("Hier ist der Stunden plan für morgen:")
            await message.channel.send("1/2: Spanisch bei Fr. X")
            await message.channel.send("3/4: Fach1 bei Hr. X")
            await message.channel.send("5/6: Kunst bei Herr X")

        if datetime.datetime.today().weekday() == 0: #montag
            await message.channel.send("Hier ist der Stunden plan für morgen:")
            await message.channel.send("1/2: Fach1 bei Fr. X")
            await message.channel.send("3/4: Sport bei Hr. X")
            await message.channel.send("5/6: Physik bei Hr. X")

        if datetime.datetime.today().weekday() == 1: #dienstag
            await message.channel.send("Hier ist der Stunden plan für morgen:")
            await message.channel.send("1/2: Fach1 bei Hr. X")
            await message.channel.send("3/4: Spanisch bei Fr. X")
            await message.channel.send("5/6: Geschichte bei Fr. Norden")

        if datetime.datetime.today().weekday() == 2: #mittwoch
            await message.channel.send("Hier ist der Stunden plan für morgen:")
            await message.channel.send("1/2: Fach1 bei Hr. X")
            await message.channel.send("3/4: Erdkunde bei Fr. X")
            await message.channel.send("5/6: Fach1 bei Fr. X")

        if datetime.datetime.today().weekday() == 3: #donnerstag
            await message.channel.send("Hier ist der Stunden plan für Freitag:")
            await message.channel.send("1/2: Bio bei Hr. X")
            await message.channel.send("3/4: Religion bei Hr. X (richtig?)")
            await message.channel.send("5/6: Fach1 bei Hr. X")

        if datetime.datetime.today().weekday() == 4: # freitag
            await message.channel.send("Hier ist der Stunden plan für Montag:")
            await message.channel.send("1/2: Spanisch bei Fr. X")
            await message.channel.send("3/4: Fach1 bei Hr. X")
            await message.channel.send("5/6: Kunst bei Herr X")



client.run('TOKEN')
