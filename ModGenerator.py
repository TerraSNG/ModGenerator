# #!/usr/bin/python3.8
import os
import sys
from shutil import copyfile
from termcolor import colored

print(colored('''
 
███    ███  ██████  ██████   ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
████  ████ ██    ██ ██   ██ ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██ ████ ██ ██    ██ ██   ██ ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
██  ██  ██ ██    ██ ██   ██ ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██      ██  ██████  ██████   ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
                                                                                                         
                                                                                                         
                                                                                                                              
                                                    сделано в Terraria-SNG с <3                                                                               
''','magenta'))

def coderun():
    z = 0
    x = 0
    c = 0
    v = 0
    erz = None
    erx = None
    erc = None
    erv = None

cred()
    try:
        Mn = raw_input("Напишите название мода (Без пробелов и специальных символов!): ")
        Mn = Mn.translate(None, ' \\/":.,><`~!@#$%^&?;*+=')
        if not Mn:
            raise ValueError
        else:
            z = 1
    except ValueError:
        erz = "Название мода"
    
    try:
        Md = raw_input("Напишите имя мода: ")
        if not Md:
            raise ValueError
        else:
            x = 1
    except ValueError:
        erx = "Имя мода"

    try:
        It = raw_input("Название первого предмета (Без пробелов и специальных символов!): ")
        It = It.translate(None, ' \\/":.,><`~!@#$%^&?;*+=')
        if not It:
            raise ValueError
        else:
            c = 1
    except ValueError:
        erc = "Название первого предмета+"
    
try:
        MA = raw_input("Напишите имя автора: ")
        if not MA:
            raise ValueError
        else:
            v = 1
    except ValueError:
        erv = "Ваше имя"
    b = z + x + c + v
    if b == 4:
        try:
            os.makedirs(os.path.join("Вызод", Mn, "Предметы"))
        except OSError:
            print "Dir exists - skipping."

        copyfile("Templates/Items/itemname.png", os.path.join("Output", Mn, "Items", It + ".png"))
        copyfile("Templates/modname.csproj.user", os.path.join("Output", Mn, Mn + ".csproj.user"))
        
        bldr = open(os.path.join("Шаблоны", "build.txt")).read()
        bldr = bldr.replace('{username}', MA).replace('{displayname}', Md)
        build = open(os.path.join("Выход", Mn, "build.txt"), "w")
        build.write(bldr)
        
        dscr = open(os.path.join("Шаблоны", "description.txt")).read()
        dscr = dscr.replace('{displayname}', Md)
        desc = open(os.path.join("Выход", Mn, "description.txt"), "w")
        desc.write(dscr)

        Itcr = open(os.path.join("Шаблоны", "Предметы", "itemname.cs")).read()
        Itcr = Itcr.replace("{modname}", Mn).replace("{itemname}", It)
        Itcs = open(os.path.join("Выход", Mn, "Предметы", It + ".cs"), "w")
        Itcs.write(Itcr)

        mncr = open(os.path.join("Шаблоны", "modname.cs")).read()
        mncr = mncr.replace('{modname}', Mn)
        mncs = open(os.path.join("Выход", Mn, Mn + ".cs"), "w")
        mncs.write(mncr)

        mnpr = open(os.path.join("Шаблоны", "modname.csproj")).read()
        mnpr = mnpr.replace('{modname}', Mn)
        mnpj = open(os.path.join("Выход", Mn, Mn + ".csproj"), "w")
        mnpj.write(mnpr)
    else:
        cred()
        print "ОШИБКА!!! |Следующие поля пусты.\n-----------------------------------"
        if z != 1:
            print erz
        if x != 1:
            print erx
        if c != 1:
            print erc
        if v != 1:
            print erv
        print ""

def cred():
    clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
    clear()
    print "TModloader Mod Generator\n\nСоздан в Terra-SNG.\n."
    print "--------------------------------------------------------------------------\n"

def FC():
    BaseFileCheck = ['build.txt', 'description.txt', 'modname.cs', 'modname.csproj', 'modname.csproj.user']
    ItemsFileCheck = ['itemname.cs', 'itemname.png']
    cred()
    try:
        for x in BaseFileCheck:
            if not os.path.isfile(os.path.join("Шаблоны", x)):
                raise IOError
        for x in ItemsFileCheck:
            if not os.path.isfile(os.path.join("Шаблоны", "Предметы", x)):
                raise IOError
    except IOError:
        print "В папке templates отсутствует один или несколько файлов. Генератор не может продолжать работу.\n"
        raw_input("Нажмите 'enter' чтоб закрыть окно.")
        sys.exit(0)

while True:
    FC()
    coderun()
    while True:
        lsg = raw_input("Хотели бы вы создать еще один скелет? Введите "y", в противном случае "n", чтобы закрыть.. ")
        if lsg.lower() == 'y':
            break
        elif lsg.lower() == 'n':
            sys.exit(0)
        else:
            print "Недопустимая команда. Чтобы создать другой скелет, введите "y", в противном случае "n", чтобы закрыть.\n"
