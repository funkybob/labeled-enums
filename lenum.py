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

        for name, value in list(attrs.items()):
            if not name.isupper():
                continue
            if isinstance(value, tuple):
                value, label = value
            else:
                label = name.title().replace('_', ' ')
            _choices[value] = label
            attrs[name] = EnumProperty(value)
        attrs['_choices'] = _choices
        attrs['_reverse'] = {v: k for k, v in _choices.items()}

        return type.__new__(mcs, name, bases, dict(attrs))

    def __call__(cls, value):
        '''Provide a little backward compatibility with Enum'''
        if value in cls._choices:
            return value

    def __getitem__(cls, key):
        return cls._choices[key]

    def __setattr__(cls, key, value):
        raise AttributeError('Cannot change values on LabeledEnum type.')

    def __iter__(cls):
        return iter(cls._choices.items())

    def label(cls, label):
        return cls._reverse[label]


class LabeledEnum(metaclass=LabeledEnumMeta):
    '''Base class for choices constants.'''
