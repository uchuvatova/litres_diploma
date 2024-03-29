# Автоматизация тестирования API и веб-сайта cервиса электронных книг Литрес
> <a target="_blank" href="https://www.litres.ru/">litres.ru</a>

![main page screenshot](resources/base_page_web.jpg)

----

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Запуск web/UI автотестов в Selenoid

### Список проверок, реализованных в web/UI-автотестах

- [x] Успешная регистрация пользователя
- [x] Неуспешная регистрация пользователя без ввода пароля
- [x] Неуспешная регистрация пользователя с несовпадающими паролями
- [x] Успешный логин зарегистированного пользователя
- [x] Неуспешный логин зарегистрированного пользователя с неправильным паролем
- [x] Неуспешный логин зарегистрированного пользователя без ввода пароля
- [x] Неуспешная регистрация пользователя с слишком длинным паролем

### Список проверок, реализованных в API-автотестах

- [x] Успешная регистрация пользователя по email
- [x] Неуспешная регистрация пользователя с существующим email
- [x] Неуспешная регистрация пользователя по email с невалидным паролем
- [x] Просмотр пустой корзины неавторизованного пользователя
- [x] Добавление книги в Отложенные неавторизованным пользователем
- [x] Удаление книги из Отложенных неавторизованным пользователем

----

### Проект реализован с использованием:

<img src="resources/icons/python-original.svg" width="50" title="Python"> <img src="resources/icons/pytest.png" width="50" title="Pytest"> <img src="resources/icons/intellij_pycharm.png" width="50" title="PyCharm"> <img src="resources/icons/selene.png" width="50" title="Selene"> <img src="resources/icons/selenium.png" width="50" title="Selenium"> <img src="resources/icons/selenoid.png" width="50" title="Selenoid"> <img src="resources/icons/jenkins.png" width="50" title="Jenkins"> <img src="resources/icons/allure_report.png" width="50" title="Allure Report"> <img src="resources/icons/allure_testops.png" width="50" title="Allure TestOps"> <img src="resources/icons/tg.png" width="50" title="Telegram"> <img src="resources/icons/jira.png" width="50" title="Jira">

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C08-irauchuvatova-litres-diploma/">Ссылка на проект в Jenkins</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
BROWSER = ['CHROME', 'MOZILLA']
COMMENT = 'some comment'
```
#### Запуск автотестов в Jenkins
![jenkins project main page](./resources/jenkins_project_main_page.png)
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C08-irauchuvatova-litres-diploma/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке BROWSER 
4. Указать комментарий в поле COMMENT 
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

----
### Allure-отчет


#### Общие результаты
![This is an image](resources/allure_report_overview.png)
#### Список тест-кейсов
![This is an image](resources/allure_test_cases.png)
#### Пример отчета о прохождении теста

<img alt="This is an image" height="300" src="resources/example_test_allure.png"/>

----
### Allure TestOps

#### Общий список всех кейсов, имеющихся в системе
![This is an image](resources/allure_TestOps_test_cases.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](resources/allure_TestOps_dashboard.png)

----
### Интеграция с Jira
![This is an image](resources/jira_issue.png)

----
### Оповещение о результатах прохождения тестов в Telegram

<img alt="This is an image" height="250" src="resources/tg_notification.png"/>

----
### Пример видео прохождения автотеста
Тест-кейс "Регистрация без ввода пароля"

![Регистрация без ввода пароля](resources/video_test.gif)