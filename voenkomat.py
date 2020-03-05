height = int(input("Введите рост: "))
age = int(input("Введите возраст: "))
children = int(input("Сколько у вас детей? "))
study = input("Вы учитесь? ")
if (18 <= age <= 27) and (children < 2) and (study.lower() == "нет") and (height > 140):
    print("Годен :)")
    if height > 160:
        print("В танкисты")
    elif 150 <= height <= 160:
        print("В десант")
    elif 140 < height <= 149:
        print("В штаб")
    elif height < 0:
        print("Рост введен с ошибкой")
else:
    print("Не годен :(")