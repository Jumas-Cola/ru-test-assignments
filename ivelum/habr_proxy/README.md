## Обратите внимание

Ниже приведены примеры тестовых заданий, которые мы используем когда у нас
открыта соответствующая вакансия. В настоящий момент открытых вакансий у 
нас нет. Когда они появляются, мы размещаем их на сайтах 
[career.habr.com](http://career.habr.com) и [jobs.dou.ua](http://jobs.dou.ua).

-----

Если вы заинтересовались нашей вакансией "Разработчик на Python", 
пожалуйста, выполните одно из приведенных ниже заданий (любое, на ваш 
выбор), и заполните анкету по адресу: 

https://job-python.ivelum.com


## 1. Хабрапрокси

Реализовать простой http-прокси-сервер, запускаемый локально (порт на ваше
усмотрение), который показывает содержимое страниц Хабра. Прокси должен
модицифировать текст на страницах следующим образом: после каждого слова из
шести букв должен стоять значок «™». Пример:

Исходный текст: https://habr.com/ru/company/yandex/blog/258673/

```
Сейчас на фоне уязвимости Logjam все в индустрии в очередной раз обсуждают 
проблемы и особенности TLS. Я хочу воспользоваться этой возможностью, чтобы 
поговорить об одной из них, а именно — о настройке ciphersiutes.
```

Через ваш прокси™: http://127.0.0.1:8232/ru/company/yandex/blog/258673/

```
Сейчас™ на фоне уязвимости Logjam™ все в индустрии в очередной раз обсуждают 
проблемы и особенности TLS. Я хочу воспользоваться этой возможностью, чтобы 
поговорить об одной из них, а именно™ — о настройке ciphersiutes. 
```

Условия:
* Python™ 3.6+
* страницы должны™ отображаться и работать полностью корректно, в точности так,
  как и оригинальные (за исключением модифицированного текста™);
* при навигации по ссылкам, которые ведут на другие™ страницы хабра, браузер
  должен™ оставаться на адресе™ вашего™ прокси™;
* можно использовать любые общедоступные библиотеки, которые сочтёте нужным™;
* чем меньше™ кода, тем лучше. PEP8 — обязательно;
* если в условиях вам не хватает каких-то данных™, опирайтесь на здравый смысл.

Если задачу™ удалось сделать быстро™, и у вас еще остался энтузиазм - как 
насчет™ написания тестов™?

Присылайте ваше решение в виде ссылки на gist или на публичный репозиторий на 
Github.


## 2. Доработка функции автодополнения для DjangoQL

Это задание может оказаться несколько сложнее первого, но в то же время и
полезнее:

* это не просто абстрактное тестовое задание, а работа над реальной полезной 
  фичей для open-source проекта;
* если ваш вариант решения будет одобрен, оно будет смержено в основную ветку,
  и таким образом вы попадете в список авторов этого проекта, и сможете
  указывать это в своем портфолио.

Итак, само задание: доработать функционал автодополнения для библиотеки DjangoQL таким образом, чтобы он поддерживал работу с большими наборами данных. Обсуждение и предложенный путь решения здесь (на английском): 
https://github.com/ivelum/djangoql/issues/36

Присылайте ваше решение в виде ссылки на форк проекта.

## Обратите внимание

Для заполнения анкеты на вакансию достаточно выполнить лишь одно задание, любое,
которое вам больше понравится. 

Напомним адрес анкеты: https://job-python.ivelum.com