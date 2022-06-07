from aiogram import Bot,types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from json import load, dumps
from pprint import pprint
from art import tprint
API = '5475092352:AAGUJE12377OcF4qzupYhhekL1L7F3Rty8o'
with open('degrees.json') as f:
    links = load(f)
bot = Bot(token=API)
dp = Dispatcher(bot)

linkstum = links['tum']
linksoxf = links['oxford']
linkssta = links['stanford']
del links
def search_in_links(link,search):
    tmp = None
    for i in link.keys():
        if search.strip().lower() in i.lower():
            tmp = i
            break
    if tmp == None:
        return ['I cant see anything here😔',None,['No degree']]
    else:
        return [tmp,link[tmp]["url"],link[tmp]["degree"]]
#id
@dp.message_handler(commands='id')
async def iduser(msg:types.Message):
    await msg.reply(msg["from"]["id"])


@dp.message_handler(commands='help')
async def bothelp(msg:types.Message):
    await msg.answer('--- Hello I\'m ParserBot ---\nI can search some info from\nTUM,Oxford and Harvard degrees\n--- Have a nice day ---')
@dp.message_handler(commands='search')
async def answer_url(msg:types.Message):
    temp = msg['text'][8:]
    linkoxf = search_in_links(link=linksoxf,search=temp)
    linktum = search_in_links(link=linkstum,search=temp)
    linksta = search_in_links(link=linkssta,search=temp)
    await msg.answer(f'------Oxford------\n<a href="{linkoxf[1]}">{linkoxf[0]}</a>\nDegree: {", ".join(linkoxf[2])}\n--------TUM--------\n<a href="{linktum[1]}">{linktum[0]}</a>\nDegree: {", ".join(linktum[2])}\n------Stanford------\n<a href="{linksta[1]}">{linksta[0]}</a>\nDegree: {", ".join(linksta[2])}\n',parse_mode=types.ParseMode.HTML)
@dp.message_handler()
async def allmsg(msg: types.Message):
    await msg.answer('Введите сообщение с командой')


if __name__ == '__main__':
    executor.start_polling(dp)
    