#Задано текущее время (в часах) и количество часов, через которое должен сработать таймер. Определить 
#время, в которое сработает таймер.
def timer(hours, hours_on_the_timer):
    set_hours = (hours + hours_on_the_timer) % 24 #сколько часов будет на таймере
    print()

    if hours < 0 or hours > 24: #проверка введеного времени
        print('Вы ввели неверное время')
    else:
        if set_hours < 10: #условие для красивого вывода в стиле hh:mm
            print('Таймер сработает в 0' + str(set_hours) + ':00')
        else:
            print('Таймер сработает в ' + str(set_hours) + ':00')
    # узнаем какой день (если переходит за 24 - то 1)
    if hours + hours_on_the_timer >= 24:
        set_days = (hours + hours_on_the_timer) // 24
        print('Пройдёт {} дня(-ей).'.format(set_days))

hours = int(input('Введите текущее время, часы (от 0 до 24):''\n')) #исходные данные, часы
print()
hours_on_the_timer = int(input('Введите количество часов для срабатывания таймера:''\n')) #исходные данные, сколько часов нужно выставить

timer(hours, hours_on_the_timer)