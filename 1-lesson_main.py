from aiogram import Bot, Dispatcher, executor, types
import config 
import time

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'go'])
async def start(message : types.Message):
    with open('users.txt', 'r', encoding='utf-8') as read_user:
        res = read_user.readlines()
        # print(res)
        
        for i in res:
            id = i.split()[1] 
            print(id)

            if id != res:
                with open('users.txt', 'a+', encoding='utf-8') as users:
                    users.write(f"{message.from_user.username} {message.from_user.id} {time.ctime()}\n")

            else:
                print("Ошибка")
        # for i in res:
        #     username = i.split()[0]
        #     if message.from_user.username ==username:
        #         pass
        #         # users.append(username)
        #         # if username in user:
        #         #     with open('users.txt', 'a+', encoding='utf-8') as user:
        #         #         user.write(f'{message.from_user.username} {message.from_user.id} {time.ctime()}\n')
        # else:
            
    await message.answer(f"Здраствуйте, {message.from_user.full_name} {message.from_user.id}")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Помощь")

@dp.message_handler(text = "Привет")
async def hello(message: types.Message):
    await message.answer("Привет")

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("Я вас не понял введите /help")

executor.start_polling(dp)