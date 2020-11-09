# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

subnet = argv[1]
ip = subnet.split("/")[0]
mask = int(subnet.split("/")[1])
bin_mask = "1" * mask + "0" * (32-mask)

ip_oct_list = ip.split(".")

ip_bin = "{:08b}{:08b}{:08b}{:08b}".format(int(ip_oct_list[0]),
                                            int(ip_oct_list[1]),
                                            int(ip_oct_list[2]),
                                            int(ip_oct_list[3]))
                                            
ip_bin = ip_bin[:mask] + "0" * (32-mask)

oct1,oct2,oct3,oct4 = [int(ip_bin[:8], 2),
            int(ip_bin[8:16], 2),
            int(ip_bin[16:24], 2),
            int(ip_bin[24:32], 2),
            ]

m1,m2,m3,m4 = [int(bin_mask[:8], 2),
            int(bin_mask[8:16], 2),
            int(bin_mask[16:24], 2),
            int(bin_mask[24:32], 2),
            ]

ip_template = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_template = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""
 
print(ip_template.format(oct1,oct2,oct3,oct4))
print(mask_template.format(mask,m1,m2,m3,m4))
