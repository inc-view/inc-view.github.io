import os
import psutil
import time

cor = {
    'verde': "\033[92m",
    'amarelo': "\033[93m",
    'vermelho': "\033[31m",
    'branco': "\033[0m"
}

cont = 0
cpu_historico = []
ram_historico = []
cpu_soma = 0
ram_soma = 0

while True:
    os.system('cls')

    cpu_use = psutil.cpu_percent()
    partitions = psutil.disk_partitions()
    disk_use_list = []
    disk_bar = []

    for (k, part) in enumerate(partitions):
        disk_use_list.append(psutil.disk_usage(part.device))
        if (disk_use_list[k].percent <= 70):
            disk_bar.append(cor['verde'] + "|")
        elif (disk_use_list[k].percent <= 90):
            disk_bar.append(cor['amarelo'] + "|")
        else:
            disk_bar.append(cor['vermelho'] + "|")

    ram_use = psutil.virtual_memory()
    cpu_bar = ""
    if (cpu_use <= 70):
        cpu_bar = cor['verde'] + "|"
    elif (cpu_use <= 90):
        cpu_bar = cor['amarelo'] + "|"
    else:
        cpu_bar = cor['vermelho'] + "|"

    ram_bar = ""
    if (ram_use.percent <= 70):
        ram_bar = cor['verde'] + "|"
    elif (ram_use.percent <= 90):
        ram_bar = cor['amarelo'] + "|"
    else:
        ram_bar = cor['vermelho'] + "|"

    for i in range(51):
        if (cpu_use <= i*2):
            cpu_bar += " "
        else:
            cpu_bar += "="
        
        for (k, disk_use) in enumerate(disk_use_list):
            if (disk_use.percent <= i*2):
                disk_bar[k] += " "
            else:
                disk_bar[k] += "="

        if (ram_use.percent <= i*2):
            ram_bar += " "
        else:
            ram_bar += "=" 

    cpu_bar += "|" + cor['branco']          
    ram_bar += "|" + cor['branco']  

    for (k,disk) in enumerate(disk_use_list):         
        disk_bar[k] += "|" + cor['branco']         

    print('CPU: ' + str(cpu_use) + ' %\n' + cpu_bar)
    print('\nRAM: ' + str(round(ram_use.used / 1000000000, 2)) + '/' + str(round(ram_use.total / 1000000000,2)) +' GB\n' + ram_bar)
    
    for (k,disk) in enumerate(disk_use_list):         
        print('\n' + partitions[k].device + ': ' +str(round(disk.used / 1000000000, 2))+ '/' +str(round(disk.total / 1000000000, 2))  + ' GB\n' + disk_bar[k])

    cpu_soma += cpu_use
    ram_soma += ram_use.percent
    cont += 1
    if (cont >= 30):
        cpu_historico.append(cpu_soma / 30)
        ram_historico.append(ram_soma / 30)
        cpu_soma = 0
        ram_soma = 0
        cont = 0
    print('\nHistórico: ')
    print('CPU: ', cpu_historico)
    print('RAM: ', ram_historico)
    time.sleep(1)