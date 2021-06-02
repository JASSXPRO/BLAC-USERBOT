# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in blac Userbot by @JATTGAMINGYT11

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, mafiaversion
from mafiabot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "BLAC- BOT"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

Mafia = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/fcb944ba85cd6d97e1e86.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "_🔥 𝙱𝙻𝙰𝙲 𝙱𝙾𝚃 𝙸𝚂 𝙾𝙽 𝙵𝙸𝚁𝙴 🔥_\n\n"


pm_caption += f"               ↼𝙼𝙰𝚂𝚃𝙴𝚁 ⇀\n**      『{DEFAULTUSER}』**\n\n"


pm_caption += "𖣘 𝙰𝙱𝙾𝚄𝚃 𝙼𝚈 𝚂𝚈𝚂𝚃𝙴𝙼 𖣘\n\n"
                   

pm_caption += "➾ 𝚃𝙷𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : 1.19.5\n"
pm_caption += "➾ 𝚃𝙴𝙰𝙼 𝙶𝚁𝙾𝚄𝙿  ➣ [𝙹𝙾𝙸𝙽](t.me/JATTGAMINGYTHACKS)\n"
pm_caption += "➾ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙽𝙽𝙴𝙻 ➣ [𝙹𝙾𝙸𝙽](https://t.me/BLACUSERBOT_SUPPORT)\n"
pm_caption += "➾ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 ➣ [𝙹𝙾𝙸𝙽](https://t.me/BLACUSERBOT_PUBLIC)\n"
pm_caption += "➾ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁    ➣ [⚡𝙱𝙻𝙰𝙲 𝙹𝙰𝚂𝚂⚡](@JATTGAMINGYT11)\n" 
                                        
pm_caption += " \n"
pm_caption += "[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙱𝙻𝙰𝙲✨](https://github.com/sameerpanthi/BLAC-2.0-BOT)"


# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "savage", None, "To check am i alive with your favorite alive pic"
).add()
