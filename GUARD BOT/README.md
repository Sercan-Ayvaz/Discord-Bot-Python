# 🚨 Guard Bot 🚨

---

## 📜 About / Hakkında

**English:**  
Guard Bot is a powerful and user-friendly Discord moderation bot designed to help server admins manage users effectively with commands for moderation, warning & penalty tracking, and detailed logging.

**Türkçe:**  
Guard Bot, sunucu yöneticilerinin kullanıcıları kolayca yönetmesini sağlayan güçlü ve kullanımı kolay bir Discord moderasyon botudur. Moderasyon, uyarı & ceza takibi ve detaylı loglama özelliklerine sahiptir.

---

## ⚙️ Features / Özellikler

| 🇬🇧 English                                    | 🇹🇷 Türkçe                                    |
|-----------------------------------------------|---------------------------------------------|
| 🔨 Moderation commands: ban, kick, unban      | 🔨 Moderasyon komutları: ban, kick, unban  |
| 🔇 Text & voice mute/unmute, including timed voice mutes | 🔇 Metin & ses susturma/susturma kaldırma, zamanlı ses susturma dahil |
| ⚠️ Warning and penalty point system            | ⚠️ Uyarı ve ceza puanı sistemi               |
| 🧹 Bulk message deletion                        | 🧹 Çoklu mesaj silme                         |
| 📋 Detailed logging to channel & JSON files    | 📋 Logların kanala ve JSON dosyasına kaydedilmesi |
| 🛡️ Role-based permission control                | 🛡️ Rol bazlı yetki kontrolü                  |
| ❓ Help command showing all commands            | ❓ Komutların listelendiği yardım menüsü     |

---

## 🛠️ Commands / Komutlar

| 🇺🇸 **Command**               | 📘 **Description (EN)**                     | 🇹🇷 **Komut**                    | 📙 **Açıklama (TR)**                                         |
| ------------------------------ | ------------------------------------------- | --------------------------------- | ------------------------------------------------------------ |
| `!ban @user reason`            | Ban a user from the server                  | `!ban @kullanıcı sebep`           | Bir üyeyi sunucudan yasaklar                                 |
| `!unban user#0000` or `userID` | Unban by tag or ID                          | `!unban kullanıcı#0000` veya ID   | Kullanıcının yasağını kullanıcı etiketi veya ID ile kaldırır |
| `!kick @user reason`           | Kick a user from the server                 | `!kick @kullanıcı sebep`          | Bir üyeyi sunucudan atar                                     |
| `!mute @user reason`           | Mute a user in text channels                | `!mute @kullanıcı sebep`          | Metin kanallarında bir kullanıcıyı susturur                  |
| `!unmute @user`                | Remove text mute                            | `!unmute @kullanıcı`              | Metin susturmasını kaldırır                                  |
| `!vmute @user 10m reason`      | Voice mute a user for a duration (e.g. 10m) | `!vmute @kullanıcı 10dk sebep`    | Belirtilen süre boyunca sesli susturma uygular               |
| `!vunmute @user`               | Remove mute from voice channel              | `!vunmute @kullanıcı`             | Sesli susturmayı kaldırır                                    |
| `!clear <number>`              | Delete multiple messages from the channel   | `!clear <sayı>`                   | Belirli sayıda mesajı siler (1-100 arası)                    |
| `!profile @user (optional)`    | Show user profile information               | `!profile @kullanıcı (opsiyonel)` | Kullanıcının profil bilgilerini embed olarak gösterir        |

---

## 🚀 Setup & Installation / Kurulum & Yükleme

### English
1. Clone repository  
```
git clone https://github.com/yourusername/guard-bot.git
cd guard-bot
```

2. Create & activate virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Create .env file with your Discord token:
```
DISCORD_TOKEN=your_discord_bot_token_here
```

5. Run the bot:
```
python bot.py
```

### Türkçe
1. Depoyu klonlayın
```
git clone https://github.com/yourusername/guard-bot.git
cd guard-bot
```

2. Sanal ortam oluşturup aktif edin (önerilir)
```
python -m venv venv
source venv/bin/activate  # Linux/macOS için
venv\Scripts\activate     # Windows için
```

3. Gerekli kütüphaneleri yükleyin
```
pip install -r requirements.txt
```

4. .env dosyasına Discord tokenınızı ekleyin:
```
DISCORD_TOKEN=your_discord_bot_token_here
```

5. Botu başlatın:
```
python bot.py
```


## ⚙️ Configuration / Ayarlar
- **Log Channel / Log Kanalı:**\
The bot sends logs to a channel named guard-log. Create this or change the LOG_CHANNEL_NAME variable.
Bot logları guard-log adlı kanala gönderir. Bu kanalı oluşturun veya LOG_CHANNEL_NAME değişkenini değiştirin.
- **Roles / Roller:**\
Command permissions require roles: KURUCU, Yetkili, and <>. Adjust role names in code if needed.
Komutlar için KURUCU, Yetkili ve <> rollerinin olması gerekir. Gerekirse kodda değiştirin.

## 💾 Data Storage / Veri Saklama
- **Penalties:** Saved in penalties.json
- **Logs:** Saved in guard_logs.json and posted to the log channel

## 💻Example guard_logs.json content / Örnek guard_logs.json içeriği
```json
{
  "guild_id": [
    {
      "user_id": "123456789012345678",
      "user_tag": "ExampleUser#1234",
      "title": "User Warned",
      "description": "Warned for spamming in chat.",
      "executor_id": "987654321098765432",
      "executor_tag": "Moderator#5678",
      "channel": "mod-log",
      "date": "2025-06-26",
      "time": "20:00:00"
    },
    {
      "user_id": "123456789012345678",
      "user_tag": "ExampleUser#1234",
      "title": "User Banned",
      "description": "Banned for repeated offenses.",
      "executor_id": "987654321098765432",
      "executor_tag": "Admin#9999",
      "channel": "mod-log",
      "date": "2025-06-25",
      "time": "18:30:00"
    }
  ]
}
```

## 💻Example penalties.json content / Örnek penalties.json içeriği
```json
{
  "123456789012345678": {
    "points": 10,
    "warnings": [
      "Spamming in chat",
      "Using offensive language"
    ]
  },
  "987654321098765432": {
    "points": 5,
    "warnings": [
      "Posting inappropriate content"
    ]
  }
}
```

## 📄guard.py File Content / guard.py Dosya İçeriği
```python
import discord
from discord.ext import commands
from datetime import datetime, timedelta, timezone
import json
import os
from dotenv import load_dotenv
import asyncio

# Load .env file
# .env dosyasını yükle
load_dotenv()

# Get current time in Turkey timezone (UTC+3)
def get_current_tr_time():
    # Return datetime in Turkey timezone
    # Türkiye saatinde datetime döndürür
    return datetime.now(timezone.utc) + timedelta(hours=3)

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents(
    guilds=True,
    members=True,
    bans=True,
    emojis=True,
    integrations=False,
    webhooks=False,
    invites=True,
    voice_states=True,
    presences=True,
    messages=True,
    message_content=True,
    reactions=True,
    typing=True,
    guild_messages=True,
    dm_messages=True,
    guild_reactions=True,
    dm_reactions=True,
    guild_typing=True,
    dm_typing=True
)

bot = commands.Bot(command_prefix="!", intents=intents)

LOG_CHANNEL_NAME = "guard-log"  # Log channel name / Log kanalı adı
LOG_FILE = "guard_logs.json"    # Log file name / Log dosyası adı

def find_penalty(penalties, user_id):
    """
    Search for a user penalty record by user_id.
    Returns penalty dict if found, else None.
    ---
    Kullanıcı ceza kaydını user_id ile arar.
    Bulursa ceza dict döner, yoksa None döner.
    """
    for penalty in penalties:
        if penalty.get("user_id") == user_id:
            return penalty
    return None

def load_penalties():
    """
    Load penalties from JSON file.
    ---
    JSON dosyasından cezaları yükler.
    """
    if os.path.exists("penalties.json"):
        with open("penalties.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def save_penalties(data):
    """
    Save penalties dict to JSON file.
    ---
    Cezaları JSON dosyasına kaydeder.
    """
    with open("penalties.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def is_staff():
    """
    Check if command author has staff roles (OWNER, Staff, Software).
    ---
    Komutu kullananın KURUCU, Yetkili veya <> rolleri var mı kontrol eder.
    """
    async def predicate(ctx):
        owner_role = discord.utils.get(ctx.guild.roles, name="KURUCU")
        staff_role = discord.utils.get(ctx.guild.roles, name="Yetkili")
        software_role = discord.utils.get(ctx.guild.roles, name="<>")
        if owner_role in ctx.author.roles or staff_role in ctx.author.roles or software_role in ctx.author.roles:
            return True
        else:
            embed_log = discord.Embed(
                title="🚫 WARNING / UYARI",
                color=discord.Color.red(),
                description=f"🚫 You must have **{owner_role}** or **{staff_role}** role to use this command.")
            await ctx.send(embed=embed_log)
            return False
    return commands.check(predicate)

def save_log_json(ctx, guild_id, user: discord.Member, admin: discord.Member, title: str, description: str):
    """
    Save action log to JSON file.
    ---
    İşlem logunu JSON dosyasına kaydeder.
    """
    logs = {}
    current_time = get_current_tr_time()
    date_str = current_time.strftime("%Y-%m-%d")
    time_str = current_time.strftime("%H:%M:%S")

    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = {}

    guild_id = str(guild_id)
    if guild_id not in logs:
        logs[guild_id] = []

    log_entry = {
        "id": str(user.id),
        "tag": str(user),
        "title": title,
        "description": description,
        "executor_id": str(ctx.author.id),
        "executor_tag": str(ctx.author.mention),
        "channel": ctx.channel.name if hasattr(ctx, 'channel') else "DM",
        "date": date_str,
        "time": time_str
    }

    logs[guild_id].append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=4)

async def send_log(ctx, guild, user: discord.Member, admin: discord.Member, title: str, description: str):
    """
    Send log message to the designated log channel.
    ---
    Log kanalına embed olarak log gönderir.
    """
    log_channel = discord.utils.get(guild.text_channels, name=LOG_CHANNEL_NAME)
    current_time = get_current_tr_time()

    embed = discord.Embed(
        title=title,
        color=discord.Color.red(),
        timestamp=current_time
    )
    embed.add_field(name="👤 User", value=f"{user.mention} (`{user}`)", inline=False)
    embed.add_field(name="👮 Admin", value=f"{admin.mention} (`{admin}`)", inline=False)
    embed.add_field(name="📝 Description", value=description, inline=False)
    embed.add_field(name="🕒 Date", value=current_time.strftime("%d.%m.%Y"), inline=False)
    embed.add_field(name="📅 Time", value=current_time.strftime("%H:%M:%S"), inline=False)
    embed.set_footer(text="Guard Log System", icon_url=guild.icon.url if guild.icon else None)

    if log_channel:
        await log_channel.send(embed=embed)

    # Save to JSON log as well
    save_log_json(ctx=ctx, guild_id=guild.id, user=user, admin=admin, title=title, description=description)


### COMMANDS ###

@bot.command()
@is_staff()
async def ban(ctx, member: discord.Member = None, *, reason: str = None):
    """
    Ban a member from the guild.
    Usage: !ban @member reason
    ---
    Bir üyeyi sunucudan yasaklar.
    Kullanım: !ban @kullanıcı sebep
    """
    current_time = get_current_tr_time()
    if not member or not reason:
        await ctx.send(embed=discord.Embed(description="❗ Usage: `!ban @member reason`", color=discord.Color.red()))
        return
    try:
        await member.ban(reason=reason)
        description = (f"**Admin:** {ctx.author.mention}\n"
                       f"**User:** {member.mention}\n"
                       f"**Reason:** {reason}")
        embed = discord.Embed(title="User Banned", description=description, color=discord.Color.red(), timestamp=current_time)
        await ctx.send(embed=embed)
        await send_log(ctx, ctx.guild, admin=ctx.author, user=member, title="User Banned", description=description)
    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(description="🚫 I don't have permission to ban this user.", color=discord.Color.red()))
    except Exception as e:
        await ctx.send(embed=discord.Embed(description=f"❗ Error: {e}", color=discord.Color.red()))

@bot.command()
@is_staff()
async def unban(ctx, *, arg=None):
    """
    Unban a user by ID or username#discriminator.
    Usage: !unban username#0000 or !unban userID
    ---
    Bir kullanıcının banını kaldırır.
    Kullanım: !unban kullanıcı#0000 veya !unban kullanıcıID
    """
    if arg is None:
        await ctx.send(embed=discord.Embed(description="❗ Usage: `!unban username#0000` or `!unban userID`", color=discord.Color.red()))
        return

    try:
        # Try unban by ID
        if arg.isdigit():
            user = discord.Object(id=int(arg))
            await ctx.guild.unban(user)
            await ctx.send(embed=discord.Embed(description=f"♻️ Unbanned user with ID: <@{arg}>", color=discord.Color.green()))
            await send_log(ctx, ctx.guild, user=ctx.author, admin=ctx.author, title="User Unbanned", description=f"Admin: {ctx.author.mention}\nUser ID: {arg}")
            return
        # Try unban by username#discriminator
        async for ban_entry in ctx.guild.bans():
            banned_user = ban_entry.user
            full_name = f"{banned_user.name}#{banned_user.discriminator}"
            if full_name.lower() == arg.lower():
                await ctx.guild.unban(banned_user)
                await ctx.send(embed=discord.Embed(description=f"♻️ Unbanned user: {full_name}", color=discord.Color.green()))
                await send_log(ctx, ctx.guild, user=ctx.author, admin=ctx.author, title="User Unbanned", description=f"Admin: {ctx.author.mention}\nUser: {full_name}")
                return
        await ctx.send(embed=discord.Embed(description="❗ User not found or not banned.", color=discord.Color.red()))
    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(description="🚫 I don't have permission to unban this user.", color=discord.Color.red()))
    except Exception as e:
        await ctx.send(embed=discord.Embed(description=f"❗ Error: {e}", color=discord.Color.red()))

@bot.command()
@is_staff()
async def kick(ctx, member: discord.Member = None, *, reason: str = None):
    """
    Kick a member from the guild.
    Usage: !kick @member reason
    ---
    Bir üyeyi sunucudan atar.
    Kullanım: !kick @kullanıcı sebep
    """
    current_time = get_current_tr_time()
    if not member or not reason:
        await ctx.send(embed=discord.Embed(description="❗ Usage: `!kick @member reason`", color=discord.Color.red()))
        return
    try:
        await member.kick(reason=reason)
        description = (f"**Admin:** {ctx.author.mention}\n"
                       f"**User:** {member.mention}\n"
                       f"**Reason:** {reason}")
        embed = discord.Embed(title="User Kicked", description=description, color=discord.Color.orange(), timestamp=current_time)
        await ctx.send(embed=embed)
        await send_log(ctx, ctx.guild, admin=ctx.author, user=member, title="User Kicked", description=description)
    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(description="🚫 I don't have permission to kick this user.", color=discord.Color.red()))
    except Exception as e:
        await ctx.send(embed=discord.Embed(description=f"❗ Error: {e}", color=discord.Color.red()))

@bot.command()
@is_staff()
async def mute(ctx, member: discord.Member = None, *, reason: str = None):
    """
    Mute a member in text channels.
    Usage: !mute @member reason
    ---
    Bir üyeyi metin kanallarında susturur.
    Kullanım: !mute @kullanıcı sebep
    """
    current_time = get_current_tr_time()
    if not member or not reason:
        await ctx.send(embed=discord.Embed(description="❗ Usage: `!mute @member reason`", color=discord.Color.red()))
        return

    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        try:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False, add_reactions=False)
        except Exception as e:
            await ctx.send(embed=discord.Embed(description=f"❗ Could not create Muted role: {e}", color=discord.Color.red()))
            return

    try:
        await member.add_roles(muted_role, reason=reason)
        description = (f"**Admin:** {ctx.author.mention}\n"
                       f"**User:** {member.mention}\n"
                       f"**Reason:** {reason}")
        embed = discord.Embed(title="User Muted", description=description, color=discord.Color.gold(), timestamp=current_time)
        await ctx.send(embed=embed)
        await send_log(ctx, ctx.guild, user=member, admin=ctx.author, title="User Muted", description=description)
    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(description="🚫 I don't have permission to mute this user.", color=discord.Color.red()))
    except Exception as e:
        await ctx.send(embed=discord.Embed(description=f"❗ Error: {e}", color=discord.Color.red()))

@bot.command()
@is_staff()
async def unmute(ctx, member: discord.Member = None):
    """
    Remove mute role from a member.
    Usage: !unmute @member
    ---
    Bir üyenin metin susturmasını kaldırır.
    Kullanım: !unmute @kullanıcı
    """
    current_time = get_current_tr_time()
    if not member:
        await ctx.send(embed=discord.Embed(description="❗ Usage: `!unmute @member`", color=discord.Color.red()))
        return

    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        await ctx.send(embed=discord.Embed(description="❗ Muted role not found.", color=discord.Color.red()))
        return

    try:
        await member.remove_roles(muted_role)
        description = (f"**Admin:** {ctx.author.mention}\n"
                       f"**User:** {member.mention}")
        embed = discord.Embed(title="User Unmuted", description=description, color=discord.Color.green(), timestamp=current_time)
        await ctx.send(embed=embed)
        await send_log(ctx, ctx.guild, user=member, admin=ctx.author, title="User Unmuted", description=description)
    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(description="🚫 I can't remove mute from this user.", color=discord.Color.red()))
    except Exception as e:
        await ctx.send(embed=discord.Embed(description=f"❗ Error: {e}", color=discord.Color.red()))

@bot.command()
@is_staff()
async def vmute(ctx, member: discord.Member = None, duration: str = None, *, reason: str = None):
    """
    Mute a user in voice channel for a duration.
    Usage: !vmute @member 10m reason
    ---
    Bir üyeyi sesli kanalda belirtilen süre kadar susturur.
    Kullanım: !vmute @kullanıcı 10dk sebep
    """
    current_time = get_current_tr_time()
    if not member or not duration or not reason:
        await ctx.send(embed=discord.Embed(description="❗ Usage: `!vmute @member 10m reason`", color=discord.Color.red()))
        return

    if not member.voice or not member.voice.channel:
        await ctx.send(embed=discord.Embed(description="❗ User is not in a voice channel.", color=discord.Color.red()))
        return

    duration_map = {"s": 1, "sn": 1, "m": 60, "dk": 60, "h": 3600, "saat": 3600, "d": 86400, "gün": 86400}
    try:
        time_unit = ''.join([i for i in duration if not i.isdigit()]).lower()
        time_number = int(''.join([i for i in duration if i.isdigit()]))
        duration_seconds = time_number * duration_map.get(time_unit, 0)
        if duration_seconds == 0:
            raise ValueError("Invalid time unit")
    except:
        await ctx.send(embed=discord.Embed(description="⏱️ Enter a valid duration! E.g.: `10dk`, `30sn`, `1saat`", color=discord.Color.red()))
        return

    try:
        await member.edit(mute=True, reason=reason)

        embed = discord.Embed(
            title="🔇 User Muted (Voice)",
            description=(f"**Admin:** {ctx.author.mention}\n"
                         f"**User:** {member.mention}\n"
                         f"**Duration:** {duration}\n"
                         f"**Reason:** {reason}"),
            color=discord.Color.orange(),
            timestamp=current_time
        )
        await ctx.send(embed=embed)

        await asyncio.sleep(duration_seconds)

        await member.edit(mute=False, reason="Temporary mute expired.")

        unmute_embed = discord.Embed(
            title="🔊 User Unmuted (Voice)",
            description=f"{member.mention} can now speak.",
            color=discord.Color.green(),
            timestamp=get_current_tr_time()
        )
        await ctx.send(embed=unmute_embed)

    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(description="🚫 I don't have permission to mute this user.", color=discord.Color.red()))

@bot.command()
@is_staff()
async def vunmute(ctx, member: discord.Member = None):
    """
    Remove voice mute from a user.
    Usage: !vunmute @member
    ---
    Bir üyenin sesli susturmasını kaldırır.
    Kullanım: !vunmute @kullanıcı
    """
    current_time = get_current_tr_time()
    if not member:
        await ctx.send(embed=discord.Embed(description="❗ Usage: `!vunmute @member`", color=discord.Color.red()))
        return

    if not member.voice or not member.voice.channel:
        await ctx.send(embed=discord.Embed(description="❗ User is not in a voice channel.", color=discord.Color.red()))
        return

    try:
        await member.edit(mute=False, reason="Unmuted by staff.")
        embed = discord.Embed(
            title="🔊 Voice Unmute",
            description=f"{member.mention} can now speak.",
            color=discord.Color.green(),
            timestamp=current_time
        )
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(description="🚫 Insufficient permissions to remove mute.", color=discord.Color.red()))

@bot.command()
@is_staff()
async def clear(ctx, amount: int = 5):
    """
    Delete a specified number of messages in the channel.
    Usage: !clear 5
    ---
    Kanaldaki belirli sayıda mesajı siler.
    Kullanım: !clear 5
    """
    if amount < 1 or amount > 100:
        await ctx.send(embed=discord.Embed(description="❗ Please specify a number between 1 and 100.", color=discord.Color.red()))
        return

    try:
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f"🧹 Deleted {len(deleted)} messages.", color=discord.Color.green()), delete_after=5)
    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(description="🚫 I don't have permission to delete messages.", color=discord.Color.red()))

@bot.command()
@is_staff()
async def profile(ctx, member: discord.Member = None):
    """
    Show user's profile information.
    Usage: !profile @member
    ---
    Kullanıcının profil bilgilerini gösterir.
    Kullanım: !profile @kullanıcı
    """
    if not member:
        member = ctx.author

    embed = discord.Embed(
        title=f"Profile of {member}",
        color=discord.Color.blue(),
        timestamp=get_current_tr_time()
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.add_field(name="User ID", value=member.id, inline=True)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%d.%m.%Y %H:%M"), inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%d.%m.%Y %H:%M") if member.joined_at else "Unknown", inline=True)
    embed.add_field(name="Roles", value=", ".join([role.name for role in member.roles if role.name != "@everyone"]), inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)
```
