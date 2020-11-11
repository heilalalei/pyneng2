# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""

import ipaddress

def convert_ranges_to_ip_list(ip_ranges):
    ip_list = []
    for ip_range in ip_ranges:
        if not "-" in ip_range:
            ip_list.append(ip_range)
        else:
            if len(ip_range.split("-")[1]) <= 3:
                last_oct_last_ip = int(ip_range.split("-")[1])
            else:
                last_oct_last_ip = int((ip_range.split("-")[1]).split(".")[-1])
            last_oct_first_ip = int(ip_range.split("-")[0].split(".")[-1])
            first_three_octets = ".".join(ip_range.split("-")[0].split(".")[:-1])
            local_list = [first_three_octets+f".{ip}" for ip in range(last_oct_first_ip, last_oct_last_ip+1)]
            ip_list.extend(local_list)

    print(ip_list)
    return ip_list        

if __name__ == '__main__':
    ip_ranges = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    convert_ranges_to_ip_list(ip_ranges)

