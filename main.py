import os

class Reading:
    def __init__(self,file):
        if os.path.exists(file)==True and os.path.isfile(file)==True:#обычно не пишут True
            self.__file = os.path.abspath(file)# храним файл, абсолютный путь  #os.path.abspath(file) храним абсолютный путь
            self.__ext = os.path.splitext(file)[1]# splitext делит на расширение и на базовую часть # храним расширение
        else:
            raise FileNotFoundError # вызываем ошибку

    file=property()
    ext=property()
    @file.getter
    def file(self):
        return self.__file
    @file.setter
    def file(self,new_file):
        self.__file = new_file
        if os.path.exists(new_file) and os.path.isfile(new_file):#обычно не пишут True
            self.__file = os.path.abspath(new_file)# храним файл, абсолютный путь  #os.path.abspath(file) храним абсолютный путь
            self.__ext = os.path.splitext(new_file)[1]# splitext делит на расширение и на базовую часть # храним расширение
        else:
            raise FileNotFoundError # вызываем ошибку
    @ext.getter
    def ext(self):
        return self.__ext

    def read(self,size=1024):
        if self.ext== '.json':
            import json
            with open(self.file) as fr:#контексный менеджер
                data=json.load(fr) #json.load(fr) создаёт json  объект из json файла
                for i in data:
                    yield i
        elif self.ext == '.csv':
            import csv
            with open(self.file) as fr:  # контексный менеджер
                data = csv.reader(fr)  # csv.reader(fr) создаёт csv  объект из csv файла
                while block := data.read(size):#конкатенация оператора присваивая и обращения
                    yield block
        else:
            with open(self.file) as fr:
                while block := fr.read(size):
                    yield block
    def __enter__(self):# то что нужно сделать перед входом в контекстный менеджер
        self.handle=open(self.file)
        return self.handle
    def __exit__(self, exc_type, exc_val, exc_tb):# при выходе из контекстного менеджера,если не закрывать ,то будет утечка памяти
        self.handle.close()
        return True
    def __add__(self, other):#суммируем 2 файла
        with open(f"{os.path.dirname(self.file)}\\{(k:=os.path.basename(self.file))[:k.rfind('.')]}\\{(k:=os.path.basename(other.file))[:k.rfind('.')]}",'w') as fw:
            with open(self.file) as fr:
                for i in fr.readlines():
                    fw.write(f'{i.strip()}\n')
            with open(other.file) as fr:
                for i in fr.readlines():
                    fw.write(f'{i.strip()}\n')
        self.file= f"{os.path.dirname(self.file)}\\{(k:=os.path.basename(self.file))[:k.rfind('.')]}\\{(k:=os.path.basename(other.file))[:k.rfind('.')]}"



    # @property #превращает метод в свойство
    # def method(self):
    #     pass








