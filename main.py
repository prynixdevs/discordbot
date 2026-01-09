
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio
import requests
from back import answer
#
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Welcome!",
        description=f"Welcome to {member.guild.name} server, {member.name}!",
        color=0x00ff00
    )
    try:
        await member.send(embed=embed)
    except:
        print(f"Could not DM {member.name}")

@bot.event
async def on_member_remove(member):
    embed = discord.Embed(
        title="Goodbye!",
        description=f"You left {member.guild.name} server, {member.name}!",
        color=0xff0000
    )
    try:
        await member.send(embed=embed)
    except:
        print(f"Could not DM {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        try:
            response = answer(message.content)
            await message.channel.send(response)
        except Exception as e:
            await message.channel.send(f'Error: {e}')
    await bot.process_commands(message)

@bot.command()
async def kick4(ctx, member: discord.Member):
    if not (ctx.author.guild_permissions.administrator or 
            discord.utils.get(ctx.author.roles, name="Moderator")):
        await ctx.send("🚫 You don’t have permission to use this command.")
        return
    await ctx.message.delete()
    await member.kick()
    embed = discord.Embed(
        title="User Kicked",
        description=f" {member.mention} has been kicked from the server.",
        color=0xff0000
    )
    await ctx.send(embed=embed)

@bot.command()
async def spam(ctx, times: int, *, text: str):
    if not (ctx.author.guild_permissions.administrator or 
            discord.utils.get(ctx.author.roles, name="Moderator")):
        await ctx.send("🚫 You don’t have permission to use this command.")
        return
    for i in range(times):
        await ctx.send(text)
        await asyncio.sleep(1)

@bot.command()
async def calc(ctx, *, expression: str):
    try:
        result = eval(expression)
        embed = discord.Embed(
            title="Calculation Result",
            description=f"`The result of {expression} is`\n## {result}",
            color=0x41acd0
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command()
async def chat(ctx, *, user_message):
    try:
        response = answer(user_message)
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command()
async def notifyall(ctx, title: str, *, description: str):
    if not (ctx.author.guild_permissions.administrator or 
         discord.utils.get(ctx.author.roles, name="Moderator")):
        await ctx.send("🚫 You don’t have permission to use this command.")
        return
    await ctx.message.delete()

    notifyall = discord.Embed(
        title="Notification",
        description=f" {ctx.author.mention} has notified all.",
        color=0x41acd0
    )
    await ctx.send(embed=notifyall)
    embed = discord.Embed(title=title, description=description, color=0x41acd0)
    failed = 0
    for member in ctx.guild.members:
        if member.bot:  
            continue
        try:
            await member.send(embed=embed)
            await asyncio.sleep(1)
        except:
            failed += 1
    if failed == 0:
        response = discord.Embed(description="Notification sent to all members.", color=0x41acd0)
        await ctx.send(embed=response)
    else:
        response = discord.Embed(description=f"Notification sent. Failed to DM {failed} member(s).", color=0xff0000)
        await ctx.send(embed=response)

@bot.command()
async def notify(ctx, member: discord.Member, title: str, *, description: str):
    await ctx.message.delete()
    notifyall = discord.Embed(
        title="Notification",
        description=f" {ctx.author.mention} has notified {member.mention}.",
        color=0x41acd0
    )
    await ctx.send(embed=notifyall)
    embed = discord.Embed(title=title, description=description, color=0x41acd0)
    if member.bot:  
        await ctx.send("🚫 Cannot notify bots.")
        return
    try:
        await member.send(embed=embed)
        response = discord.Embed(description=f"✅ **Notification sent to {member.name}.**", color=0x41acd0)
        await ctx.send(embed=response)
    except Exception as e:
        await ctx.send(f"Error: {e}")


@bot.command()
async def announcement(ctx, title: str, *, description: str):
    await ctx.message.delete()
    if not (ctx.author.guild_permissions.administrator or 
            discord.utils.get(ctx.author.roles, name="Moderator")):
        await ctx.send("🚫 You don’t have permission to use this command.")
        return
 
    embed = discord.Embed(title=title, description=description, color=0x41acd0)
    try:
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f'Error: {e}')
@bot.command()
async def mathquote(ctx):
    try:
        response = requests.get('https://mathex.onrender.com/api/quotes')
        data = response.json()
        
        quote = data.get('quote', 'No quote available')
        author = data.get('author', 'Unknown')
        
        embed = discord.Embed(
            description=f"## {quote}",
            color=0x41acd0
        )
        embed.set_footer(text=f"— {author}")
        
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f'Error fetching math quote: {e}')

bot.run(token, log_handler=handler, log_level=logging.DEBUG)