# telegrambot

## 1. Создай новый проект в PyCharm.
  * Создание проекта

![image](https://user-images.githubusercontent.com/94354182/170044810-19372470-fa2f-40ab-bba4-195c815ed3e8.png)
  
  * выбери следующие настройки:
  
 ![image](https://user-images.githubusercontent.com/94354182/170045921-15df3217-332c-4eb1-99cc-3b61c9397bc8.png)

  * ждем, пока создастся venv
## 2. Настраиваем связь 

![image](https://user-images.githubusercontent.com/94354182/170051403-0956950c-cef6-498f-a85a-ed34a54751a3.png)

![image](https://user-images.githubusercontent.com/94354182/170051525-631a52a1-2c5c-4ce8-9f0d-bdee7bc0e7d1.png)

* Вставляешь наш репозиторий

```
https://github.com/ka1qw/telegrambot.git
```

![image](https://user-images.githubusercontent.com/94354182/170051620-1589f50d-3434-42e7-ad38-5671c3c4b56d.png)

* делаешь fetch (не совсем понимаю что это, вроде бы подтягиваешь структуру удаленного репозитория)

![image](https://user-images.githubusercontent.com/94354182/170051750-9a169276-fd74-48a2-b1b8-51db82cddadc.png)

* делаешь pull (подтягиваешь все файлы с удаленного репозитория)

![image](https://user-images.githubusercontent.com/94354182/170051789-8e932ea9-bd41-4420-9e19-086533da7b45.png)

* тут выбираешь, на какую ветку пуллить.

_Дальше будем еще работать с ветками, очень удобная тема_

![image](https://user-images.githubusercontent.com/94354182/170051827-d9b609c5-4cb0-4a0d-a905-a6d9bd5bfb2e.png)

## 3. Доработочки

 * Заходишь в любой .py файл проекта, сверху должно будет появиться следующее:
 
 ![image](https://user-images.githubusercontent.com/94354182/170052135-537db2c8-001d-4ed9-b8f8-2a009f62fb86.png)

 * ждешь пока установятся пакеты
 
 ![image](https://user-images.githubusercontent.com/94354182/170052200-7c3edf7e-ab5e-466d-92d0-a4be9e209c9c.png)

 * создаешь файл .gitignore в корне проекта
 
 ![image](https://user-images.githubusercontent.com/94354182/170052476-c6cff5a6-df70-4780-bcae-efa112114806.png)
 
 __ВАЖНО__
 Нажимаешь отмену в следующем окне
 
 ![image](https://user-images.githubusercontent.com/94354182/170052962-e5489987-d0b2-4a13-96f6-5899c1909c0f.png)

 * ручками или через IDE копируешь батник из старого проекта в корень нового
 
 ![image](https://user-images.githubusercontent.com/94354182/170052774-91948245-f069-42bb-afc4-7c62268892ea.png)
 
 * прописываешь в .gitignore след строки
  ```
  /venv/
  /.idea/
  bot_run.bat
  ```
 
 ![image](https://user-images.githubusercontent.com/94354182/170053177-a2f6a836-0b90-4bec-899d-a17065b6f017.png)

## 4. Радуешься жизни (но не долго, все таки в России живем)

Дальше нужно будет разобраться, как делать коммиты, пуши и пуллы. Тут объяснено очень подробно и понятно:
***
[тык №1](https://www.youtube.com/watch?v=9VKKZNqzPcE&list=PLrzHY9riBq3bu8xnTqukuj_6JpWD8LFB5&index=4&ab_channel=PythonRussian)

[тык №2](https://www.youtube.com/watch?v=hqDWXBlQG5c&ab_channel=PythonRussian)
***
Работаем мы каждый со своим разделом, именно поэтому я их составляющие разнес на разные файлы.
Если мы одновременно будем менять какой-то файл, а потом попытаемся его запушить, то произойдет конфликт, который потом запаримся решать.

__ПОЭТОМУ СОВЕТУЮ ПОСМОТРЕТЬ ВИДОСЫ, ХОТЬ И ЗНАЮ, ЧТО ТЫ ЭТО ДЕЛАТЬ НЕ ЛЮБИШЬ__

    «Нет ничего невозможного. Само слово говорит: „Я возможно!“ (Impossible — I'm possible)», — Одри Хепбёрн.
    
_Взято с [сайта мотивирующих цитат](https://ru.ihodl.com/lifestyle/2016-09-09/50-luchshih-motiviruyushih-citat-na-kazhdyj-sluchaj-zhizni/)._
