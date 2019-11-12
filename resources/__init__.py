import os

dir_path = os.path.dirname(os.path.realpath(__file__))

header_server = open(f'{dir_path}/header').read().encode()
body = open(f'{dir_path}/body').read().encode()
top_ports = [int(i[:-1]) for i in open(f'{dir_path}/top_ports.txt').readlines()]