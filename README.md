# telegrambot

## 1. Создаем новый проект в PyCharm.
  * Создание проекта

![image](https://user-images.githubusercontent.com/94354182/170044810-19372470-fa2f-40ab-bba4-195c815ed3e8.png)
  
  * выберите следующие настройки:
  
 ![image](https://user-images.githubusercontent.com/94354182/170045921-15df3217-332c-4eb1-99cc-3b61c9397bc8.png)

  * ждем, пока создастся venv
## 2. Настраиваем связь 

![image](https://user-images.githubusercontent.com/94354182/170051403-0956950c-cef6-498f-a85a-ed34a54751a3.png)

![image](https://user-images.githubusercontent.com/94354182/170051525-631a52a1-2c5c-4ce8-9f0d-bdee7bc0e7d1.png)

* Вставляем наш репозиторий

```
https://github.com/ka1qw/telegrambot.git
```

![image](https://user-images.githubusercontent.com/94354182/170051620-1589f50d-3434-42e7-ad38-5671c3c4b56d.png)

* делаем fetch

![image](https://user-images.githubusercontent.com/94354182/170051750-9a169276-fd74-48a2-b1b8-51db82cddadc.png)

* делаем pull (подтягиваем все файлы с удаленного репозитория)

![image](https://user-images.githubusercontent.com/94354182/170051789-8e932ea9-bd41-4420-9e19-086533da7b45.png)

* тут выбираем, на какую ветку пуллить.


![image](https://user-images.githubusercontent.com/94354182/170051827-d9b609c5-4cb0-4a0d-a905-a6d9bd5bfb2e.png)

## 3. Доработочки

 * Заходим в любой .py файл проекта, сверху должно будет появиться следующее:
 
 ![image](https://user-images.githubusercontent.com/94354182/170052135-537db2c8-001d-4ed9-b8f8-2a009f62fb86.png)

 * ждем пока установятся пакеты
 
 ![image](https://user-images.githubusercontent.com/94354182/170052200-7c3edf7e-ab5e-466d-92d0-a4be9e209c9c.png)

 * создаем файл .gitignore в корне проекта
 
 ![image](https://user-images.githubusercontent.com/94354182/170052476-c6cff5a6-df70-4780-bcae-efa112114806.png)
 
 __ВАЖНО__
 Нажимаем отмену в следующем окне
 
 ![image](https://user-images.githubusercontent.com/94354182/170052962-e5489987-d0b2-4a13-96f6-5899c1909c0f.png)

 * ручками или через IDE копируем батник из старого проекта в корень нового
 ***
__Для новых юзеров:__

__О содержании .bat файла написано в 5-м пункте__
***
 ![image](https://user-images.githubusercontent.com/94354182/170052774-91948245-f069-42bb-afc4-7c62268892ea.png)
 
 * прописываем в .gitignore след строки
  ```
  /venv/
  /.idea/
  bot_run.bat
  ```
 
 ![image](https://user-images.githubusercontent.com/94354182/170053177-a2f6a836-0b90-4bec-899d-a17065b6f017.png)

## 4. Радуемся жизни



    «Нет ничего невозможного. Само слово говорит: „Я возможно!“ (Impossible — I'm possible)», — Одри Хепбёрн.
    
_Взято с [сайта мотивирующих цитат](https://ru.ihodl.com/lifestyle/2016-09-09/50-luchshih-motiviruyushih-citat-na-kazhdyj-sluchaj-zhizni/)._

## 5. Создание .bat файла и работа с ним

В корне проекта нужно создать .bat файл, при запуске которого будет запускаться бот.

В поле __TOKEN=__ нужно вставить токен твоего телеграм-бота.
```
@echo off

call %~dp0\venv\Scripts\activate

set TOKEN=ТВОЙ_ТОКЕН

python bot_telegram.py

pause
```
