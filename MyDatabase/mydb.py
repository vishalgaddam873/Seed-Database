import json
import os
import random

def load(filename='hello.db',autodump=False):
    MyDb = MyDatabase(filename,autodump)
    MyDb.load_file()
    return MyDb

class MyDatabase():
    json_object = {}
    def __init__(self,fileName,autodump):
        self.fileName = fileName
        self.autodump = autodump

    def load_file(self): # Here the self is object or instance 
        print("Loading database from",self.fileName)
        if os.path.exists(self.fileName):
            content = open(self.fileName).read()
            self.json_object = json.loads(content)
        else:
            with open(self.fileName,'w') as data:
                json.dump(self.json_object,data)
            content = open(self.fileName).read()
            self.json_object = json.loads(content)
        print("Databse Loaded sucessfully")
        return self.json_object

    def dump(self):
        print("Dumping databse to ",self.fileName)
        file_handler = open(self.fileName,'w')
        json_dump = json.dumps(self.json_object)
        file_handler.write(json_dump)
        file_handler.close()
        print("Database dumped sucessfully")
        print("Ok")
    
    def get(self,key):
        try:
            dic = self.load_file()
            return dic[key]
        except KeyError:
             return("Enter correct Key to access the values")

    def set(self,key,value):
        dic = self.load_file()
        dic[key] = value
        self.auto_dump()
        return dic

    def get_all(self):
        key_list = []
        dic = self.load_file()
        for i in dic.keys():
            key_list.append(i)
        return key_list

    def rem(self,key):
        dic = self.load_file()
        del dic[key]
        return dic

    def exists(self,key):
        dic = self.load_file()
        if key in dic.keys():
            return True
        else:
            return False
    
    def total_keys(self):
        key_list = []
        dic = self.load_file()
        for i in dic.keys():
            key_list.append(i)
        return len(key_list)

    def del_db(self):
        dic = self.load_file()
        dic.clear()
        print("Database sucessfully deleted")
        return dic

    def random_insert(self,number):
        dic = self.load_file()
        for i in range(number):
            random_keys = random.randint(0,10000)
            random_values = random.randint(0,10000)   
            dic[random_keys] = random_values
        self.auto_dump()
        return dic

    def auto_dump(self):
        if self.autodump:
            self.dump()

    def dmerge(self,otherDb):
        dic1 = self.load_file()
        new_object = MyDatabase(otherDb,self.autodump)
        dic2 = new_object.load_file()
        dic1.update(dic2)
        self.auto_dump()
        return "Your data merge sucessfully to "+ self.fileName