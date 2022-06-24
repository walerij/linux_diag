#информация об операционной системе
import os
print("Система:"+os.name)
print("Логин:"+os.getlogin() )
print("Количество CPU:"+str(os.cpu_count()))
print(os.get_terminal_size())
print(os.getpid())
