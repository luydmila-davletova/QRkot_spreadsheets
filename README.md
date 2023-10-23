# QRKot

## Описание
Расширеная версия проекта  QRkot с добавлением формирования отчета в гугл таблицах

### Проекты
В Фонде может быть открыто несколько целевых проектов. У каждого проекта есть название,  
описание и сумма, которую планируется собрать. После того как нужная сумма собрана — проект закрывается.  
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект,  
открытый раньше других; когда этот проект набирает необходимую сумму,
и закрывается — пожертвования начинают поступать в следующий проект.

### Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием.  
Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект.  
Каждое полученное пожертвование автоматически добавляется в первый открытый проект,  
который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в  
Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта.  
При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.  

### Права пользователей
Любой посетитель сайта (в том числе неавторизованный) может посмотреть список всех проектов.
Суперпользователь может: 
1. создавать проекты,
2. удалять проекты, в которые не было внесено средств,
3. изменять название и описание существующего проекта, устанавливать для него новую требуемую сумму (но не меньше уже внесённой).

* Никто не может менять через API размер внесённых средств, удалять или модифицировать закрытые проекты, изменять даты создания и закрытия проектов.

### Формирование отчета в гугл таблицах 
QRKot может формировать отчёт в гугл-таблице. В таблице будут закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму
# Стек технологий
<p>
  <a 
  target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-_3.9-green.svg">
  </a>
  <a 
  target="_blank" href="https://pypi.org/project/fastapi/" title="fastapi"><img src="https://img.shields.io/badge/fastapi-0.78-green.svg">
  </a>
  <a
  target="_blank" href="https://pypi.org/project/SQLAlchemy/" title="SQLAlchemy"><img src="https://img.shields.io/badge/SQLAlchemy-1.4-green.svg">
  </a>
  <a 
  target="_blank" href="https://pypi.org/project/alembic/" title="Alembic"><img src="https://img.shields.io/badge/Alembic-1.7-green.svg">
  </a>
    <a 
  target="_blank" href="https://pypi.org/project/aiogoogle/" title="Aiogoogle"><img src="https://img.shields.io/badge/Aiogoogle-4.2-green.svg">
  </a>
</p>

## **Как запустить проект**:

* Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/luydmila-davletova/cat_charity_fund
```

* Создать и активировать виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```

* Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

* Создание БД.
```
alembic upgrade head
```
* Наполнение env-файла.
```
APP_AUTHOR= Автор
AUTHOR_PASS= Пароль
DEADLINE_DATE= Время
DATABASE_URL= База (sqlite+aiosqlite:///./fastapi.db)
SECRET = Секрет
FIRST_SUPERUSER_EMAIL= Имя супер юзера
FIRST_SUPERUSER_PASSWORD = Пароль от супер юзера
type: Optional[str] = None              |
project_id: Optional[str] = None        |
private_key_id: Optional[str] = None    |
private_key: Optional[str] = None       |  Параметры из json google
client_email: Optional[str] = None      |
client_id: Optional[str] = None         |
auth_uri: Optional[str] = None          |
token_uri: Optional[str] = None         |
auth_provider_x509_cert_url:            |
client_x509_cert_url:                   |
email твой маил
```
* Стандартный запуск:
```
uvicorn app.main:app
```
* Запуск сервера с автоматическим перезапуском при изменении кода (только для режима разработки):
```
uvicorn app.main:app --reload
```
Сервер будет доступен локально по адресу: http://127.0.0.1:8000
