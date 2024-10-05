# Sprint_7 - финальный проект 7 спринта
Тестирование API учебного сервиса Яндекс Самокат: qa-scooter.praktikum-services.ru/docs/
Тестирование проводится с целью определения корректности работы сервиса и выявления ошибок при его функционировании. 

Покрытие:
Проводится тестирование на создание курьера: 
- курьера можно создать;
- нельзя создать двух одинаковых курьеров;
- чтобы создать курьера, нужно передать в ручку все обязательные поля;
- запрос возвращает правильный код ответа;
- успешный запрос возвращает {"ok":true};
- если одного из полей нет, запрос возвращает ошибку;
- если создать пользователя с логином, который уже есть, возвращается ошибка.

Тесты на авторизацию курьера:
- курьер может авторизоваться;
- для авторизации нужно передать все обязательные поля;
- система вернёт ошибку, если неправильно указать логин или пароль;
- если какого-то поля нет, запрос возвращает ошибку;
- если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
- успешный запрос возвращает id.
  
Тесты на создание заказа: 
- можно указать один из цветов — BLACK или GREY;
- можно указать оба цвета;
- можно совсем не указывать цвет;
- тело ответа содержит track.

Тесты на проверку списка заказов: 
- тело ответа содержит список заказов.
  
Структура репозитория:
- директория tests содержит файл с тестами;
- файл data содержит тестовые данные, необходимые для тестирования;
- файл helpers содержит функции, для генерирования рандомных данных с помощью библиотеки Faker;
- файле urls содержит ручки для тестирования;
- директория allure_results содержит отчет с результататами тестирования;
- файле requirements.txt содержит информация о зависимостях;
- файл README содержит информацию о текущем проекте и тестах
