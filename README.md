# Вычислитель отличий (Python)

[![hexlet-check](https://github.com/Lunoed/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Lunoed/python-project-50/actions)

[![gendiff_check](https://github.com/Lunoed/python-project-50/actions/workflows/gendiff_check.yml/badge.svg)](https://github.com/Lunoed/python-project-50/actions/workflows/gendiff_check.yml)

Данный репозиторий содержит код программы GENDIFF - утилита, предназначенная для нахождения различий между 2 файлами (плоскими либо со вложенной структурой) форматов JSON и YAML. 
Есть три формата отображения:

- stylish (вложенный)

- plain (плоский)

- json 
    ...
## Стек

- Python 3.14

## Установка дополнительной утилиты
Для установки данной программы необходима утилита uv.
Установить её можно следующим образом:

```bash
pip install uv
```
(Более подробную инструкцию с альтернативными способами установки можно почитать на официальном сайте: https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

## Скачивание репозитория и установка программы
- Скачивание репозитория:

```bash
git clone https://github.com/Lunoed/python-project-50.git
cd python-project-50
```

- Установка пакетов:

```bash
make install
```
- Создание дистрибутива:

```bash
make build
```

- Установка проекта в систему:

```bash
make package-istall
```
## Краткий пример использования программы и вывода
``` bash
gendif -f plain path/to/file1.json path/to/file2.json
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
...
```

## Использование

Пример использования программы на ранних этапах: 

[![asciicast](https://asciinema.org/a/Qw5FAaSG2KC9dDdE.svg)](https://asciinema.org/a/Qw5FAaSG2KC9dDdE)

Работа программы с плоскими yaml файлами

[![asciicast](https://asciinema.org/a/tMezCi6OrelGos6o.svg)](https://asciinema.org/a/tMezCi6OrelGos6o)

Работа программы с вложенными json и yaml файлами

[![asciicast](https://asciinema.org/a/m56FWTJaBt5Q6sFv.svg)](https://asciinema.org/a/m56FWTJaBt5Q6sFv)

Программа умеет делать "плоский" вывод сводки различий. Для этого нужно указывать формат - "plain"

[![asciicast](https://asciinema.org/a/2lPgwdtSnAJlhiu9.svg)](https://asciinema.org/a/2lPgwdtSnAJlhiu9)

Также есть возможность вывести результат в формате json. Для этого нужно указать формат - "json"

[![asciicast](https://asciinema.org/a/Y9wCuxiNy1LfaUvd.svg)](https://asciinema.org/a/Y9wCuxiNy1LfaUvd)

---

