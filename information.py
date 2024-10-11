import datetime
from bs4 import BeautifulSoup
import requests

#Текущая дата
def monthh():
    current_month = ""
    crm = str(datetime.date.today())
    crm = str(crm[5:7])
    if crm == "01":
        current_month = "Янв"
    elif crm == "02":
        current_month = "Фев"
    elif crm == "03":
        current_month = "Мар"
    elif crm == "04":
        current_month = "Апр"
    elif crm == "05":
        current_month = "мая"
    elif crm == "06":
        current_month = "Июн"
    elif crm == "07":
        current_month = "Июл"
    elif crm == "08":
        current_month = "Авг"
    elif crm == "09":
        current_month = "Сен"
    elif crm == "10":
        current_month = "Окт"
    elif crm == "11":
        current_month = "Ноя"
    elif crm == "12":
        current_month = "Дек"
    return current_month

def day_of_the_week():
    current_date = datetime.datetime.now()
    weekday_number = current_date.weekday()
    week_day = ""
    if weekday_number == 0:
        week_day = "пн"
    if weekday_number == 1:
        week_day = "вт"
    if weekday_number == 2:
        week_day = "ср"
    if weekday_number == 3:
        week_day = "чт"
    if weekday_number == 4:
        week_day = "пт"
    if weekday_number == 5:
        week_day = "сб"
    if weekday_number == 6:
        week_day = "вс"
    return week_day


def data():
    current_date = str(datetime.date.today())
    year = current_date[:4]
    month = monthh()
    dayweek = day_of_the_week()
    day = current_date[8:]
    datet = f"{day} {month} {year}, {dayweek}"
    return datet

def datasa():
    current_date = str(datetime.datetime.now())
    print(current_date)
    return current_date[8:10] + "." + current_date[5:7] + "." + current_date[2:4]
matchdates2 = datasa()
matchdates1 = data()
#Матчи в текущий день
def matchestoday(league):
    global matchdates1
    global matches
    url = league
    page = requests.get(url)
    target_date = matchdates1
    soup = BeautifulSoup(page.text, "html.parser")


    match_date = soup.find_all('span', class_='match_date')
    matches_dates = []
    for name in match_date:
        a = name.text
        a = a.replace("\n", "")
        a = a[14:29]
        matches_dates.append(a) #matches dates
    match_time = soup.find_all('span', class_='match_time')
    matchtime = []
    for name in match_time:
        a = name.text
        matchtime.append(a) #matches times


    team_1 = soup.find_all('span', class_='match_team1')
    match_team1 = []
    for name in team_1:
        a = name.text
        match_team1.append(a) #matches team 1


    team_2 = soup.find_all('span', class_='match_team2')
    match_team2 = []
    for name in team_2:
        a = name.text
        match_team2.append(a) #matches team 2

    result = {}
    for i in range(len(matchtime)-10):
        if str(matches_dates[i]) in result:
            result[str(matches_dates[i])] += f" {str(match_team1[i])}  против {str(match_team2[i])} в {str(matchtime[i])} \n"
        else:
            result[str(matches_dates[i])] = f" {str(match_team1[i])}  против {str(match_team2[i])} в {str(matchtime[i])} \n"

    result_matches = ""
    for i in result:
        #if i == target_date:
        if i == target_date:
            result_matches += result[i]
    return result_matches

def kubki(url):
    global matchdates2
    global matchdates1
    target_date1 = matchdates1
    target_date2 = matchdates2
    response = requests.get(url)
    response.raise_for_status()  # Проверка на ошибки

    soup = BeautifulSoup(response.text, 'html.parser')
    matches = soup.find_all('div', class_='item_line')

    # Обработка информации о матчах
    keyy = []
    timee = []
    teamm1 = []
    teamm2 = []
    for match in matches:
        date = match.find('span', class_='match_date')
        date = date.text
        keyy.append(date)
        time = match.find('span', class_='match_time')
        time = time.text
        timee.append((time))
        team1 = match.find('span', class_='match_team1')
        team1 = team1.text
        teamm1.append(team1)
        team2 = match.find('span', class_='match_team2')
        team2 = team2.text
        teamm2.append(team2)
    result = {}
    for i in range(len(teamm2)): #делаем result всех дат и игр
        if str(keyy[i]) in result:
            result[str(keyy[i])] += f" {str(teamm1[i])}  против {str(teamm2[i])} в {str(timee[i])} \n"
        else:
            result[str(keyy[i])] = f" {str(teamm1[i])}  против {str(teamm2[i])} в {str(timee[i])} \n"
    def normalize_string(s):
        return ' '.join(s.split())
    result_new = {}
    seen_values = set()
    for key, value in result.items():
        normalized_value = normalize_string(value)
        # Если значение еще не встречалось
        if normalized_value not in seen_values:
            result_new[key] = value
            seen_values.add(normalized_value)

    target_dates = []
    target_dates.append(target_date1)
    target_dates.append(target_date2)

    def normalize(date_str):
        return date_str.strip().replace('.', ' ').replace(',', '')  # Заменяем точки и запятые на пробелы

    result_ma = []
    gale = []
    for key, value in result_new.items():
        if normalize(key) in map(normalize, target_dates):
            result_ma.append(value)
    for i in result_ma:
        s = i.find("\n")
        if s != -1:  # Если символ найден
            slice_s = str(i[:s])
            gale.append(slice_s)

    chester = ""
    for i in gale:
        chester += i + "\n"
    return chester