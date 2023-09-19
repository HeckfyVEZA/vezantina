import openai
import telebot
import streamlit as st


# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен, полученный от BotFather
TELEGRAM_BOT_TOKEN = '6093284738:AAF5tO9eSirDfT-nfXW22F_aXdZZbwz-vNg'

# Замените 'YOUR_OPENAI_API_KEY' на ваш ключ API от GPT-3
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
def generate_response(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Выберите нужную модель GPT
        messages = [{"role": "user", "content": input_text}],
        max_tokens=150  # Максимальная длина ответа
    )
    return response.choices[0].message.content

@bot.message_handler(content_types=['text'])
def resp_onse(message):
    bot.send_message(message.chat.id, generate_response(message.text))

if __name__=="__main__":
    st.set_page_config(layout='wide')
    bot.infinity_polling()