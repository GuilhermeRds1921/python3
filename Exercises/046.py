# Develop a program that shows on the screen a countdown
# to the fireworks burst, going from 10 to 0, 
# with 1 second delay between them.
from time import sleep
print('=' * 25)
print('|\tcountdown\t|')
print('=' * 25)
sec = 10
for i in range(0, 11):
    print(sec)
    sleep(1)
    sec -= 1
print('BOM!!!')