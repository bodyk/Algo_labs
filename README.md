# Лабораторна робота 1
## Рівень 3.

### Варіант 1

Потрібно написати програму для обходу двовимірного масиву розміром NxM у форматі "зігзагу". Зігзаговий обхід означає, що спочатку ми рухаємось по діагоналях масиву, пчинаючи з лівої верхньої точки.  Другим елементом буде виведено елемент, який знаходиться справа, потім  знизу і ліворуч, далі ще крок вниз і рухаємось по діагоналі знову вправо. Для масиву розміром 3x3 обхід у форматі зігзагу виглядає так (де номер у клітинці відповідає порядку її відвідин):

<pre>
1 2 6
3 5 7
4 8 9
</pre>
Для масиву 3 х 5 це матиме вигляд:
<pre>
1  2  6   7  12
3  5  8  11  13
4  9  10 14 15
</pre>
Реалізуйте алгоритм, який отримає на вхід масив розміром m та n та поверне одномірний масив з значеннями елементів вхідного масиву при обході його у порядку, зазначеному вище у задачі

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` . Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m =2, n =4, n = 1, m = 6, n == m == 1
