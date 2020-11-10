# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

user_vlan = input("Введите вашу VLAN: ")
mac_table = []
with open('CAM_table.txt', 'r') as f:
    for line in f:
        words = line.split()
        for word in line.split():
            if len(word) == 14 and '.' in word:
                vlan, mac, _, intf = words
                mac_table.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(mac_table):
    if vlan == int(user_vlan):
        print(f"{vlan:<9}{mac:20}{intf}")

