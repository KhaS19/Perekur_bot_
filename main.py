import telebot
import config
import time

bot = telebot.TeleBot(config.id)
list_of_id = [534098407, 1028100356]

@bot.message_handler(commands=['go_perekur'])
def hello_message(message):
  message = bot.send_message(message.chat.id, 'Через скок перекур?')
  bot.register_next_step_handler(message, send_next_text)

def send_next_text(message):
  time_ = int(message.text)
  time_end = float(time_)
  if message.chat.id == list_of_id[0]:
      bot.send_message(list_of_id[0], f'Инициатор: Илюха\nПерекур запланирован через {int(time_end)} минут.')
      bot.send_message(list_of_id[1], f'Инициатор: Илюха\nПерекур запланирован через {int(time_end)} минут.')
  else:
      bot.send_message(list_of_id[0], f'Инициатор: Саня\nПерекур запланирован через {int(time_end)} минут.')
      bot.send_message(list_of_id[1], f'Инициатор: Саня\nПерекур запланирован через {int(time_end)} минут.')


  for i in range(1,time_+ 2):
    time_end = float(time_ - i + 1)
    # print(time_end)
    if time_end > 0:
      if time_end == 45 or time_end == 30 or time_end == 15 or time_end == 5:
        bot.send_message(list_of_id[0], f'До перекура осталось {int(time_end)} минут(ы)')
        bot.send_message(list_of_id[1], f'До перекура осталось {int(time_end)} минут(ы)')
    else:
      bot.send_message(list_of_id[0], 'Го!')
      bot.send_message(list_of_id[1], 'Го!')
    # print(i)
    time.sleep(60)


@bot.message_handler(commands=['ebanaya_uniforma'])
def fuck_this_shit(message):
  time_ = 60
  time_end = float(time_)
  if message.chat.id == list_of_id[0]:
      bot.send_message(list_of_id[0], f'Инициатор: Илюха\nПерекур запланирован через {int(time_end)} минут.')
      bot.send_message(list_of_id[1], f'Инициатор: Илюха\nПерекур запланирован через {int(time_end)} минут.')
  else:
      bot.send_message(list_of_id[0], f'Инициатор: Саня\nПерекур запланирован через {int(time_end)} минут.')
      bot.send_message(list_of_id[1], f'Инициатор: Саня\nПерекур запланирован через {int(time_end)} минут.')


  for i in range(1,time_+ 2):
    time_end = float(time_ - i + 1)
    # print(time_end)
    if time_end > 0:
        if time_end == 45 or time_end == 30 or time_end == 15 or time_end == 5:
            bot.send_message(list_of_id[0], f'До перекура осталось {int(time_end)} минут(ы)')
            bot.send_message(list_of_id[1], f'До перекура осталось {int(time_end)} минут(ы)')
        else:
            pass

    else:
      bot.send_message(list_of_id[0], 'Го!')
      bot.send_message(list_of_id[1], 'Го!')
    print(time_end)
    time.sleep(60)

@bot.message_handler(commands=['test'])
def check_work(message):
    bot.send_message(message.chat.id, 'Бот работает корректно!\nПерезапуск не требуется')


@bot.message_handler(commands=['check_id'])
def get_id(message):
  print(message.chat.id)

if __name__ == '__main__':
  bot.polling(none_stop=True)
