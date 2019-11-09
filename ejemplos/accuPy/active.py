from MMA8452 import *
import time
acc=MMA8452()
print(acc.isActive())
time.sleep(1)
acc.active()
time.sleep(1)
print(acc.isActive())
time.sleep(1)
acc.standby()
time.sleep(1)
print(acc.isActive())
while True:
    print(acc.read())
    time.sleep(0.3)