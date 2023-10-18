from fastapi import APIRouter
from datetime import datetime

from database.userservice import add_new_user_db, edit_user_info_db, delete_user_db, get_exact_user_db, check_user_email_db

from user import UserRegisterModel, EditUserModel

user_router = APIRouter(prefix='/user', tags=['Работа с пользователем'])


# Регистрация пользователя
@user_router.post('/registr')
async def registr_user(data: UserRegisterModel):
    # переводим pydantic в обычный словарь
    new_user_data = data.model_dump()
    # вызов функции для проверки почты в базе
    checker = check_user_email_db(data.email)

    # Если нет в базе такого пользователя, то регистрация
    if not checker:
        result = add_new_user_db(reg_date=datetime.now(), **new_user_data)

        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'пользователь с такой почтой уже существует'}


# Получение информации о пользователе
@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id=user_id)

    return {'status': 1, 'message': result}


# Изменить информацию о пользователе
@user_router.put('/edit-data')
async def edit_user(data: EditUserModel):
    # переводим pydantic в обычный словарь
    change_data = data.model_dump()
    result = edit_user_info_db(**change_data)

    return {'status': 1 if result else 0, 'message': result}


# Удалить пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id=user_id)

    return {'status': 1, 'message': result}
