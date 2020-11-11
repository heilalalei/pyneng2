# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

def ping_ip_addresses(ip_addresses):
    available_ip = []
    unavailable_ip = []
    for ip in ip_addresses:
        if not subprocess.run(['ping', f'{ip}', '-c', '1'],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL,).returncode:
            available_ip.append(ip)
        else: 
            unavailable_ip.append(ip)
    
    return available_ip, unavailable_ip

if __name__ == '__main__':
    ping_ip_addresses(['8.8.8.8','10.1.1.1','8.8.4.4','10.2.2.2'])
