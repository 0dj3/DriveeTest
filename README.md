# DriveeTest
Тестовое задание для Drivee

Работа полностью описана в файле ```Drivee.ipynb```. Данный файл можно открыть в Colabotory ```https://colab.research.google.com/```:

- Открыть сайт,
- Пройти по пути: Файл -> Загрузить блокнот -> Загрузить -> Выбрать файл ```Drivee.ipynb```
- После открытия блокнота нажать на кнопки: Среда выполнения -> Выполнить всё
- Код запустится

По отрисовке объектов:
- Разноцветные круги - начальные точки заказов
- Разноцветные звезды - конечные точки заказов (рядом указан id)
- Темные треугольники - курьеры (рядом указан id)

Принцип работы:

Задаётся n-ое количество заказов и k-ое количество курьеров. С условием, что ```n >= k``` и ```n mod k == 0```.

Описание работы кода:
1. Курьеры находят ближайшие к ним заказы со статусами "Waiting"
2. Курьеры перемещаются на начальную точку заказа и заказ получает статус "In Progress"
3. Курьеры доходят до конечной точки заказа и заказ получает статус "Delivered"

Эти шаги повторяются до тех пор, пока все заказы не будут доставлены.
