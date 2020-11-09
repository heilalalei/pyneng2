# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

access_template.append("номер VLAN")
trunk_template.append("разрешенные VLANы")

mode = input("Введите режим работы интерфейса (access/trunk): ")
intf = input("Введите тип и номер интерфейса: ")

config_dict = {
    "access": access_template,
    "trunk": trunk_template
    }
    
vlan = input("Введите {}: ".format(config_dict[mode][-1]))
access_template.remove("номер VLAN")
trunk_template.remove("разрешенные VLANы")

config_dict[mode].insert(0, "interface {}".format(intf))
result = "\n".join(config_dict[mode])


print()
print(result.format(vlan))
