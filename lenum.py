class EnumProperty:
    '''Descriptor class for yielding values, but not allowing setting.'''
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, cls=None):
        return self.value


class LabeledEnumMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        '''Use an ordered dict for declared values.'''
        return OrderedDict()

    def __new__(mcs, name, bases, attrs):
        _choices = OrderedDict()
        _label_map = {}

        for name, value in list(attrs.items()):
            if not name.isupper():
                continue
            if isinstance(value, tuple):
                value, label = value
            else:
                label = name.title().replace('_', ' ')
            _choices[value] = label
            _label_map[label] = value
            attrs[name] = EnumProperty(value)
        attrs['_choices'] = _choices
        attrs['_labem_map'] = _label_map

        return type.__new__(mcs, name, bases, dict(attrs))

    def __getitem__(cls, key):
        return cls._choices[key]

    def __iter__(cls):
        return iter(cls._choices.items())


class LabeledEnum(metaclass=LabeledEnumMeta):
    '''Base class for choices constants.'''
