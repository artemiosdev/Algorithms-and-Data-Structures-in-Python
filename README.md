## [2017-2018 Алгоритмы и структуры данных на Python 3, all playlist](https://www.youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0)

- [Youtube channel Тимофей Хирьянов](https://www.youtube.com/c/ТимофейХирьянов)

- Материалы курса находятся на [сайте](http://judge.mipt.ru/mipt_cs_on_python3/)

- https://www.python.org/

- https://pythonworld.ru/

### Лекция №1. Введение, базовый синтаксис Python. Концепция присваивания. Арифметические операции. Цикл while and for. range(). continue and break. 
Программирование включает, по степени  важности:

1. Алгоритмы и структуры данных
2. Практика программирования
3. Дизайн ПО (архитектура приложения)
4. Синтаксис языка программирования
5. Прикладные библиотеки
6. Групповая разработка, коммуникация

"Код читается намного больше раз, чем пишется" @Гвидо ван Россум

My version:
```bash
flyboroda@MacBook-Air-Artem ~ % python3
Python 3.8.9 (default, Feb 18 2022, 07:45:33) 
[Clang 13.1.6 (clang-1316.0.21.2)] on darwin
```

```python
x = "Hello, World"
print(x)
print(type(x)) # узнаем какой тип у имени х
x = 1 + 2 + 3
```
Переменных нет, есть имена, `х` это имя, ссылающееся на строковое значение в памяти "Hello, World". Х это именнованная ссылка на значение "Hello, World". Оператор присваивания `=` в Python это ссылка. Есть сборщик мусора который сразу же убирает не именованные или безхозные объекты из памяти. В Питоне х не привязан к конкретной области памяти. Далее х привязывается к новому числовому значению равному 6, и теряет связь с  "Hello, World". 

Питон не архитектурно ориентирован, он более приближен к математической модели.

hypot.py
```python
a = 179
b = 197
c = (a ** 2 + b ** 2) ** 0.5
print (c)
```

Здесь мы используем переменные — объекты, в которых можно сохранять различные (числовые, строковые и прочие) значения. В первой строке переменной a присваивается значение 179, затем переменной `b` присваивается значение 97, затем переменной `c` присваивается значение арифметического выражения, равного длине гипотенузы. После этого значение переменной c выводится на экран.

```bash
flyboroda@MacBook-Air-Artem examples % touch hypot.py
flyboroda@MacBook-Air-Artem examples % open hypot.py
flyboroda@MacBook-Air-Artem examples % python3 hypot.py
266.1766330841233
```

***Типы данных***

Числа записываются последовательностью цифр, также перед числом может стоять знак минус, а строки записываются в одинарных кавычках. 2 и '2' — это разные объекты, первый объект — число, а второй — строка. Операция + для целых чисел и для строк работает по-разному: для чисел это сложение, а для строк — конкатенация.

Кроме целых чисел есть и другой класс чисел: действительные (вещественные числа), представляемые в виде десятичных дробей. Они записываются с использованием десятичной точки, например, 2.0.

Определить тип объекта можно при помощи функции type:

```python
>>> type(2)
<class 'int'>
>>> type('2')
<class 'str'>
>>> type(2.0)
<class 'float'>
```

Обратите внимание — `type` является функцией, аргументы функции указываются в скобках после ее имени.


***Операции с числами***

Вот список основных операций для чисел:

`A + B` — сумма;

`A - B` — разность;

`A * B` — произведение;

`A / B` — частное;

`A ** B` — возведение в степень, двойное умножение, работает не только с целыми числами

Полезно помнить, что квадратный корень из числа `x` — это `x ** 0.5`, а корень степени `n` — это `x ** (1 / n)`.
Например корень из 3 это `3**0.5`

Есть также унарный вариант операции ` - `, то есть операция с одним аргументом. Она возвращает число, противоположное данному. Например: -A.

В выражении может встречаться много операций подряд. Как в этом случае определяется порядок действий? Например, чему будет равно `1+2*3**1+1`? В данном случае ответ будет 8, так как сначала выполняется возведение в степень, затем — умножение, затем — сложение.

```python
a += 1
a = a + 1

a -= 1
a = a - 1

a /= 1
a = a / 1

a // = 1 # с отбрасыванием остатка
a = a // 1

a %= 1 # интересует остаток, по модулю
a = a % 1

a *= 1
a = a * 1
```


Правила определения приоритетов операций такие:

1. Выполняются возведения в степень справа налево, то есть `3**3**3` это 3²⁷ (7625597484987).

2. Выполняются унарные минусы (отрицания) `-x`.

3. Выполняются умножения и деления слева направо. Операции умножения и деления имеют одинаковый приоритет.

```python
# деление с отбрасыванием остатка
x = 16
y = 3
z = x // y
print(z)  # будет 5 и остаток 1 отбрасываем

# если интересует остаток, то
x = 16
y = 3
z = x % y
print(z) # 1
```

```python
x = -12
y = 5
z = x // y
s = x % y
print(z) # - 3
print(s) # 3
```

```python
x = -11
y = 10
z = x // y
s = x % y
print(z) # -2
print(s) # 9
```

4. Выполняются сложения и вычитания слева направо. Операции сложения и вычитания имеют одинаковый приоритет.


***Операции над строками***

`A + B` — ***конкатенация***;

`A * n` — повторение n раз, значение n должно быть целого типа.

***Каскадное (трамвайное) присваивание***

```python
x = y = z = 0
```

***Множественное присваивание (кортеж)***

```python
x, y, z = 1, 2, 3
```

***Обмен значений двух переменных через третью***.
```python
a = 1
b = 2

tmp = a
a = b
b = tmp
```

***Обмен значений двух переменных через две дополнительных***.
```python
a = 1
b = 2

tmp1 = b
tmp2 = a
a = tmp1
b = tmp2
```

Можно применить множественное присвание (ниже), и сократить код. Это ***обмен через временный кортеж с 2 дополнительными переменными*** (кортеж это множественное присваивание x, y = 1, 2, кортеж - пачка имен и присваиваемых значений). Как только выражение вычислится, кортеж исчезнет. Кортеж представляет из себя ссылки на числовые объекты, сами объекты не копируются.

```python
a = 1
b = 2

tmp1, tmp2 = b, a
a, b = tmt1, tmp2

# или еще лучше
a, b = b, a
```

В этом примере ниже происходит ***Пересвязывание***, сам объект мы не можем изменить, можем лишь изменить то на что ссылается имя. Сам объект когда он существует, он таким и остается всегда, не меняется. Значение объекта изменить нельзя. Сам объект таким и остается каким он создан, до момента вытирания его сборщиком мусора.
```python
x = 1
x = 2
```

***Ветвление***

Ветвление (или условная инструкция) в Python имеет следующий синтаксис:

```python
if Условие:
    Блок_инструкций_1
else:
    Блок_инструкций_2
```

Блок_инструкций_1 будет выполнен, если Условие истинно. Если Условие ложно, будет выполнен Блок_инструкций_2.

В условной инструкции может отсутствовать слово else и последующий блок. Такая инструкция называется неполным ветвлением. Например, если дано число x и мы хотим заменить его на абсолютную величину x, то это можно сделать следующим образом:

```python
if x < 0:
    x = -x
print(x)
```

В этом примере переменной x будет присвоено значение -x, но только в том случае, когда x<0. А вот инструкция print(x) будет выполнена всегда, независимо от проверяемого условия.

Для выделения блока инструкций, относящихся к инструкции if или else в языке Python используются отступы. Все инструкции, которые относятся к одному блоку, должны иметь равную величину отступа, то есть одинаковое число пробелов в начале строки. Рекомендуется использовать отступ в 4 пробела.

***Вложенные условные инструкции***

Внутри условных инструкций можно использовать любые инструкции языка Python, в том числе и условную инструкцию. ***Вложенное ветвление*** — после одной развилки в ходе исполнения программы появляется другая развилка. При этом вложенные блоки имеют больший размер отступа (например, 8 пробелов).

Пример программы, которая по данным ненулевым числам x и y определяет, в какой из четвертей координатной плоскости находится точка (x,y):

`x = int(input())` - считываем введенное значение с клавиатуры, оно будет строковым, прообразуем в число, и присваиваем его значение имени х

```python
x = int(input())
y = int(input())
if x > 0:
    if y > 0:               # x>0, y>0
        print("Первая четверть")
    else:                   # x>0, y<0
        print("Четвертая четверть")
else:
    if y > 0:               # x<0, y>0
        print("Вторая четверть")
    else:                   # x<0, y<0
        print("Третья четверть")
```

***Комментариями*** в Pythonе является символ ` # `.

***Операторы сравнения***

Как правило, в качестве проверяемого условия используется результат вычисления одного из следующих операторов сравнения:

```python
<	   Меньше — условие верно, если первый операнд меньше второго.
>	   Больше — условие верно, если первый операнд больше второго.
<=	 Меньше или равно — условие верно, если первый операнд меньше или равен второму.
>=	 Больше или равно — условие верно, если первый операнд больше или равен второму.
==	 Равенство. Условие верно, если два операнда равны.
```

Например, условие (x * x < 1000) означает «значение x * x меньше 1000», а условие (2 * x != y) означает «удвоенное значение переменной x не равно значению переменной y».

Операторы сравнения можно объединять в цепочки, например, `a == b == c` или `1 <= x <= 10`.

***Тип данных bool***

Значения логического типа могут принимать одно из двух значений: True (истина) или False (ложь). Если преобразовать логическое True к типу `int`, то получится 1, а преобразование False даст 0. При обратном преобразовании число 0 преобразуется в False, а любое ненулевое число в True. При преобразовании `str` в `bool` пустая строка преобразовывается в False, а любая непустая строка в True.

***Каскадные условные инструкции***

Пример программы, определяющий четверть координатной плоскости, можно переписать используя «каскадную« последовательность операцией `if... elif... else`:

```python
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Первая четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
    # если x<0, y>0, то
elif y > 0:
    print("Вторая четверть")
    # если x<0, y<0, то
else:
    print("Третья четверть")
```

В такой конструкции условия `if, ..., elif` проверяются по очереди, выполняется блок, соответствующий первому из истинных условий. Если все проверяемые условия ложны, то выполняется блок `else`, если он присутствует.

***Цикл while («пока»)***

Позволяет выполнить одну и ту же последовательность действий, пока проверяемое условие истинно. ***Условие записывается до тела цикла и проверяется до выполнения тела цикла***. Как правило, цикл while используется, когда невозможно определить точное значение количества проходов исполнения цикла.

Синтаксис цикла while в простейшем случае выглядит так:

```python
while Условие:
    Блок_инструкций
```

При выполнении цикла while сначала проверяется условие. Если оно ложно, то выполнение цикла прекращается и управление передается на следующую инструкцию после тела цикла while. Если условие истинно, то выполняется инструкция, после чего условие проверяется снова и снова выполняется инструкция. Так продолжается до тех пор, пока условие будет истинно. Как только условие станет ложно, работа цикла завершится и управление передастся следующей инструкции после цикла.

Например, следующий фрагмент программы напечатает на экран всех целые числа, не превосходящие `n`:

```python
a = 1
while a <= n:
    print(a)
    a += 1
```

Общая схема цикла `while` в данном случае для перебора всех подходящих значений такая:

```python
a = начальное_значение
while а_является_подходящим_числом:
    обработать_a
    перейти_к_следующему_a
```

Выводем все степени двойки, не превосходящие числа n:

```python
a = 1
while a <= n:
    print(a)
    a *= 2
```

***Цикл for*** 

Является синтаксическим сахаром, т.е он удобен и практичен, делает жизнь программиста слаще, но вовсе необязателен.

Нужен чтобы пробегать какой-то диапозон арифметической прогрессии. 

Более краткая альтернатива циклу `while`.

Для последовательного перебора целых чисел из диапазона `[0; n)` можно использовать цикл `for`:

```python
for i in range(10):
   print(i)
```

Этот код по выполняемым действиям полностью соответствуют циклу `while`:

```python
i = 0
while i < 10:
  print(i)
  i += 1
```

***Итерация*** - это однократное выполнение тела цикла.

Можно задавать начальные и конечные значения для переменной цикла, а также шаг (последнее значение):

```python
for i in range(20, 10, -2):
  print(i)
```

Result: 20 18 16 14 12

Универсальный генератор арифметической прогрессии,  ***`range(start, stop, step)`***, значение `stop` не включается, значение на позиции `start` всегда включается, `[start, stop)`

`range(5)` - диапозон, старт будет с 0, шаг 1, до 5
`range(5, 10)` - диапозон от и до
`range(5, 10, 2)` - диапозон от и до, с шагом

```python
for i in range(5):
   print(i)
```
Result: 1, 2, 3, 4, 5

```python
for x in range(5, 0, -1):
  print(x ** 2)
```
Result: 25 16 9 4 1


***Аналогичный цикл while***

```python
i = 20
while i > 10:
  print(i)
  i -= 2
```

***break***

Экстренный выход из цикла, перепрыгивание на следующую инструкцию программы минуя else if и тп, аналогия "пожар". Чаще всего используется с проверкой условия ` if что-то там, то break`. 

***continue***
Телепортация сразу на следующую итерацию. С середины тела цикла, могу снова попасть, телепортироваться на следующую новую итерацию.


***Черепаха***

Стандартная библиотека Python содержит модуль `turtle`, предназначенный для обучения программированию. Этот модуль содержит набор функций, позволяющих управлять черепахой. Черепаха умеет выполнять небольшой набор команд, а именно:

Команда	Значение
```python
forward(X)	# Пройти вперёд X пикселей
backward(X)	# Пройти назад X пикселей
left(X)		# Повернуться налево на X градусов
right(X)	# Повернуться направо на X градусов
penup()		# Не оставлять след при движении
pendown()	# Оставлять след при движении
shape(X)	# Изменить значок черепахи (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
stamp()		# Нарисовать копию черепахи в текущем месте
color()		# Установить цвет
begin_fill()	# Необходимо вызвать перед рисованием фигуры, которую надо закрасить
end_fill()	# Вызвать после окончания рисования фигуры
width()		# Установить толщину линии
goto(x, y)	# Переместить черепашку в точку (x, y)
```

***Практика: Черепаха***

***[IDE repl.it](https://replit.com/)***

***Рисуем букву S***

```python
import turtle

turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
```

***Рисуем круг***

```python
import turtle

# Create a turtle
turtle.speed(10)
turtle.width(10)
turtle.color("red")

# Draw a circle starting at (x, y)
radius = 100
turtle.circle(radius)

# Make it all work properly
turtle.done()
```

***Рисуем вложенные квадраты***, один в другой с уменьшением шага

```python
import turtle
 
a = int(input())  # сторона квадрата
turtle.shape('turtle')
while a > 1:
    turtle.pendown()
    for i in range(4):
        turtle.forward(a * 10)
        turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    a -= 1
input()
```

***Рисуем паука, с заданным количеством лап***

```python
import turtle

a = int(input())  # количество лап паука
turtle.shape('turtle')
for i in range(a):
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(360 / a)
input()
```

***Рисуем спираль***

Нужно подключить модуль `math`

```python
from math import pi, sin, cos
import turtle

turtle.shape('turtle')
for i in range(200):
    t = i / 10 * pi
    dx = t * cos(t)
    dy = t * sin(t)
    turtle.goto(dx, dy)
```

or

```python
import turtle

turtle.shape('turtle')
x = 0.5
for i in range(20):
    for j in range(30):
        turtle.forward(x)
        turtle.left(6)
    x += 0.5
```

***Рисуем квадратную спираль***

```python
import turtle

turtle.shape('turtle')
x = 15
for i in range(20):
    for j in range(30):
        turtle.forward(x)
        turtle.left(90)
        x += 5
```

***Написание функции***

Как было сказано раньше, функции — это своего рода готовые кирпичики, из которых строится программа. До этого момента мы использовали стандартные функции (`print`, `input`, функции модуля `turtle`), теперь настало время написать функцию:

```python
>>> def hello(name):
...     print('Hello, ', name, '!')
...
>>> hello('world')
```
Hello,  world!

Это простейший пример функции, которая принимает в качестве параметра имя, а затем выводит на экран сообщение Hello, <имя>. Как видно из примера, функции в языке Python описываются при помощи ключевого слова `def`:

```python
def Имя_функции(параметр_1, параметр_2, ...):
    Блок_операций
```

Так же, как и в случае циклов и условных операторов, тело функции выделяется при помощи отступов.

Вызов функции осуществляется по имени с указанием параметров:

`hello('world')`

Внутри функции можно использовать те же синтаксические конструкции, что и вне её — циклы, ветвления, можно даже описывать новые функции. Естественно, внутри функции можно работать и с переменными.

Написанная ранее функция имеет особенность — она просто выводит текст на экран и не возвращает никакого результата. Многие функции, напротив, занимаются вычислением какого-либо значения, а затем возвращают его тому, кто эту функцию вызвал. В качестве примера можно рассмотреть функцию для сложения двух чисел:

```python
>>> def sum(a, b):
...     return a + b
...
>>> sum(1, 2)
3
>>> sum(5, -7)
-2
```

Для возврата значения из функции используется оператор return: в качестве параметра указывается значение, которое требуется вернуть.

***Рисуем 10 вложенных правильных многоугольников***. Используйте функцию, рисующую правильный n-угольник.
[Формулы](https://www.fxyz.ru/%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B_%D0%BF%D0%BE_%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%B8/%D0%BF%D0%BB%D0%BE%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D0%B8%D0%B3%D1%83%D1%80%D1%8B/%D0%B2%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D0%B8_%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B8/%D1%80%D0%B0%D0%B4%D0%B8%D1%83%D1%81_%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%BD%D0%BE%D0%B9_%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8/%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B0/) для нахождения радиуса описанной окружности. 

```python
import turtle
import math
turtle.shape('turtle')
n = 3
r = 10 #задаем радиус первой окружности
def more_agles(n, m): #опеределяем функцию, рисующую многоугольник
    q = 360 / n
    while n > 0:
        
        turtle.left(q)
        turtle.forward(m)
        n -= 1
        
while n < 13:
    m = 2 * r * math.sin(math.pi / n) #считаем размер стороны многоугольника по формуле "Площадь правильного многоугольника вписанного в окружность"(a=2Rsin (360/2n))
    x = (180 - 360 / n ) / 2
    turtle.left(x)
    
    more_agles(n,m)
    turtle.right(x)
    turtle.penup()
    turtle.forward(10)# задаем расстояние между окружностями
    
    turtle.pendown()
    n += 1
    r += 10 #раз расстояние между окружностями 10, увеличиваем радиус на 10
```

***Рисуем простой цветок***

```python
import turtle

my_turtle = turtle.Turtle()
for i in range(6):
    my_turtle.circle(50)
    my_turtle.right(60)
```

***Рисуем бабочку***

```python
import turtle

radius = 20
turtle.left(90)

for i in range(5):
  turtle.circle(radius)
  turtle.circle(-radius)
  radius += 10
```

***Рисуем пружину***

```python
import turtle
turtle.shape('turtle')
turtle.speed(3)
turtle.penup()
# отодвинем черепашку назад, чтобы поместилась пружина
turtle.setx(-450)
turtle.pendown()

for _ in range(4):
    # Повернуть черепашку под углом to_angle к вертикали (0 — наверх, 90 — направо);
    turtle.setheading(90)
    turtle.circle(-100, 180)
    turtle.circle(-20, 180)
turtle.circle(-100, 180)
turtle.done()
```

***Рисуем смайлик***

```python
import turtle
lion=turtle.Turtle()
lion.up()
lion.goto(0, -100)  
lion.down()

lion.begin_fill()
lion.fillcolor("yellow")  
lion.circle(100)
lion.end_fill()

lion.up()
lion.goto(-67, -40)
lion.setheading(-60)
lion.width(5)
lion.down()
lion.circle(80, 120)    
lion.fillcolor("black")

for i in range(-35, 105, 70):
    lion.up()
    lion.goto(i, 35)
    lion.setheading(0)
    lion.down()
    lion.begin_fill()
    lion.circle(10)   
    lion.end_fill()
    
lion.hideturtle()
```

***Рисуем звезду***
```python
import turtle
turtle.pensize(5)
turtle.pencolor("red")
turtle.forward(200)
for i in range(4):
    turtle.right(144)
    turtle.fd(200)
turtle.done()
```

***Рисуем 11-ти конечную звезду***

```python
from turtle import *
t = Turtle()
for i in range(11):
# угол - 180-180/11 градусов
    t.right(180-180/11)
    t.fd(200)
```

---

### Лекция №2. Алгебра Логики. Законы де Моргана. Тип bool. Конструкция `else + if = elif
Любая функция - это отображение множества на множество, область определения и множество значений.

<img alt="image" src="images/Svodnaja-tablitsa-logicheskikh-operatsij.jpeg"/>

***Законы алгебры логики***

<img alt="image" src="images/Законы алгебры логики.jpeg"/>

<img alt="image" src="images/Законы алгебры логики, др запись.png" />

<img alt="image" src="images/Конспект с доски, законы алгебры логики.jpeg"/>

***[Законы де Моргана](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%D1%8B_%D0%B4%D0%B5_%D0%9C%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B0)*** - логические правила, связывающие пары логических операций при помощи логического отрицания. В краткой форме звучат так:

***Отрицание конъюнкции есть дизъюнкция отрицаний.***

***Отрицание дизъюнкции есть конъюнкция отрицаний.***

<img alt="image" width="70%" src="images/Законы Де Моргана.jpg"/>

`==` - оператор сравнения двух значений

В Питоне если нужно перенести строку с выражением используем скобки (.....), так как он очень внимателен к переносам и требует сдвига, иначе будет ошибка выражения.

<img alt="image" src="images/bool true or false code example.jpg"/>

<img alt="image" src="images/каскадные условные конструкции.jpg"/>

***Python: Конструкция `else + if = elif`***

Это способ задать несколько альтернативных условий.

Функция `get_type_of_sentence()` из предыдущего урока различает только вопросительные и обычные предложения. Давайте попробуем добавить поддержку восклицательных предложений:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'

    if last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is normal'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'
```

Технически функция работает, но вопросительные предложения трактует неверно, да и с точки зрения семантики есть проблемы.

Проверка на наличие восклицательного знака происходит в любом случае, даже если уже был обнаружен вопросительный знак.

Ветка `else` описана именно для второго условия, но не для первого (именно поэтому вопросительное предложение становится "normal").

Для исправления ситуации воспользуемся ещё одной возможностью условной конструкции:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'
```

Теперь все условия выстроены в единую конструкцию. ***`elif` — это «если не выполнено предыдущее условие, но выполнено текущее»***. Получается такая схема:

- если последняя буква `?`, то 'question'

- иначе, если последняя буква `!`, то 'exclamation'

- иначе 'normal'

Выполнится только один из блоков кода, относящихся ко всей конструкции `if`.

Конструкция с несколькими `elif` может также служить отличной заменой конструкции `switch - case`

```python
a = int(input())
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')
```

### Лекция №3. Системы счисления. Литералы чисел. Разложение числа на цифры. Однопроходные алгоритмы без реализации.