class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access = 'user'
        user_list[user_id] = self
        print(f'Пользователь {name} добавлен под id {user_id}')


    def set_admin(self):
        self.__access = 'admin'


    def get_user_info(self, user_id):
        return user_list[user_id].__name, user_list[user_id].__access


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        super().set_admin()
        user_list[user_id] = self
        print(f'Администратор {name} добавлен под id {user_id}')


    def add_user(self, user_id, name):
        if user_id not in user_list:
            user_list[user_id] = User(user_id, name)
            print(f'Пользователь {name} добавлен под id {user_id}')
        else:
            print(f'Пользователь с id {user_id} уже есть списке')


    def remove_user(self, user_id):
        if user_id not in user_list:
            print(f'Пользователя с id {user_id} нет в списке')
        else:
            del user_list[user_id]
            print(f'Пользователь с id {user_id} удален из списка')


user_list = {}

admin1 = Admin("12345", "Иван Иванов")

admin1.add_user("212345", "Василий Васильев")
admin1.add_user("212346", "Ксения Петрова")
admin1.add_user("212347", "Екатерина Сорокина")
print(user_list)

admin1.remove_user('212345')
print(user_list)
print(admin1.get_user_info('12345'))
print(admin1.get_user_info('212346'))

user_list['212348'] = User('212348', 'Виталий Скворцов')