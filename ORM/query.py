AND = 'and'
OR = 'or'

class Q:
    def __init__(self, exp_type=AND, **kwargs):
        self.separator = exp_type
        self._params = kwargs

    def __str__(self):
        kv_pairs = [f"{k} = {v}" for k, v in self._params.items()]
        return f"{self.separator}".join(kv_pairs)

    def __bool__(self):
        return bool(self._params)



class BaseExp:
    name = None

    def add(self, *args, **kwargs):
        # Ошибка перезаписи
        raise NotImplementedError()

    def definition(self):
        return self.name + '\n\t' + self.line() + '\n'

    def line(self):
        raise NotImplementedError()

    def __bool__(self):
        raise NotImplementedError()


class Select(BaseExp):
    name = 'SELECT'

    def __init__(self):
        self._params = []

    def add(self, *args, **kwargs):
        self._params.extend(args)

    def line(self):
        separator = ','
        return separator.join(self._params)

    def __bool__(self):
        return bool(self._params)


class From(BaseExp):
    name = 'from'

    def __init__(self):
        self._params = []

    def add(self, *args, **kwargs):
        self._params.extend(args)

    def line(self):
        separator = ','
        return separator.join(self._params)

    def __bool__(self):
        return bool(self._params)


class Where(BaseExp):
    name = 'Where'

    def __init__(self, exp_type=AND, **kwargs):
        self._q = Q(exp_type, **kwargs)

    def add(self, exp_type=AND, **kwargs):
        self._q = Q(exp_type, **kwargs)
        return self._q

    def line(self):
        return str(self._q)

    def __bool__(self):
        return bool(self._q)



class Query:
    def __init__(self):
        self._data = {"select": Select(), "from": From(), "where": Where()}

    def SELECT(self, *args):
        self._data['select'].add(*args)
        return self

    def FROM(self, *args):  
        self._data['from'].add(*args)
        return self

    def WHERE(self, exp_type=AND, **kwargs):
        self._data['where'].add(exp_type=AND, **kwargs)
        return self

    def _lines(self):
        for key, value in self._data.items():
            yield value.definition()

    def __str__(self):
        return ''.join(self._lines())


if __name__ == '__main__':
    q = Query()
    q = q.SELECT('*').FROM('table').WHERE(id=1)
    print(q)


