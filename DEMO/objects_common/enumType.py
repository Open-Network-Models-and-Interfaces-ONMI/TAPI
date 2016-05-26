class EnumType(object):
    # Internal data storage uses integer running from 0 to range_end
    # range_end is set to the number of possible values that the Enum can take on
    # External representation of Enum starts at 1 and goes to range_end + 1

    def __init__(self, initial_value):
        self.set(initial_value)

    def load_json(self, json_struct):
        self.set(json_struct)

    def json_serializer(self):
        # Returns a string
        # This could be changed to encode enums as integers when transmitting messages
        if self.value < 0:
            return None
        else:
            return type(self).possible_values[self.value]

    def __str__(self):
        return str(self.json_serializer())

    def get(self):
        # Returns an integer, using the external representation
        return self.value + 1

    def set(self, value):
        # The value to set can be either a string or an integer
        if type(value) is str:
            # This will raise ValueError for wrong assignments
            try:
                self.value = type(self).possible_values.index(value)
            except ValueError:
                raise ValueError('', value, type(self).possible_values)
        elif type(value) is int:
            if value >= 0 and value <= type(self).range_end:
                # External representation of Enum starts at 1, internal at 0. External value 0 by default
                # to indicate empty object.
                value = value - 1
                self.value = value
            else:
                raise ValueError('', value, type(self).range_end)
        else:
            raise TypeError('', value, 'string or integer')
