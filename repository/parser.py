import requests
from bs4 import BeautifulSoup


def pars_all():
    url = "https://www.rshu.ru/university/stud/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    hrefs_autumn = {}
    hrefs_spring = {}
    for link in soup.find_all('a'):
        key_shot = str(link)[str(link).find('>') + 1:str(link).find('</a>')]
        if link.get('href').find("second") != -1:
            hrefs_spring[key_shot] = link.get('href')
        if link.get('href').find("first") != -1:
            hrefs_autumn[key_shot] = link.get('href')

    return hrefs_spring, hrefs_autumn


def change_faculty_name(name):
    if name == "ИИСиГТ":
        name = "Институт Информационных систем и геотехнологий"
    elif name == "ИГиО":
        name = "Институт гидрологии и океанологии"
    elif name == "ФМиПП":
        name = "Факультет морского и полярного права"
    elif name == "Полярная академия":
        name = "Институт Полярная академия"
    elif name == "Факультет ГМO":
        name = "Факультет ГМО"
    return name
