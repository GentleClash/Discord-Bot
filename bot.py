import discord, json, asyncio, openai, requests, spotipy
from spotipy.oauth2 import SpotifyOAuth
from discord.ext import commands
from config import *
from random import choice

intent = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intent, case_insensitive = True)
reminders = []

sp_oauth=SpotifyOAuth(scope = SCOPE, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,\
                      redirect_uri = REDIRECT_URL)
openai.api_key = OPENAI_API_KEY
spotify = spotipy.Spotify(auth_manager=sp_oauth)

commands_list={"!hello" : "Random greeting",
               "!set ": "Set reminder using format \'[MINUTES] [MESSAGE]\', eg: \"!set 2 maggie time\" ",
               "!show" : "Shows the reminders",
               "!join" : "Joins the voice channel. Note: User must have joined a voice channel.",
               "!leave" : "Leaves the voice channel",
               "!pause/!resume" : "Pause and Resume current audio respectively.",
               "!play" : "Play the song by spotify. Use format !play [SONG_NAME]",
               "!ask" : "ChatGPT. Use format !ask [PROMPT]"

}



@bot.event
async def on_ready():
    print("The bot is ready to use")
    await check_reminders()




@bot.command()
async def list(ctx, name: str = ""):
    if name == "":
        await ctx.send("The list of available commands:\n")
        for command, description in commands_list.items():
            await ctx.send(f"{command}: {description}")
    elif name in commands_list:
        await ctx.send(f"{name}: {commands_list[name]}")
    else:
        await ctx.send("Not found")



@bot.command()
async def hello(ctx):
    greet = ["Hello Sweetie ", "Damn You ", "Well, well, well ",\
             "Fancy seeing you here ", "Oh, it's you again ", \
             "Well, look what the cat dragged in " ]        #Of course its gonna be like this
    await ctx.send( choice(greet) + str(ctx.author.name))

@bot.command()
async def set(ctx, time: int, *, reminder: str):
    reminder_time = time * 60  # Convert minutes to seconds
    reminders.append((ctx.author.id, ctx.author.name, reminder, reminder_time))
    await ctx.send(f'Reminder set for {time} minutes: "{reminder}"')

async def check_reminders():
    while True:
        
        for reminder in reminders:
            userID, name, message, time_left = reminder
            user = await bot.fetch_user(userID)
            if time_left <= 0:
             await user.send(f'Reminder: {message}')
             reminders.remove(reminder)
            else:
                reminders[reminders.index(reminder)] = (userID, name, message, time_left - 10)
        await asyncio.sleep(10)

@bot.command()
async def show(ctx):
    for reminder in reminders:
        await ctx.send(f"User: {reminder[1]}, Message: {reminder[2]}, Time (seconds): {reminder[3]} \n" )

@bot.command()
async def join(ctx):
    if (ctx.author.voice):
        channel= ctx.message.author.voice.channel
        try:
            voice = await channel.connect()
        except discord.errors.ClientException:
            await ctx.send("Error joining")
    else:
        await ctx.send("You join the channel first dumbo.")

@bot.command()
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("What do you want me to leave huh, LET ME JOIN FIRST")

@bot.command()
async def pause(ctx):
    voice = ctx.voice_client
    if voice.is_playing():
        voice.pause()
        await ctx.send("Paused")
    else:
        await ctx.send("Pause What.")

@bot.command()
async def resume(ctx):
    voice = ctx.voice_client
    if voice.is_paused():
        voice.resume()
        await ctx.send("Resumed")
    else:
        await ctx.send("Resume what.")

@bot.command()
async def skip(ctx):
    ctx.voice_client.stop()
    await ctx.send("Stopped")

@bot.command()
async def ask(ctx, *, prompt: str):
    response = await get_gpt_response(prompt)
    await ctx.send(response)

async def get_gpt_response(prompt):
    model_engine = "text-davinci-003"  
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

@bot.command()
async def play(ctx, *, query):
    async with ctx.typing():
        results = spotify.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            #track_url = track['external_urls']['spotify']
            track_uri = track['uri']
            track_name = track['name']
            track_artist = track['artists'][0]['name']
            track_image = track['album']['images'][0]['url']

            spotify.start_playback(uris=[track_uri])

            ctx.voice_client.play(discord.FFmpegPCMAudio(track['preview_url']))

            embed = discord.Embed(title=track_name, description=f'by {track_artist}', color=discord.Color.green())
            embed.set_thumbnail(url=track_image)
            #embed.add_field(name='Spotify', value=f'[Listen on Spotify]({track_url})')
            await ctx.send(embed=embed)
        else:
            await ctx.send('No results found.')




bot.run(TOKEN)

    

