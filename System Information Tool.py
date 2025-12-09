import platform
import psutil

print("CPU:", psutil.cpu_percent())
print("RAM:", psutil.virtual_memory().percent)
print("Disk:", psutil.disk_usage('/').percent)
print("OS:", platform.system(), platform.release())
