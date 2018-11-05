import random


day = ["Monday", "Tuesday", "Wensday", "Thursday", "Friday", "Satuday", "Sunday"]
chan = ['M1', 'X-Sport', 'K1', 'K2', 'Football-1']
progr = ['news', 'cinema', 'sport', 'music', 'advertising']
time = ['00:00 - 02:15', '02:15 - 07:00', '07:00 - 17:00', '17:00 - 22:00', '22:00 - 00:00']

def schedule(day_of_the_week, channel):
    if day_of_the_week in day and channel in chan:
        print()
        print(channel + ': ' + day_of_the_week)
        print('=====================')
        for h in range(len(time)):
            print(progr[random.randint(0, len(progr)-1)] + ': ' + time[h])
    else:
        print('Error. Enter correct data or channel!')

day_of_the_week = input('Enter day of the week: ')
channel = input('Enter the channel: ')

schedule(day_of_the_week, channel)