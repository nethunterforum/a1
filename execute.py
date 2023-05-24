import os

with open('result1.txt', 'a') as file:
    file.write('start\n')
file.close()
with open('a.txt') as f:
    for line in f:
        os.system('python3.8 papercut.py http://'+line.strip('\n'))
        with open('result1.txt', 'a') as file:
            file.write(line.strip('\n')+'\n')
        file.close()
with open('result1.txt', 'a') as file:
    file.write('fin\n')
file.close()
with open('a1.txt') as f:
    for line in f:
        os.system('python3.8 papercut.py http://'+line.strip('\n'))
        with open('result2.txt', 'a') as file:
            file.write(line.strip('\n')+'\n')
        file.close()
with open('result2.txt', 'a') as file:
    file.write('fin\n')
file.close()
