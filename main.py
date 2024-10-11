from aiogram import Bot, types, Dispatcher, executor, types, filters
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from information import *
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
premier_league = len(matchestoday("https://www.readfootball.com/football-england/tournaments/premer-liga/calendar.html"))
bundesliga = len(matchestoday("https://www.readfootball.com/football-germany/tournaments/bundesliga/calendar.html"))
league1 = len(matchestoday("https://www.readfootball.com/football-france/tournaments/liga1/calendar.html"))
seriea = len(matchestoday("https://www.readfootball.com/football-italy/tournaments/seriya-a/calendar.html"))
laliga = len(matchestoday("https://www.readfootball.com/football-italy/tournaments/seriya-a/calendar.html"))
champions_league = len(matchestoday("https://www.readfootball.com/football-europe/tournaments/liga-chempionov/calendar.html"))
europa_league = len(matchestoday("https://www.readfootball.com/football-europe/tournaments/liga-evropy/calendar.html"))
copadelrey = len(kubki("https://www.readfootball.com/football-spain/tournaments/kubok.html"))
facup = len(kubki("https://www.readfootball.com/football-england/tournaments/kubok-fa.html"))
coupedefrance = len(kubki("https://www.readfootball.com/football-france/tournaments/kubok-ligi.html"))
dfb_pokal = len(kubki("https://www.readfootball.com/football-germany/tournaments/kubok.html"))
carabaocup = len(kubki("https://www.readfootball.com/football-england/tournaments/kubok.html"))
coppaitalia = len(kubki("https://www.readfootball.com/football-italy/tournaments/kubok.html"))
#Создание строки топ 5 лиг
def strokatop5():
    matches = "Сегодня есть матчи в топ 5 лигах!!"
    count = 0
    if premier_league != 0:
        matches += "\nPremier League"
        count += 1
    if bundesliga != 0:
        matches += "\nBundesliga"
        count += 1
    if seriea != 0:
        matches += "\nSerie A"
        count += 1
    if league1 != 0:
        matches += "\nLeague 1 Uber Eats"
        count += 1
    if laliga != 0:
        matches += "\nLaliga"
        count += 1
    if count == 0:
        matches = "Сегодня к сожалению нет матчей в топ лигах!!!"
    else:
        matches += "\nКакую лигу предпочитаешь смотреть?"
    return matches
#Строка Еврокубков
def strokaeuro():
    matches = "Сегодня есть матчи в еврокубках!!!"
    count = 0
    if champions_league != 0:
        count += 1
        matches += "\nChampions League"
    if europa_league != 0:
        count += 1
        matches += "\nEuropa League"
    if count == 0:
        matches = "Сегодня к сожалению нет матчей в еврокубках!!!"
    else:
        matches += "\nЧто предпочитаешь смотреть?"
    return matches

#Строка Кубков
def strokacups():
    matches = "Сегодня есть матчи в кубках!!!"
    count = 0
    if facup != 0:
        count += 1
        matches += "\nFA Cup"
    if carabaocup != 0:
        count += 1
        matches += "\nCarabao Cup"
    if coppaitalia != 0:
        count += 1
        matches += "\nCoppa Italia"
    if copadelrey != 0:
        count += 1
        matches += "\nCopa Del Rey"
    if dfb_pokal != 0:
        count += 1
        matches += "\nDFB-Pokal"
    if coupedefrance != 0:
        count += 1
        matches += "\nCouoe De France"
    if count == 0:
        matches = "Сегодня к сожалению нет матчей в кубках!!!"
    else:
        matches += "\nКакой кубок предпочитаешь смотреть?"
    return matches


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    user_name = message.from_user.first_name
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(text="Матчи в топ 5 лигах"), KeyboardButton(text="Матчи в еврокубках"),
               KeyboardButton(text="Матчи в кубках")]
    keyboard.add(*buttons)
    await message.answer(f"Привет, {user_name}! Как я могу тебе помочь?.", reply_markup=keyboard)
matchesleagues = strokatop5()
matcheseuro = strokaeuro()
matchescups = strokacups()
# Матчи в топ 5 лигах
@dp.message_handler(lambda message: message.text == "Матчи в топ 5 лигах")
async def top5leagues(message: Message):
    global matchesleagues
    await message.answer(matchesleagues)
    if lambda message: message.text.lower() == "premier league":
        pl()
    if lambda message: message.text.lower() == "serie a":
        seriea()
    if lambda message: message.text.lower() == "bundesliga":
        bundesliga()
    if lambda message: message.text.lower() == "league 1 uber eats":
        league1ubereats()
    if lambda message: message.text.lower() == "laliga":
        laliga()

#Матчи в еврокубках
@dp.message_handler(lambda message: message.text == "Матчи в еврокубках")
async def euromatches(message: Message):
    global matcheseuro
    await message.answer(matcheseuro)
    if lambda message: message.text.lower() == "champions League":
        ucl()
    if lambda message: message.text.lower() == "europa League":
        uel()

#    if lambda message: message.text.lower() == "conference League":
#        uecl()

#Матчи в кубках
@dp.message_handler(lambda message: message.text == "Матчи в кубках")
async def cupmatches(message: Message):
    global matchescups
    await message.answer(matchescups)
    if lambda message: message.text.lower() == "fa cup":
        facup()
    if lambda message: message.text.lower() == "carabao Cup":
        carabaocup()
    if lambda message: message.text.lower() == "dfb-pokal":
        dfb_pokal()
    if lambda message: message.text.lower() == "coupe de france":
        coupedefrance()
    if lambda message: message.text.lower() == "copa del rey":
        copadelrey()
    if lambda message: message.text.lower() == "coppa italia":
        coppaitalia()
#Апл
def pl():
    league = "https://www.readfootball.com/football-england/tournaments/premer-liga/calendar.html"
    @dp.message_handler(lambda message: message.text.lower() == "premier league")
    async def pl(message: Message):
        await message.answer(f"Понял, сегодня в Premier League сегодня есть такие матчи: \n {matchestoday(league)}")
    return league

#Серия а
def seriea():
    league = "https://www.readfootball.com/football-italy/tournaments/seriya-a/calendar.html"
    @dp.message_handler(lambda message: message.text.lower() == "serie a")
    async def seriea(message: Message):
        await message.answer(f"Понял, сегодня в Serie A сегодня есть такие матчи: \n {matchestoday(league)}")
    return league

#Бундеслига
def bundesliga():
    league = "https://www.readfootball.com/football-germany/tournaments/bundesliga/calendar.html"
    @dp.message_handler(lambda message: message.text.lower() == "bundesliga")
    async def bundesliga(message: Message):
        await message.answer(f"Понял, сегодня в Bundesliga сегодня есть такие матчи: \n {matchestoday(league)}")
    return league

#League 1 Uber Eats
def league1ubereats():
    league = "https://www.readfootball.com/football-france/tournaments/liga1/calendar.html"
    @dp.message_handler(lambda message: message.text.lower() == "league 1 uber eats")
    async def seriea(message: Message):
        await message.answer(f"Понял, в League 1 Uber Eats сегодня есть такие матчи: \n {matchestoday(league)}")

#Laliga
def laliga():
    league = "https://www.readfootball.com/football-spain/tournaments/primera/calendar.html"
    @dp.message_handler(lambda message: message.text.lower() == "laliga")
    async def laliga(message: Message):
        await message.answer(f"Понял, в Laliga сегодня есть такие матчи: \n {matchestoday(league)}")

#Champions League
def ucl():
    league = "https://www.readfootball.com/football-europe/tournaments/liga-chempionov/calendar.html"
    @dp.message_handler(lambda message: message.text.lower() == "champions league")
    async def ucl(message: Message):
        await message.answer(f"Понял, в Champions League сегодня есть такие матчи: \n {matchestoday(league)}")

#Europa League
def uel():
    league = "https://www.readfootball.com/football-europe/tournaments/liga-evropy/calendar.html"
    @dp.message_handler(lambda message: message.text.lower() == "europa league")
    async def uel(message: Message):
        await message.answer(f"Понял, в Europa League сегодня есть такие матчи: \n {matchestoday(league)}")

#Conference League
#def uecl():
#    @dp.message_handler(lambda message: message.text.lower() == "conference league")
#    async def uecl(message: Message):
#        await message.answer(f"Понял, в Conference League сегодня есть такие матчи: \n {matchestoday(league)}")

#FA Cup
def facup():
    league = "https://www.readfootball.com/football-england/tournaments/kubok-fa.html"
    @dp.message_handler(lambda message: message.text.lower() == "fa cup")
    async def facup(message: Message):
        await message.answer(f"Понял, в FA Cup сегодня есть такие матчи: \n {kubki(league)}")

#Carabao Cup
def carabaocup():
    league = "https://www.readfootball.com/football-england/tournaments/kubok.html"
    @dp.message_handler(lambda message: message.text.lower() == "carabao cup")
    async def carabaocup(message: Message):
        await message.answer(f"Понял, в Carabao cup сегодня есть такие матчи: \n {kubki(league)}")

#DFB-Pokal
def dfb_pokal():
    league = "https://www.readfootball.com/football-germany/tournaments/kubok.html"
    @dp.message_handler(lambda message: message.text.lower() == "dfb-pokal")
    async def dfb_pokal(message: Message):
        await message.answer(f"Понял, в DFB-Pokal сегодня есть такие матчи: \n {kubki(league)}")

#Coupe De France
def coupedefrance():
    league = "https://www.readfootball.com/football-france/tournaments/kubok-ligi.html"
    @dp.message_handler(lambda message: message.text.lower() == "coupe de france")
    async def coupedefrance(message: Message):
        await message.answer(f"Понял, в Coupe De France сегодня есть такие матчи: \n {kubki(league)}")

#Copa Del Rey
def copadelrey():
    league = "https://www.readfootball.com/football-spain/tournaments/kubok.html"
    @dp.message_handler(lambda message: message.text.lower() == "copa del rey")
    async def copadelrey(message: Message):
        await message.answer(f"Понял, в Copa Del Rey сегодня есть такие матчи: \n {kubki(league)}")

#Coppa Italia
def coppaitalia():
    league = "https://www.readfootball.com/football-italy/tournaments/kubok.html"
    @dp.message_handler(lambda message: message.text.lower() == "coppa italia")
    async def coppaitalia(message: Message):
        await message.answer(f"Понял, в Coppa Italia сегодня есть такие матчи: \n {kubki(league)}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
