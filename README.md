# Автоматизация тестирования веб-сайта и API "Сервис электронных книг Литрес"
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

- [x] Главная страница сайта отображается
- [x] Страница фильма отображается
- [x] Промо страница отображается
- [x] Найти фильм в поиске возможно
- [x] Раздел "Что нового" отображается
- [x] Открыть страницу "Фильмы" через верхнее меню возможно
- [x] Открыть страницу "Сериалы" через верхнее меню возможно
- [x] Открыть страницу "Мультфильмы" через верхнее меню возможно

### Список проверок, реализованных в API-автотестах

- [x] Элементы управления отображаются
- [x] Раздел "Сериалы" отображается
- [x] Раздел "Профиль" отображается

----

### Проект реализован с использованием:

<img src="resources/icons/python-original.svg" width="50" title="Python"> <img src="resources/icons/pytest.png" width="50" title="Pytest"> <img src="resources/icons/intellij_pycharm.png" width="50" title="PyCharm"> <img src="resources/icons/selene.png" width="50" title="Selene"> <img src="resources/icons/selenium.png" width="50" title="Selenium"> <img src="resources/icons/selenoid.png" width="50" title="Selenoid"> <img src="resources/icons/jenkins.png" width="50" title="Jenkins"> <img src="resources/icons/allure_report.png" width="50" title="Allure Report"> <img src="resources/icons/allure_testops.png" width="50" title="Allure TestOps"> <img src="resources/icons/tg.png" width="50" title="Telegram"> <img src="resources/icons/jira.png" width="50" title="Jira">

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C08-irauchuvatova-litres-diploma/">Ссылка</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
ENVIRONMENT = ['STAGE', 'PROD']
COMMENT = 'some comment'
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C08-irauchuvatova-litres-diploma/">проект</a>

![jenkins project main page](./resources/jenkins_project_main_page.png)

2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать окружение
4. В поле "COMMENT" ввести комментарий
5. Нажать "Build"

![jenkins_build](ivi_ui_and_mobile_test_framework/pictures/jenkins_build.png)

----

### Allure отчет
#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/">Общие результаты</a>
![allure_report_overview](ivi_ui_and_mobile_test_framework/pictures/allure_report_overview.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#suites">Результаты прохождения теста</a>

![allure_reports_behaviors](ivi_ui_and_mobile_test_framework/pictures/allure_reports_suites.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#graph">Графики</a>


![allure_reports_graphs](ivi_ui_and_mobile_test_framework/pictures/alluere_reports_graphs_1.png)
![allure_reports_graphs](ivi_ui_and_mobile_test_framework/pictures/alluere_reports_graphs_2.png)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3910/dashboards">Ссылка на проект</a>

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/dashboards">Дашборд с общими показателями тестовых прогонов</a>

![allure_test_ops_dashboards](ivi_ui_and_mobile_test_framework/pictures/allure_testops_dashboards.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/launches">История запуска тестовых наборов</a>

![allure_testops_launches](ivi_ui_and_mobile_test_framework/pictures/allure_testops_launches.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Тест кейсы</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_suites.png)

#### <a target="_blank" href="https://allure.autotests.cloud/launch/33573/tree/551292/attachments?treeId=0">Тестовые артефакты</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_test_attachments.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Ручной запуск авто теста из Allure TestOps</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_manual_test_run.png)

1. Нажать на чек-бокс необходимого тест кейса
2. Нажать на "Bulk actions"
3. Нажать на "Run"

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1021">Ссылка на проект</a>

![jira_project](ivi_ui_and_mobile_test_framework/pictures/jira_project.png)

----

### Оповещения в Telegram
![telegram_allert](ivi_ui_and_mobile_test_framework/pictures/telegram_allert.png)

----

### Видео прохождения web/UI автотеста
![autotest_gif](ivi_ui_and_mobile_test_framework/pictures/autotest.gif)
