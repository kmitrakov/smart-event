# TODO: Необходимо отрефакторить метод отрисовки menu_main в шаблоне base.html.
#  Избавиться от дублирования кода.
menu_main = [{'title': "Main Page", 'urlname': 'index'},
             {'title': "Event Add", 'urlname': 'event_add'},
             {'title': "Contact", 'urlname': 'contact'},
             {'title': "About", 'urlname': 'about'},
             {'title': "Sign Out", 'urlname': 'sign_out'},
             {'title': "Sign In", 'urlname': 'sign_in'},
             {'title': "My Space", 'urlname': 'my_space'}
             ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu_main'] = menu_main

        return context
