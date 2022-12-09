# TODO: Доработать метод отрисовки menu_main в шаблоне base.html.
#  Избавиться от дублирования кода.
menu_main = [{'title': "Main Page", 'urlname': 'index'},
             {'title': "Event Add", 'urlname': 'event_add'},
             {'title': "Contact", 'urlname': 'contact'},
             {'title': "About", 'urlname': 'about'},
             {'title': "Sign Out", 'urlname': 'sign_out'},
             {'title': "Sign In", 'urlname': 'sign_in'},
             {'title': "Sign Up", 'urlname': 'sign_up'},
             {'title': "My Space", 'urlname': 'my_space'}
             ]


class DataMixin:
    # TODO: Доработать пагинацию в шаблоне base.html.
    #  Сделать блокировку кнопок "<", ">" вместо их не отображения.
    #  Добавить кнопки "<<", ">>".
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs

        menu_user = menu_main.copy()

        # TODO: Добавить удаление пунктов меню для неавторизованных пользователей.
        #if not self.request.user.is_authenticated:

        context['menu_main'] = menu_user

        return context
