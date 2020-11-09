# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



while True:
    ip = input("Введите IP-адрес: ")
    if len(ip.split(".")) == 4:
        oct1,oct2,oct3,oct4 = ip.split(".")
        if ip.replace(".", "").isdigit() and (0 <= int(oct1) <= 255
                or 0 <= int(oct2) <= 255
                or 0 <= int(oct3) <= 255
                or 0 <= int(oct4) <= 255):
            break
        else: 
            print("Неправильный IP-адрес")
    else: 
        print("Неправильный IP-адрес")
            
if 1 <= int(oct1) <= 223:
    print("unicast")
elif 224 <= int(oct1) <= 239:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
