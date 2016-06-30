from collections import OrderedDict
import re


class KeyedArrayKeyError(Exception):
    pass

class KeyedArrayDiscriminatorError(Exception):
    pass

class KeyedArrayType(OrderedDict):

    def __init__(self, klass, key, diff = None):
        super(KeyedArrayType, self).__init__()
        if isinstance(klass,tuple):
            self.klasses = []
            for k in klass:
                self.klasses.append(k)
            if diff:
                self.discriminator = diff
            else:
                raise KeyedArrayDiscriminatorError('More than one child class but not discriminator found.', None, None)
        else:
            self.klass = klass

        self.key = key

    def load_json(self, json_struct):
        if type(json_struct) is list:
            self.clear()
            for element in json_struct:
                if hasattr(self,'discriminator'):
                    for k in self.klasses:
                        if to_upper_camelcase(element[self.discriminator]) == str(k)[2:-2].split('.')[-1]:
                            self.klass = k

                if self.key in element:
                    self[element[self.key]] = self.klass(element)
                else:
                    raise KeyedArrayKeyError('', element, self.key)
        else:
            raise TypeError('', json_struct, 'list')

    def json_serializer(self):
        return [a.json_serializer() for a in self.values()]

    def __str__(self):
        return str(self.json_serializer())

def to_upper_camelcase(name):
    """ Converts the name string to upper camelcase by using "-" and "_" as
    markers.
    """
    return re.sub(r'(?:\B_|\b\-|^)([a-zA-Z0-9])', lambda l: l.group(1).upper(),
                  name)

