#!/usr/bin/python3

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return __objects
    
    def new(self, obj):
        key = "{}{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            d = {k:v.to_dict for k, v in FileStorage.__objects.items()}
            json.dump(d, json_file)
    
    def reload(self):
        if __file_path:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as json_file:
                