mems = {
    "Чувааак": 'Надо просто понять',
    "Кери": "Основной игрок",
    "Сигмабой": "Вообще классный чувак!",
    "Меганайт": "Человек с неопределенной ориентацией"
}

add = input("Введите слово для перевода: ")
if add in mems:
    print(mems.get(add))
else:
    print("Иди проспись!")
