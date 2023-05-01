"""
chatgpt.py
-----------

This module contains the implementation of a Telegram bot that uses the OpenAI chat GPT API 
to generate responses to user messages.

Usage:
1. Set up a Telegram bot and obtain its token.
2. Set up an OpenAI account and obtain an API key.
3. Set the environment variables "TOKEN" and "OPENAI_API_KEY" 
    to the bot token and OpenAI API key, respectively.
4. Run this script to start the bot.

Note: This implementation uses the aiogram, openai library to interact with the Telegram API 
and the OpenAI API, respectively.

Example:
    $ python chatgpt.py

Author: Sunny BHaveen Chandra
"""

import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import openai

class Reference:
    """
    A class to store the previous response from the chatGPT API.
    """
    # raise NotImplementedError
    def __init__(self) ->None:
        self.response=""

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key=os.getenv("OPENAI_API_KEY")

# Create a reference object to store the previous response
reference=Reference()



# Bot token can be obtained via https://t.me/BotFahter
TOKEN = os.getenv("TOKEN")

# Model used in chatGPT
MODEL_NAME="gpt-3.5-turbo"



# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    """
    A function to clear the previous conversation and context.
    """
    # raise NotImplementedError
    reference.response=""







@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    A handler to welcome the user and 
    clear past conversation and context.
    """
    # raise NotImplementedError
    clear_past()
    await message.reply(f"hello!\nI am chat gpt bot created\
                         by shivansh!\nHow may I assist you today")

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    # raise NotImplementedError
    clear_past()
    await message.reply(f"I have cleared the past\
                         conversation and context")


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command="""
    Hi there, I'm chatGpt bot created by shivansh!. Please follow these commands-
    /start - to strt the conversation    
    /clear - to clear the past conversation and context
    /help - to get this help menu.
    I hope this helps.
    """
    # raise NotImplementedError
    await message.reply(help_command)



@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    # raise NotImplementedError
    
    print(f">>> USER:\n\t{message.text}")
    response=openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role":"assistant","content": reference.response},
            {"role":"user", "content":message.text}
        ]
    )
    reference.response=response['choices'][0]['message']['content']

    print(f">>> chatGpt:\n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id,
                           text=reference.response)


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)