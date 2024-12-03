import os

def announce_ram():
    ram_info = os.popen('free -m').read()
    return ram_info

print(announce_ram())