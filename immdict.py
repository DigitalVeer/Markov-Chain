from copy import deepcopy

class ImmDict:

    def __init__(self, dict = {}):
        self.__dict = dict


    def put(self, key, val):
        new_dict = deepcopy(self.__dict)
        new_dict[key] = val
        updated_dict = ImmDict(new_dict)
        return updated_dict


    def get(self, key):
        try:
            return self.__dict[key]
        except:
            return None

    def keys(self):
        return [key for key in self.__dict]

    def values(self):
        return [val for key, val in self.__dict.items()]
