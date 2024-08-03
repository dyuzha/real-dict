class Field:
    pass

class IntegerField(Field):
    pass

class CharField(Field):
    pass


class ModelMeta(type):

    def __new__(mcs, class_name, parents, attributes):
        print(class_name, attributes)
        c = super(ModelMeta, mcs).__new__(mcs, class_name, parents, attributes)
        setattr(c, '_model_name', attributes['__qualname__'].lower())
        return c

class Model(metaclass=ModelMeta):
    pass


class CityModel(Model):
    id = IntegerField()
    name = CharField()
    population = IntegerField()


if __name__ == '__main__':
    model = CityModel()
