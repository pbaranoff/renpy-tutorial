# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    "Ой.... Опять вставать на работу /n может нафиг оно  надо?"
    scene bg street
    show nemo at center with dissolve

    menu:
        e "Марина! Доброе утро!"
        "Пошел в жопу!":
            jump label_name1
        "Доброе утрО!":
            jump label_name2

label label_name1:
    e "Сама иди в жопу!"
    return
label label_name2:
    e "Выспалась?"
    return

    return
