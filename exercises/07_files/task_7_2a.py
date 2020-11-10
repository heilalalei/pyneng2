# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]
config = argv[1]
with open(config, 'r') as f:
    for line in f:
        if not line.startswith("!"): 
            ignore_flag = False
            for word in ignore:
                if word in line:
                    ignore_flag = True
            if not ignore_flag:
                print(line.rstrip())            
            
