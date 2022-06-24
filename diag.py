#информация об операционной системе
import os
import platform
print("Система:"+os.name)
print("Операционная система:")
print (platform.uname())
print("Логин:"+os.getlogin() )
print("Количество CPU:"+str(os.cpu_count()))

