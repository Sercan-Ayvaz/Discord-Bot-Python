# 💻Discord Registration Bot / Discord Kayıt Botu

---

## 📝Description / Açıklama

**English:**  
This bot automatically assigns the **"Unregistered"** role to new members when they join the server.

Authorized users with the **"Staff"** role can register members using the `.k` command by providing their name and age.

When a member is registered:  
- The **"Unregistered"** role is removed  
- The **"Member"** role is added  
- The member's nickname is changed to: `❈ » Name [Age]`  
- Registration data is saved in `registrations.json`  
- A log is sent to the **"registration-log"** channel  
- A welcome message is sent to the **"welcome"** channel  

**Türkçe:**  
Bu bot, sunucuya katılan yeni üyeye otomatik olarak **"Kayıtsız"** rolünü verir.

**"Yönetim"** rolüne sahip yetkililer `.k` komutunu kullanarak üyeleri isim ve yaş bilgisiyle kayıt edebilir.

Üye kayıt edildiğinde:  
- **"Kayıtsız"** rolü kaldırılır  
- **"Üye"** rolü verilir  
- Üyenin takma adı `❈ » İsim [Yaş]` formatına değiştirilir  
- Kayıt bilgileri `registrations.json` dosyasına kaydedilir  
- Kayıt bilgisi **"registration-log"** kanalına gönderilir  
- Hoş geldin mesajı **"welcome"** kanalına gönderilir  

---

## 📚Libraries Used / Kullanılan Kütüphaneler

- `discord.py`  
- `python-dotenv`  
- `pytz`  

---

## 📥Installation and Usage / Kurulum ve Kullanım

1. Clone the repository / Depoyu klonlayın:  
```bash
git clone <repository-url>
```

2. Install dependencies / Gerekli paketleri yükleyin:
```
pip install -r requirements.txt
```

3. 🔑Copy .env.example to .env and add your Discord bot token / .env.example dosyasını .env olarak kopyalayın ve Discord bot tokenınızı ekleyin:
```
DISCORD_TOKEN="YOUR_DISCORD_BOT_TOKEN_HERE"
```

4. Run the bot / Botu çalıştırın:
```
python bot.py
```
## Commands / Komutlar
```
.k @member name age
```
- Used by users with the Staff role / Yönetim rolüne sahip kullanıcılar kullanır.

- Removes the Unregistered role, adds the Member role, changes nickname, and logs the registration / Kayıtsız rolü kaldırılır,
Üye rolü verilir, isim ve yaş nickname olarak ayarlanır, kayıt loglanır.



## 🛠File Contents / Dosya İçerikleri
- bot.py: Main Python bot file / Ana Python bot dosyası
- .env.example: Example environment variables file / Örnek çevresel değişken dosyası
- requirements.txt: List of required Python packages / Gerekli Python paketleri listesi
- registrations.json: Registration data JSON file, created automatically / Kayıt verilerinin tutulduğu JSON dosyası (bot tarafından otomatik oluşturulur)

## 💻Example registrations.json content / Örnek registrations.json içeriği
```json
{
    "123456789012345678": {
        "name": "Ahmet",
        "age": "25",
        "date": "24.06.2025",
        "time": "16:30",
        "registered_by": "Admin#1234"
    },
    "987654321098765432": {
        "name": "Mehmet",
        "age": "22",
        "date": "24.06.2025",
        "time": "17:00",
        "registered_by": "Staff#5678"
    }
}
```
## ⚠Notes / Dikkat Edilmesi Gerekenler
- Copy .env.example to .env and insert your own bot token / .env.example dosyasını kopyalayıp kendi .env dosyanızı oluşturun.
- Make sure the roles (Staff, Unregistered, Member) and channels (welcome, registration-log) exist on your server / Roller
(Yönetim, Kayıtsız, Üye) ve kanallar (welcome, registration-log) sunucunuzda oluşturulmuş olmalıdır.


## 📄registration_bots.py File Content / registration_bots.py Dosya İçeriği
```python
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
```
