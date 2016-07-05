from keyedArrayType import KeyedArrayKeyError

class JsonObject(object):

    def __init__(self, json_struct=None):
        self.build_child_objects_list()
        if json_struct is not None:
            self.load_json(json_struct)

    def build_child_objects_list(self):
        self._child_objects = [i for i in dir(self) if not i.startswith('__') and not callable(getattr(self, i))]

    def json_serializer(self):
        ret={}
        for item in self._child_objects:
            if hasattr(getattr(self, item), 'json_serializer'):
                if getattr(self, item).json_serializer():
                    ret[item]=getattr(self, item).json_serializer()
            else:
                if getattr(self, item):
                    ret[item]=getattr(self, item)
        return ret

    def __str__(self):
        return str(self.json_serializer())

    def byteify(self,input):
        if isinstance(input, dict):
            return {self.byteify(key):self.byteify(value) for key,value in input.iteritems()}
        elif isinstance(input, list):
            return [self.byteify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input

    def load_json(self, json_struct):
        json_struct=self.byteify(json_struct)
        if type(json_struct) != dict:
            raise TypeError('', json_struct, 'object')
        # Run through the keys in the input structure
        for key in json_struct:
            # Check if there is an attribute in this object that has the name of the key
            if key in self._child_objects:
                if hasattr(getattr(self, key), 'load_json'):
                    try:
                        getattr(self, key).load_json(json_struct[key])
                    except KeyError as inst:
                        raise KeyError(key + '/' + inst.args[0])
                    except ValueError as inst:
                        raise ValueError(key + '/' + inst.args[0], inst.args[1], inst.args[2])
                    except TypeError as inst:
                        raise TypeError(key + '/' + inst.args[0], inst.args[1], inst.args[2])
                    except KeyedArrayKeyError as inst:
                        raise KeyedArrayKeyError(key + '/' + inst.args[0], inst.args[1], inst.args[2])
                else:
                    # basic type
                    if type(json_struct[key]) == type(getattr(self, key)):
                        setattr(self, key, json_struct[key])
                    else:
                        raise TypeError(key, json_struct[key], str(type(getattr(self, key)))[7:-2])
            else:
                raise KeyError(key)
