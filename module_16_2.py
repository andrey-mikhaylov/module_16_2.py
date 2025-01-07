import uvicorn
from typing import Annotated
from fastapi import FastAPI, Path


app = FastAPI()


@app.get("/")
async def main_page() -> str:
    """ Главная страница """
    return "Главная страница"


@app.get("/user/admin")
async def login_as_admin() -> str:
    """ Вход администратора """
    return "Вы вошли как администратор"


@app.get("/user/{username}/{age}")
async def get_user_info(
        username: Annotated[str, Path(title='Имя пользователя', min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(title='Возраст', ge=18, le=120, description='Enter age', example=24)]
    ) -> str:
    """ Информация о пользователе """
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get("/user/{user_id}")
async def login_as_user_id(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
    ) -> str:
    """ Вход пользователя """
    return f"Вы вошли как пользователь № {user_id}"


if __name__ == '__main__':
    uvicorn.run(app)


"""
2024/02/17 00:00|Домашнее задание по теме "Валидация данных".
Цель: научится писать необходимую валидацию для вводимых данных при помощи классов Path и Annotated.

Задача "Аннотация и валидация":
Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
'/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id, для которого необходимо написать следующую валидацию:
Должно быть целым числом
Ограничено по значению: больше или равно 1 и меньше либо равно 100.
Описание - 'Enter User ID'
Пример - '1' (можете подставить свой пример не противоречащий валидации)
'/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username и age, для которых необходимо написать следующую валидацию:
username - строка, age - целое число.
username ограничение по длине: больше или равно 5 и меньше либо равно 20.
age ограничение по значению: больше или равно 18 и меньше либо равно 120.
Описания для username и age - 'Enter username' и 'Enter age' соответственно.
Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои примеры не противоречащие валидации).

Пример результата выполнения программы:
Ошибки валидации для маршрутов '/user/{user_id}' и '/user/{username}/{age}' :

Как должен выглядеть Swagger:



Примечания:
Если у вас не отображаются параметры Path, проверьте, сделали вы присвоение данных или подсказку типа. Верно: username: Annotated[...]. Не верно: username = Annotated[...]
Файл module_16_2.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""
