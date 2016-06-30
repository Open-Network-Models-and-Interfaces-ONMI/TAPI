# Common Objects
This folder contains python class definitions for four classes: JsonObject, EnumType, KeyedArrayType, ArrayType.

## JsonObject
This class represents an JSON object, which is encoded as '{}'. The objects children are stored in python as attributes of this object.

To generate the JSON representation of this object as a dictionary, including all the child elements, call the method 'json_serializer'. The child elements are recursively serialized to JSON, by calling the method 'json_serializer' on all child elements, if it is available.

A python object that inherits from JsonObject must define its attributes before calling the super() method, such that the attributes are registered as attributes of the JSON object.
To set the values of the attributes, call the method 'load_json' with a dictionary as the input. The elements in the dictionary are recursively evaluated.

## EnumType
This class represents an enumeration, which can take on one of a set of predefined values. It has both a 'json_serializer' and a 'load_json' function. The input accepts both strings and integers from 1 to n.

## ArrayType
This class represents a JSON array, which stores a specific type or object. Call ArrayType.factory(klass) to instantiate an array which stores elements of the class 'klass'. The ArrayType class inherits from the python list, such that it is iterable. To append a new element to the list, which is initialized from a python json structure, use the 'append_new' method. To overwrite the list, use the 'load_json' method, which assumes that the toplevel item in the input is a list.

## KeyedArrayType
This class represents a JSON array, which stores JSON objects, and is indexed by a key. The key must be an attribute of the class given in 'klass'. To instantiate, use KeyedArrayType(klass, 'abc'), where 'abc' is a string that defines the attribute of 'klass' which serves as the key. This class inherits from the python dictionary type. The 'load_json' method overwrites the dictionary from a python json struct, where the toplevel item must be a list. Items can be inserted as in a python dictionary, but the programmer must ensure that the inserted items are of the class 'klass' and the type of the key is correct.

## Defining new classes
When defining a new class, it is likely that you have to implement two methods:

- 'load_json':
This method takes a python structure which results from the output of json.loads() as its input. It must evaluate the given python structure and set the values of the python object accordingly. If your class is a basic type such as an integer, where simple assignment is enough, this method does not have to be specified. It is assumed that the 'load_json' method performs type checking on the input.

- 'json_serializer':
This method evaluates the python object and generates a python structure which can serve as an input to json.dumps(). If your class can be handled by json.dumps() this method does not have to be specified.