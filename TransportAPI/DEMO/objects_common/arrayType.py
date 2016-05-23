class ArrayType(list):

    @staticmethod
    def factory(klass):
        if hasattr(klass, 'load_json'):
            if hasattr(klass, 'json_serializer'):
                return ArrayTypeComplexLoaderSerializer(klass)
            else:
                return ArrayTypeComplexLoader(klass)
        else:
            if hasattr(klass, 'json_serializer'):
                return ArrayTypeBasicLoaderSerializer(klass)
            else:
                return ArrayTypeBasicLoader(klass)

    def __init__(self, klass):
        super(ArrayType, self).__init__()
        self.klass = klass

    def load_json(self, json_struct):
        if type(json_struct) is list:
            del self[:]
            for element in json_struct:
                self.append_new(element)
        else:
            raise TypeError('', json_struct, 'list')


class ArrayTypeBasicLoader(ArrayType):

    def __init__(self, klass):
        super(ArrayTypeBasicLoader, self).__init__(klass)

    def append_new(self, json_struct):
        if type(json_struct) == self.klass:
            self.append(self.klass(json_struct))
        else:
            raise TypeError('', json_struct, str(self.klass)[7:-2])


class ArrayTypeComplexLoader(ArrayType):

    def __init__(self, klass):
        super(ArrayTypeComplexLoader, self).__init__(klass)

    def append_new(self, json_struct):
        self.append(self.klass(json_struct))


class Serializer(object):

    def json_serializer(self):
        return [x.json_serializer() for x in self]

    def __str__(self):
        return str(self.json_serializer())

class ArrayTypeComplexLoaderSerializer(ArrayTypeComplexLoader, Serializer):

    def __init__(self, klass):
        super(ArrayTypeComplexLoaderSerializer, self).__init__(klass)


class ArrayTypeBasicLoaderSerializer(ArrayTypeBasicLoader, Serializer):

    def __init__(self, klass):
        super(ArrayTypeBasicLoaderSerializer, self).__init__(klass)
