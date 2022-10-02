from javascript import require, On
import time
import json
import telebot
bot1 = telebot.TeleBot('5540404886:AAE-p0bNmyWSY8bV_Ab1piKysgwlvjeaRfI')
mineflayer = require('mineflayer')
while 1:
    try:
        bot = mineflayer.createBot({
          'host': 'dexland.su',
          'port': 25565,
          'username': 'botich554',
          'version': '1.12.2'
        })
        time.sleep(3)
        print(str(bot.players))
        h = []
        i = str(bot.players).split(",")
        bot.end()
        for i in i:
            try:
                h.append(str(i).split("\x1b[94musername\x1b[39m: \x1b[32m")[1][1:][:-6])
            except:
                pass

        if 'berendei_tv' in h:
            bot1.send_message(989911294,'berendei_tv играет на dexland.su')
    except:
        pass
