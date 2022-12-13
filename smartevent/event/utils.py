# TODO: Доработать метод отрисовки menu_main в шаблоне base.html.
#  Избавиться от дублирования кода.
# Исходное главное меню.
from urllib import request

menu_main_initial = [{'title': 'Main Page', 'urlname': 'index'},
                     {'title': 'Event Add', 'urlname': 'event_add'},
                     {'title': 'Contact', 'urlname': 'contact'},
                     {'title': 'About', 'urlname': 'about'},
                     {'title': 'Sign In', 'urlname': 'sign_in'},
                     {'title': 'My Space', 'urlname': 'my_space'}
                     ]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs

        # TODO: Перенести в отдельный метод.
        #  Избавиться от лишних циклов.
        # Изменение главного меню в зависимости от контекста пользователя.
        menu_main = menu_main_initial.copy()
        if not self.request.user.is_authenticated:
            for i in range(len(menu_main)):
                if menu_main[i]['title'] == 'Event Add':
                    del menu_main[i]
                    break

            for i in range(len(menu_main)):
                if menu_main[i]['title'] == 'My Space':
                    del menu_main[i]
                    break

        else:
            for i in range(len(menu_main)):
                if menu_main[i]['title'] == 'Sign In':
                    del menu_main[i]
                    break


        context['menu_main'] = menu_main

        return context
