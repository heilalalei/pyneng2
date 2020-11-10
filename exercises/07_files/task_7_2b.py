# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]
config = argv[1]
with open(config, 'r') as src, open('config_sw1_cleared.txt', 'w') as dst:
    for line in src:
        ignore_flag = False
        for word in ignore:
            if word in line:
                ignore_flag = True
        if not ignore_flag:
            dst.write(line)            
            
