import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

def parse_input(text):
    lines = text.lower().splitlines()
    data = {"ккал": 0, "белки": 0, "жиры": 0, "углеводы": 0, "вес": 100}
    for line in lines:
        for key in data:
            if key in line:
                try:
                    value = float(''.join(filter(lambda x: x.isdigit() or x=='.', line)))
                    data[key] = value
                except:
                    pass
    return data

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    data = parse_input(message.text)
    weight_ratio = data["вес"] / 100
    response = (
        f"На {data['вес']} г:
"
        f"Калории: {round(data['ккал'] * weight_ratio)}
"
        f"Белки: {round(data['белки'] * weight_ratio, 1)} г
"
        f"Жиры: {round(data['жиры'] * weight_ratio, 1)} г
"
        f"Углеводы: {round(data['углеводы'] * weight_ratio, 1)} г"
    )
    bot.reply_to(message, response)

if __name__ == "__main__":
    bot.polling()