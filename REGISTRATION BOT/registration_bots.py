import discord
from discord.ext import commands
from datetime import datetime
import pytz
import json
import os
from dotenv import load_dotenv

# ---------- Load token from .env ----------
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ---------- Role & Channel Settings ----------
ROLE_AUTHORIZED = "Staff"           # Role allowed to register members
ROLE_UNREGISTERED = "Unregistered"  # Default role for new members
ROLE_MEMBER = "Member"              # Role assigned after registration

CHANNEL_WELCOME = "welcome"                  # Welcome channel name
CHANNEL_REGISTRATION_LOG = "registration-log"  # Log channel for registrations

DATA_FILE = "registrations.json"

# ---------- Bot Setup ----------
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

# Timezone for Turkey
tr_tz = pytz.timezone('Europe/Istanbul')

# ---------- Load registrations from file ----------
def load_registrations():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# ---------- Save registrations to file ----------
def save_registrations(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ---------- Event: When a new member joins ----------
@bot.event
async def on_member_join(member):
    unregistered_role = discord.utils.get(member.guild.roles, name=ROLE_UNREGISTERED)
    if unregistered_role:
        try:
            await member.add_roles(unregistered_role)
            print(f"✅ Assigned '{ROLE_UNREGISTERED}' role to {member}.")
        except discord.Forbidden:
            print(f"❌ Failed to assign '{ROLE_UNREGISTERED}' to {member}.")
    else:
        print(f"⚠️ Role '{ROLE_UNREGISTERED}' not found!")

    channel = discord.utils.get(member.guild.text_channels, name=CHANNEL_WELCOME)
    if channel:
        now = datetime.now(tr_tz)
        account_creation = member.created_at.astimezone(tr_tz)
        diff_days = (now - account_creation).days
        diff_years = diff_days // 365

        embed = discord.Embed(
            title="🎉 Welcome!",
            description=f"Thanks for joining us, {member.mention}!",
            color=discord.Color.green()
        )
        embed.add_field(name="👤 Username", value=str(member), inline=True)
        embed.add_field(name="🆔 User ID", value=member.id, inline=True)
        embed.add_field(name="📅 Account Created", value=f"{diff_years} years ago", inline=True)
        embed.add_field(name="📥 Joined At", value=member.joined_at.astimezone(tr_tz).strftime("%d.%m.%Y %H:%M"), inline=False)
        embed.set_footer(text="Hope you have a great time here!")
        embed.set_image(url="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWo5OHI0Y3phNmd6dGdpNDdiZ2JjcmZ4eHV1dnlkY2ttN2lnbWVqdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8V9GmJZ16qnCid8d0r/giphy.gif")

        await channel.send(embed=embed)

# ---------- Command: .k @member name age ----------
@bot.command()
@commands.has_role(ROLE_AUTHORIZED)
async def k(ctx, member: discord.Member, name: str, age: str):
    unregistered_role = discord.utils.get(ctx.guild.roles, name=ROLE_UNREGISTERED)
    member_role = discord.utils.get(ctx.guild.roles, name=ROLE_MEMBER)

    if unregistered_role in member.roles:
        try:
            await member.remove_roles(unregistered_role)
        except discord.Forbidden:
            await ctx.send(f"❌ Failed to remove '{ROLE_UNREGISTERED}' from {member.mention}.")
            return

    if member_role:
        try:
            await member.add_roles(member_role)
        except discord.Forbidden:
            await ctx.send(f"❌ Failed to assign '{ROLE_MEMBER}' to {member.mention}.")
            return
    else:
        await ctx.send(f"⚠️ Role '{ROLE_MEMBER}' not found!")

    new_nickname = f"❈ » {name} [{age}]"
    try:
        await member.edit(nick=new_nickname)
    except discord.Forbidden:
        await ctx.send(f"❌ Failed to change nickname for {member.mention}.")

    now_tr = datetime.now(tr_tz)

    registrations = load_registrations()
    registrations[str(member.id)] = {
        "name": name,
        "age": age,
        "date": now_tr.strftime("%d.%m.%Y"),
        "time": now_tr.strftime("%H:%M"),
        "registered_by": str(ctx.author)
    }
    save_registrations(registrations)

    log_channel = discord.utils.get(ctx.guild.text_channels, name=CHANNEL_REGISTRATION_LOG)
    if log_channel:
        embed_log = discord.Embed(
            title="✅ New Registration",
            color=discord.Color.blue(),
            timestamp=now_tr
        )
        embed_log.add_field(name="👤 User", value=member.mention, inline=True)
        embed_log.add_field(name="📛 Name", value=name, inline=True)
        embed_log.add_field(name="🎂 Age", value=age, inline=True)
        embed_log.add_field(name="📅 Date", value=registrations[str(member.id)]["date"], inline=True)
        embed_log.add_field(name="🕒 Time", value=registrations[str(member.id)]["time"], inline=True)
        embed_log.add_field(name="👮 Registered By", value=ctx.author.mention, inline=True)

        await log_channel.send(embed=embed_log)

    welcome_channel = discord.utils.get(ctx.guild.text_channels, name=CHANNEL_WELCOME)
    if welcome_channel:
        embed_panel = discord.Embed(
            title=f"🎉 {member.name} registered successfully!",
            description=f"Welcome {member.mention}, we’re happy to have you!",
            color=discord.Color.green(),
            timestamp=now_tr
        )
        embed_panel.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed_panel.add_field(name="📛 Name", value=name, inline=True)
        embed_panel.add_field(name="🎂 Age", value=age, inline=True)
        embed_panel.add_field(name="🕒 Registration Time", value=registrations[str(member.id)]["time"], inline=True)
        embed_panel.add_field(name="📅 Registration Date", value=registrations[str(member.id)]["date"], inline=True)
        embed_panel.add_field(name="👮 Registered By", value=ctx.author.mention, inline=True)
        embed_panel.set_footer(text="Enjoy your stay! ❤️")

        await welcome_channel.send(embed=embed_panel)

    await ctx.send(f"✅ {member.mention} has been successfully registered!")

# ---------- Error Handling for .k ----------
@k.error
async def k_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"❌ You must have the '{ROLE_AUTHORIZED}' role to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Missing arguments! Correct usage: `.k @member name age`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Invalid user! Please mention a valid member.")
    else:
        await ctx.send(f"❌ An error occurred: {error}")

# ---------- Run the bot ----------
bot.run(TOKEN)
