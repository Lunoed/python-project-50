# Вычислитель отличий (Python)

[![hexlet-check](https://github.com/Lunoed/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Lunoed/python-project-50/actions)

[![gendiff_check](https://github.com/Lunoed/python-project-50/actions/workflows/gendiff_check.yml/badge.svg)](https://github.com/Lunoed/python-project-50/actions/workflows/gendiff_check.yml)

Данный репозитоорий содержит код программы GENDIFF - утилита предназначена для нахождения различий между 2 файлами (плоскими либо со вложенной структурой) форматов JSON и YAML. 
Есть три формата отображения:
    - stylish (вложенный)
    [![asciicast](https://asciinema.org/a/DSar9krlcWDPAk7Y.svg)](https://asciinema.org/a/DSar9krlcWDPAk7Y)

    - plain (плоский)
    [![asciicast](https://asciinema.org/a/aCGQh7eXIf1Ccyqz.svg)](https://asciinema.org/a/aCGQh7eXIf1Ccyqz)

    - json (в формате json-файла)
    ...
## Стек

- Python

## Установка
Для установки данной программы необходима утилита uv.
Установить её можно следующим образом:

```bash
pip install uv
```
(Более подробную инструкцию можно почитать на официальном сайте: https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

```bash
git clone https://github.com/Lunoed/python-project-50.git

cd python-project-50

make install

```

## Использование

Пример использования программы на ранних этапах: 

[![asciicast](https://asciinema.org/a/Qw5FAaSG2KC9dDdE.svg)](https://asciinema.org/a/Qw5FAaSG2KC9dDdE)

Работа программы с плоскими yaml файлами

[![asciicast](https://asciinema.org/a/TcOHAsG1Jsx1EXyZ.svg)](https://asciinema.org/a/TcOHAsG1Jsx1EXyZ)

Работа программы с вложенными json и yaml файлами

[![asciicast](https://asciinema.org/a/DSar9krlcWDPAk7Y.svg)](https://asciinema.org/a/DSar9krlcWDPAk7Y)

Программа умеет делать "плоский" вывод сводки различий. Для этого нужно указывать формат - "plain"

[![asciicast](https://asciinema.org/a/aCGQh7eXIf1Ccyqz.svg)](https://asciinema.org/a/aCGQh7eXIf1Ccyqz)

Также есть возможность вывести результат в формате json. Для этого нужно указать формат - "json"

[![asciicast](https://asciinema.org/a/IvV6EAA6kFvC2Ba4.svg)](https://asciinema.org/a/IvV6EAA6kFvC2Ba4)

---

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
