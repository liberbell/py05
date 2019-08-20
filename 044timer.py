import time

run = input('Start? >')

second = 0
if run == 'yes':
    while second != 10:
        print('>', second)
        time.sleep(1)
        second += 1
    print('>', second)
