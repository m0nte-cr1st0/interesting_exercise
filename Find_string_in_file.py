# Напишите программу, которая запрашивает у пользователя имя файла, затем открывает указанный файл и осуществляет поиск строк вида
# X-DSPAM-Confidence:    0.8475
# Продсчитывает количество этих строк и извлекает число с плавающей точкой из каждой такой строки, вычисляет среднее значение и выводит его на экран.

fname = input("Enter file name: ")
fh = open(fname)

average = []

for line in fh:
    try:
    #Проверяем окончивается ли строка на число
        digit = float(line[line.rfind(' ')+1:])
        if line.startswith("X-DSPAM-Confidence:") and digit: 
            average.append(digit)
    
    #Обрабатываем исключение, если строка оканчивается не на число
    except ValueError:
        continue

print("Average spam confidence:", round((sum(average) / len(average)), 12))