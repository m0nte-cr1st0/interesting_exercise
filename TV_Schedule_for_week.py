import random


day = ["Monday", "Tuesday", "Wensday", "Thursday", "Friday", "Satuday", "Sunday"]
chan = ['M1', 'X-Sport', 'K1', 'K2', 'Football-1']
progr = ['news', 'cinema', 'sport', 'music', 'advertising']
time = ['00:00 - 02:15', '02:15 - 07:00', '07:00 - 17:00', '17:00 - 22:00', '22:00 - 00:00']

def schedule():
    n = 1
    while n <= 3:
        for i in day:
            for j in chan:
                print(i + ': ' + j)
                print('=====================')

                for k in progr:
                    for h in range(len(time)):
                        print(progr[random.randint(0, len(progr))-1] + ': ' + time[h])
                        n += 1
                    break
                print('')


schedule()