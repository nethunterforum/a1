import os
import sys
"""
with open('result1.txt', 'a') as file:
    file.write('start\n')
file.close()
with open('a.txt') as f:
    for line in f:
        os.system('python ex.py http://'+line.strip('\n'))
        with open('result1.txt', 'a') as file:
            file.write(line.strip('\n')+'\n')
        file.close()
with open('result1.txt', 'a') as file:
    file.write('fin\n')
file.close()
"""
with open('result2.txt', 'a') as file:
    file.write('start\n')
file.close()
with open('aa.txt') as f:
    for line in f:
        os.system('python ex.py http://'+line.strip('\n'))
        with open('result1.txt', 'a') as file:
            file.write(line.strip('\n')+'\n')
        file.close()
with open('result1.txt', 'a') as file:
    file.write('fin\n')
file.close()
