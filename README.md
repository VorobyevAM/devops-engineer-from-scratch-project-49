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

``` bash
git clone https://github.com/VorobyevAM/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
make install
make build
make package-install
```

## Brain Games

``` bash
brain-games
```

## Игра «Проверка на чётность»

``` bash
brain-even
```

### Демонстрация

[![asciicast](https://asciinema.org/a/jgJUvTpJozCK8heY.svg)](https://asciinema.org/a/jgJUvTpJozCK8heY)

## Игра «Калькулятор»

``` bash
brain-calc
```

### Демонстрация

[![asciicast](https://asciinema.org/a/GjiJYWdCRR0DVcfU.svg)](https://asciinema.org/a/GjiJYWdCRR0DVcfU)

## Игра «НОД»

``` bash
brain-gcd
```

### Демонстрация

[![asciicast](https://asciinema.org/a/pRB06RSAbXlQKQKd.svg)](https://asciinema.org/a/pRB06RSAbXlQKQKd)

## Игра «Арифметическая прогрессия»

``` bash
brain-progression
```

### Демонстрация

[![asciicast](https://asciinema.org/a/QaCcPCzYlABXca15.svg)](https://asciinema.org/a/QaCcPCzYlABXca15)

## Игра «Простое ли число?»

``` bash
brain-prime
```

### Демонстрация

[![asciicast](https://asciinema.org/a/EXOyXN0URe5kC6uY.svg)](https://asciinema.org/a/EXOyXN0URe5kC6uY)

## Development

``` bash
make lint
make build
```

Для успешного прохождения каждой игры необходимо дать **три правильных
ответа подряд**.
