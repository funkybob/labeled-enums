from collections import OrderedDict


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

        names = []
        for name, value in list(attrs.items()):
            if not name.isupper():
                continue
            names.append(name)
            if isinstance(value, tuple):
                value, label = value
            else:
                label = name.title().replace('_', ' ')
            _choices[value] = label
            attrs[name] = EnumProperty(value)
        attrs['names'] = tuple(names)
        attrs['__members__'] = _choices
        attrs['_reverse'] = {v: k for k, v in _choices.items()}

        return type.__new__(mcs, name, bases, dict(attrs))

    def __call__(cls):
        return cls

    def __getitem__(cls, key):
        return cls.__members__[key]

    def __setattr__(cls, key, value):
        raise AttributeError('Cannot change values on LabeledEnum type.')

    def __iter__(cls):
        return iter(cls.__members__.items())

    def for_label(cls, label):
        return cls._reverse[label]


class LabeledEnum(metaclass=LabeledEnumMeta):
    '''Base class for choices constants.'''
