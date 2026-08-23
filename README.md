# Brain Games

[![Actions
Status](https://github.com/VorobyevAM/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/VorobyevAM/devops-engineer-from-scratch-project-49/actions)

**Brain Games** --- набор консольных игр для тренировки логики и
математических навыков.

В каждой игре пользователю необходимо правильно ответить на три вопроса
подряд. При неправильном ответе игра завершается.

## Requirements

-   Python 3.10+
-   uv
-   Make

## Installation

Клонируйте репозиторий:

``` bash
git clone https://github.com/VorobyevAM/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
```

Установите зависимости:

``` bash
make install
```

Соберите пакет:

``` bash
make build
```

Установите пакет:

``` bash
make package-install
```

После установки игры можно запускать напрямую из терминала.

## Brain Games

Команда приветствия пользователя:

``` bash
brain-games
```

Пример:

``` text
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
```

## Игра «Проверка на чётность»

Необходимо определить, является ли случайное число чётным.

Ответьте `yes`, если число чётное, или `no`, если нечётное.

Запуск:

``` bash
brain-even
```

### Демонстрация

Добавьте сюда asciinema с демонстрацией установки, победы и поражения в
`brain-even`.

## Игра «Калькулятор»

Необходимо вычислить результат случайного арифметического выражения.
Поддерживаются операции `+`, `-` и `*`.

Запуск:

``` bash
brain-calc
```

### Демонстрация

Добавьте сюда asciinema с демонстрацией `brain-calc`.

## Игра «НОД»

Необходимо найти наибольший общий делитель двух чисел.

Запуск:

``` bash
brain-gcd
```

### Демонстрация

Добавьте сюда asciinema с демонстрацией `brain-gcd`.

## Игра «Арифметическая прогрессия»

Необходимо определить пропущенное число в арифметической прогрессии.

Запуск:

``` bash
brain-progression
```

### Демонстрация

Добавьте сюда asciinema с демонстрацией `brain-progression`.

## Игра «Простое ли число?»

Необходимо определить, является ли случайное число простым.

Ответьте `yes`, если число простое, или `no` в противном случае.

Запуск:

``` bash
brain-prime
```

### Демонстрация

Добавьте сюда asciinema с демонстрацией `brain-prime`.

## Development

Проверка кода линтером:

``` bash
make lint
```

Сборка проекта:

``` bash
make build
```

Запуск игр без установки пакета:

``` bash
uv run brain-even
uv run brain-calc
uv run brain-gcd
uv run brain-progression
uv run brain-prime
```

## Games

  Игра                        Команда
  --------------------------- ---------------------
  Проверка на чётность        `brain-even`
  Калькулятор                 `brain-calc`
  Наибольший общий делитель   `brain-gcd`
  Арифметическая прогрессия   `brain-progression`
  Простое ли число?           `brain-prime`

Для успешного прохождения каждой игры необходимо дать **три правильных
ответа подряд**.

