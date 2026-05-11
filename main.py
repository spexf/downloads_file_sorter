from os import listdir, path
import json
import shutil
from string import ascii_letters, digits
import random
import time

f = open('./format.json')
f_json = json.load(f)
parent_dir = "C:\\Users\\[ur username]\\Downloads"


class Sorter:
    def __init__(self) -> None:
        self.file = listdir(parent_dir)
        
    def grouping(self):
        old_file = self.file
        if old_file == self.file:
            self.get_dir()
        dat = []
        for i in self.file:
            if len(i) > 1:
                dat.append({
                    'file_name': self.getting_file_format(i)['name'],
                    'file_format': self.getting_file_format(i)['format'],
                    'file_base': i
                })
            else:
                pass
        for x in dat:
            if x['file_format'] == '':
                dat.remove(x)
        return dat
        
    def getting_file_format(self, file):
        file_name, file_extension = path.splitext(file)
        return {'name':file_name,'format':file_extension}
    
    def moving_file(self):
        data = self.grouping()
        for i in data:
            for key, value in f_json['file_format'].items():
                if i['file_format'] in value:
                    location = key
                    check = f"{parent_dir}\\{location}\\{i['file_format']}\\{i['file_name']}{i['file_format']}"
                    if path.exists(check):
                        shutil.move(f"{parent_dir}\\{i['file_base']}", f"{parent_dir}\\{location}\\{i['file_format']}\\{i['file_name']}_{self.randomString(10)}_{i['file_format']}")
                    else:
                        shutil.move(f"{parent_dir}\\{i['file_base']}", f"{parent_dir}\\{location}\\{i['file_format']}\\{i['file_name']}{i['file_format']}")
                else:
                    pass
        return 'success'
    
    def randomString(self,ct):
        char = ascii_letters + digits
        randomed = ''
        for i in range(ct):
            randomed += char[random.randrange(len(char))]
        return randomed
    
    def get_dir(self):
        self.file = listdir(parent_dir)
        return '200 - OK'
sorter = Sorter()
while True:
    print(sorter.moving_file())
    time.sleep(60)
