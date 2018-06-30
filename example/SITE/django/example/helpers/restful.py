# -*- coding: utf-8 -*-

class restful(object):
    # объект который все методы соберет в один словарь
    def __init__(self, getter):
        # каждому методу сопоставляется функция которая его обрабатывает
        self._Dispatch = {'GET': getter}

    def add_handler(self, method):
        # функция будет использоваться как декоратор
        def add(handler):
            self._Dispatch[method.upper()] = handler
            return self
        return add

    def __call__(self, request, *args, **kwargs):
        # объект при вызове проверяет какой метод из ReST выбран
        # POST, GET, HEAD и т.п.
        # и вызывает соответствующий обработчик
        # в случае если метод не известен, то подставляется обработчик метода GET
        try:
            handler = self._Dispatch[request.method.upper()]
            return handler(request, *args, **kwargs)
        except KeyError:
            # если метод не поддерживается то переделываем на метод GET
            handler = self._Dispatch['GET']
            return handler(request, *args, **kwargs)

