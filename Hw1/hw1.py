from abc import ABC, abstractmethod
import json
import pickle


class SerializationInterface(ABC):

    @abstractmethod
    def serializ(self, data, file_name):
        pass


# _________________________________________________________
class SerializationBin(SerializationInterface):  # bin

    def serializ(self, data, file_name):
        with open(file_name, 'wb') as fh:
            pickle.dump(data, fh)


class SerializationJson(SerializationInterface):  # json

    def serializ(self, data, file_name):
        with open(file_name, 'w') as fh:
            json.dump(data, fh)


# _________________________________________________________

if __name__ == '__main__':
    json_file = 'jsonfile.json'
    bin_file = 'binfile.bin'

    list_data = [1, 2, 3]
    dict_data = {1: 'a', 2: 'b'}
    tuple_data = (4, 5, 6)
    set_data = {7, 8, 9}
    # _________________________________________________________
    '''Сериализация json файла'''
    data_json_dict = SerializationJson()
    data_json_dict.serializ(dict_data, json_file)
    # _________________________________________________________

    # _________________________________________________________
    '''Сериализация bin файла'''
    data_bin_set = SerializationBin()
    data_bin_set.serializ(set_data, bin_file)
    # _________________________________________________________
