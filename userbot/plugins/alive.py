# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in blac Userbot by @JATTGAMINGYT11

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, SAVAGEversion
from SAVAGEbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
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

pm_caption = "_π₯ π±π»π°π² π±πΎπ πΈπ πΎπ½ π΅πΈππ΄ π₯_\n\n"


pm_caption += f"               βΌπΌπ°πππ΄π β\n**      γ{DEFAULTUSER}γ**\n\n"


pm_caption += "π£ π°π±πΎππ πΌπ πππππ΄πΌ π£\n\n"
                   

pm_caption += "βΎ ππ·π΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ : 1.19.5\n"
pm_caption += "βΎ ππ΄π°πΌ πΆππΎππΏ  β£ [πΉπΎπΈπ½](t.me/JATTGAMINGYTHACKS)\n"
pm_caption += "βΎ πππΏπΏπΎππ π²π·π½π½π΄π» β£ [πΉπΎπΈπ½](https://t.me/BLACUSERBOT_SUPPORT)\n"
pm_caption += "βΎ πππΏπΏπΎππ πΆππΎππΏ β£ [πΉπΎπΈπ½](https://t.me/BLACUSERBOT_PUBLIC)\n"
pm_caption += "βΎ π²ππ΄π°ππΎπ    β£ [β‘π±π»π°π² πΉπ°ππβ‘](@JATTGAMINGYT11)\n" 
                                        
pm_caption += " \n"
pm_caption += "[β¨ π³π΄πΏπ»πΎπ ππΎππ πΎππ½ π±π»π°π²β¨](https://github.com/sameerpanthi/BLAC-2.0-BOT)"


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

