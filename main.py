# імпортуємо модуль pygame
import pygame
# імпортуємо модуль os 
import os
#імпортуємо клас Image з модуля image
from image import Image
#імпортуємо клас Player з модуля player
from player import Player
#Налаштували pygame для роботи із системою 
pygame.init()

#
#УМОВНІ ПОЗНАЧЕННЯ:
# 0 - це порожня клітинка
# 1 - блок землі
list_map = [
    '0000000000000000000000',
    '0000000000000000000001',
    '1121000000000001000010',
    '0000001001112100111000',
    '0000111110300000000100',
    '0001000000300000000001',
    '0100000000311110001111',
    '0010000001000000100000',
    '1111111100000011010000',
    '0000000010011000001100',
    '0010000000100000000001',
    '1100111111111111111111',
]

# list_map = [
#     '0000000000000000000000',
#     '0000000000000000000000',
#     '0000000000000000000000',
#     '0000000000000000000000',
#     '0000000000000000000000',
#     '0000000000000000000000',
#     '0000000000000000000000',
#     '0000000000000000000000',
#     '0000000000001100000000',
#     '0000000000000001100000',
#     '0000000011000000000000',
#     '0000011000000000000000',
# ]

# 
blocks_coordinats = [] # [x_left, y_top, x_right, y_bottom]
#створюємо список blocks_objects
blocks_objects = []
#створюємо змінні х і у
x = 0
y = 0
#перебираємо кожен елемент в списку list_map
for row in list_map:
    #перебираємо кожену цифру в кожномму елементі в списку
    for cell in row:
        #якщо цифра дорівнює 1
        if cell == '1':
            #вказуємо шлях та кординрати до блоку
            block = Image('images/blocks/1.png', 60, 60, x, y)
            #додати блок в список blocks_objects
            blocks_objects.append(block)
        #якщо цифра дорівнює 2
        elif cell == '2':
            #вказуємо шлях та кординрати до блоку
            block = Image('images/blocks/2.png', 60, 60, x, y)
            #додати блок в список blocks_objects
            blocks_objects.append(block)
        #якщо цифра дорівнює 3
        elif cell == '3':
            #вказуємо шлях та кординрати до блоку
            block = Image('images/blocks/3.png', 60, 60, x, y)
            #додати блок в список blocks_objects
            blocks_objects.append(block)
        #якщо цифра дорівнює 4
        elif cell == '4':
            #вказуємо шлях та кординрати до блоку
            block = Image('images/blocks/4.png', 60, 60, x, y)
            #додати блок в список blocks_objects
            blocks_objects.append(block)
        # умова якщо клітинка не = нулю то:
        if cell != '0':
            # додаємо кординати блока
            blocks_coordinats.append([x,y,x+60, y+60])
        # додати до х 60
        x += 60
    #обнуляємо х до у додаємо 60
    x = 0
    y += 60


#словник, в якому знаходяться налаштування ігрового вікна 
window_settings = {
    'width': 1320,#ширина вікна
    'height': 720,#висота вікна
    'caption':'Платформер'#назва(заголовок) вікна
}

#створ. об'єкт для можливості відслідковувати час, працювати із ним
clock = pygame.time.Clock()
#створ. об'єкт спрайта(гравця), вказуємо його розміри, координати, швидкість, швидкість, з якою гравець буде падати 
object_player = Player('images/player/stay.png', 90, 105, 500, 00, 5,5)
# створюємо задній фон
background = Image('images/bg.png',window_settings['width'], window_settings['height'], 0, 00)
#створ. об'єкт спрайта(монети), вказуємо його розміри та коодинати
money = Image('images/coin.png', 60, 60, 1240, 0)
# вказуємо розміри екрану
window = pygame.display.set_mode((window_settings['width'], window_settings['height']))
#створюємо заголовок 
pygame.display.set_caption(window_settings['caption'])
# Змінна, що відповідає за роботу гри
game = True
# поки гра запущена
while game == True:
    # заливка вікна 
    # window.fill((0, 233, 255))
    #відображаємо задній фон та монету
    background.show_image(window)

    #переюираємо блоки в змінній blocks_objects
    for block in blocks_objects: 
        #відобразити блоки
        block.show_image(window)
    #відобразити монетку
    money.show_image(window)
    #через змінну об'єкта спрайта звертаємося до самої картинки спрайта і відображаємо її
    object_player.image_player.show_image(window)
    #викликаємо метод sprite_move, щоб спрайт міг рухатись
    object_player.sprite_move()
    #викликаємо метод gravitation, щоб спрайт міг падати вниз
    object_player.gravitation(window_settings)
    #викликаємо метод jump, щоб спрайт міг стрибати
    object_player.jump()
    #додаємо колізії блоків
    object_player.collision_top_block(blocks_coordinats)
    object_player.collision_bottom_block(blocks_coordinats)
    
    # перебираємо події
    for event in pygame.event.get():
        # якщо подія це вийти з гри то
        if event.type == pygame.QUIT:
            # вимнкути гру
            game = False
    # постійне оновлення екрану
    pygame.display.flip()
    #задаємо кількість кадрів за 1 секунду 
    clock.tick(60)
    
