import json
import hashlib
import os

DIR_PATH = os.getcwd()  # это путь к нашему файлу.
FILE_PATH = DIR_PATH + '/users.json'  # путь к файлу users.json

class HashClassMixin:
    def hash_password(self, password, salt=None):
        """метод для хеширования пароля.Принадлежит классу RegisterMixin"""
        if not salt:
            salt = os.urandom(32)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
        return hashed_password
class RegisterMixin(HashClassMixin):
    """это для регистрации..."""
    def _validate_password(self, password, password2):
        """здесь валидация пароля,проверка"""
        if len(password) < 8:
            raise ValueError("Password must be at least 8 symbols")
        elif password.isdigit() or password.isalpha():
            raise ValueError("Password must contain digits and letters")
        elif password != password2:
            raise ValueError("Passwords aren\'t similar!")

    def register(self, username, first_name, last_name, password, password2):
        """проверка правильной регистрации.Чтобы имена не совпадали и пароли."""
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)

            try:
                id = data[-1]["id"] + 1
            except (IndexError, ValueError):
                data = []
                id = 1
            is_username_used = any([x['username'] == username for x in data])
        self._validate_password(password, password2)
        salt = os.urandom(32)
        hashed_password = {"password": self.hash_password(password, salt).decode('latin-1'), "salt": salt.decode('latin-1')}
        with open(FILE_PATH, "w") as file:
            if is_username_used:
                json.dump(data, file)
                raise ValueError('Username is already taken!')
            user = {"id": id, "username": username, "first_name": first_name, "last_name": last_name,
                    "password": hashed_password}
            data.append(user)
            json.dump(data, file, indent=4)
            return "успешно зарегестрированы"  # {"status": 201, 'msg': "Успешно зарегестрированы"}
class LoginMixin(HashClassMixin):
    def login(self, username, password):
        with open("users.json", 'r') as file:
            data = json.load(file)
            try:
                user = list(filter(lambda x: x['username'] == username, data))[0]
            except IndexError:
                raise ValueError("Вы возможно не правильно ввели имя или пароль!")
            user_password=user['password']['password'].encode('latin-1')
            salt=user['password']['salt'].encode('latin-1')
            hashed_password=self.hash_password(password,salt)
            if user_password != hashed_password:
                raise ValueError("Неправильно ввели пароль или имя")
        return {"status": 200, "msg": "Успешно вошли в свой аккаунт!", 'user': user['username']}


# obj = RegisterMixin()
# print(obj.register("ZhanDajner2d28", "Daffniel", "Zhanbolotov", "bastarrd123", "bastarrd123"))
# obj1=LoginMixin()
# print(obj1.login('ZhanDan228',"274627,lp46abc"))
"""
# load-функция которая считывает данные из файла JSON
# loads-функция которая считывает данные из текста JSON
# dump-записывает данные в файл формата JSON
# dumps-записывает данные в текст формата JSON
"""