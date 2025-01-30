### Hexlet tests and linter status:
[![Actions Status](https://github.com/marentsov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/marentsov/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/211f3fb05430bee114cc/maintainability)](https://codeclimate.com/github/marentsov/python-project-50/maintainability)
[![my_check](https://github.com/marentsov/python-project-50/actions/workflows/my_workflow.yml/badge.svg)](https://github.com/marentsov/python-project-50/actions/workflows/my_workflow.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/211f3fb05430bee114cc/test_coverage)](https://codeclimate.com/github/marentsov/python-project-50/test_coverage)
***

# Вычислитель отличий (gendiff)
- второй проект, разработанный в рамках обучения на курсе Хекслет. Вычислитель отличий или gendiff это инструмент командной строки для поиска различий между файлами. 
***

## Для запуска инструмента понадобятся: 
[Python 3.12.0 +] - (https://www.python.org/downloads/)

[UV 0.5.11 +] - (https://astral.sh)
***

## Установка:
``` 
git clone git@github.com:marentsov/python-project-50.git
```
````
cd python-project-50
````
`````
uv build
``````
````````
uv tool install dist/*.whl
````````
***

### Вычислитель отличий поддерживает следующие форматы для сравниваемых файлов: 

#### - JSON (.json)
#### - YAML (.yaml, .yml)
***

## Как пользоваться инструментом: 

1. Поместите файлы для сравнения в папку tests/test_data. 
2. Выполните команду заменив первый и второй файл на ваши файлы
````
uv run gendiff tests/test_data/(первый файл) tests/test_data/(второй файл)
````
3. По умолчанию применится **stylish** форматтер, для того чтобы получить вывод программы с применением другого форматтера, укажите с помощью флага **-f** необходимый формат (**json** или **plain**). Примеры вывода инструмента при использовании разных форматов можно увидеть ниже.
***

### Пример вывода инструмента при использовании разных форматтеров:

- **stylish** (форматтер по умолчанию)
````
uv run gendiff tests/test_data/(первый файл) tests/test_data/(второй файл)
````
``````
uv run gendiff -f stylish tests/test_data/(первый файл) tests/test_data/(второй файл)
``````
демонстрация:
***
- **plain** 
````
uv run gendiff -f plain tests/test_data/(первый файл) tests/test_data/(второй файл)
````
демонстрация:
***
- **json**
````
uv run gendiff -f json tests/test_data/(первый файл) tests/test_data/(второй файл)
````
демонстрация: 
*** 




