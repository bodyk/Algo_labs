# Лабораторна робота 2
## Виконав: Баланик Богдан (Група ІР-25)
### Рівень 3. Варіант 1

Зоомагазин займається продажем хом’ячкiв. Це мирнi домашнi iстоти, проте, як
виявилося, вони мають цiкаву харчову поведiнку.
Для того, щоб прогодувати хом’ячка, який живе наодинцi, потрiбно H пакетiв корму
на день. Однак, якщо кiлька хом’ячкiв живуть разом, у них прокидається жадiбнiсть.
У такому випадку кожен хом’ячок з’їдає додатково G пакетiв корму в день за
кожного сусiда. Денна норма H та жадiбнiсть G є iндивiдуальними для кожного
хом’ячка.
Всього в магазинi є C хом’ячкiв. Ви бажаєте придбати якомога бiльше, проте у вас
є всього S пакетiв їжi на день. Визначте максимальну кiлькiсть хом’ячкiв, яку ви
можете прогодувати.

Реалізуйте функцію, яка поверне число - максимальне число хо
Вхідні параметри функції:
S — ваш денний запас їжi. 0 ≤ S ≤ 109
C — загальна кiлькiсть хом’ячкiв, яка є в продажу, 1 ≤ C ≤ 105
Матриця `hamsters`, яка містить С рядків, перший стовчик якої містить денну норму корму, другий - рiвень жадiбностi кожного хом’ячка. Деннs нормb є цілими додатніми числами і гарантовано меншими за 109. Іноді у вас можуть бути не жадібні хом’ячки, але також можуть траплятись і надзвичайно жадібні, рівень жадібності може бути як нульовим, так і великим цілим числом
<pre>
Приклад 1

S = 7
C = 3
hamsters = `[ [1 2], [2 2], [3 1]]``

Результат:
2

Пояснення: Можна взяти першого хом’ячка та будь-якого з iнших двох.

Приклад 2

S = 19
C = 4
hamsters = `[ [5 0], [2 2], [1 4], [5 1]]

Результат:
3
Пояснення: Третiй хом’ячок надто жадiбний. Можна взяти всiх iнших трьох, тодi
за день вони з’їдять (5 + 0 · 2) + (2 + 2 · 2) + (5 + 1 · 2) = 18 пакетiв

Приклад 3
hamstr .in
S = 2
C = 2
hamsters = `[[1 50000], [1 60000]]

Результат:
1
Пояснення: Обидва хом’ячки надто жадiбнi, щоб їсти разом.
</pre>
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище