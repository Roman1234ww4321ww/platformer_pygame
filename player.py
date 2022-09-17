import os
import pygame
from image import Image
class Player:
    #конструктор класу, куди передаємо необхідні аргументи
    def __init__(self, image_path, width, heigth, x, y, speed, speed_gravitation):
        #створ. об'єкт картинки гравця
        self.image_player = Image(image_path, width, heigth, x, y)
        #швидкість руху
        self.speed = speed
        #змінна, в якій зберіг. індекс кожного спрайта(в даній ситуац. присвоюємо змінній індекс першого спрайта)
        self.number_of_costume = 1
        #лічильник для контролю швидкості спрайта; задаємо лічильнику початкове значення 
        self.count_animation = 1
        #напрямок віддзеркаленого зображення(присвоюємо цій змінній значення False)
        self.flip_direction = False
        #швидкість гравітвції(швидкість, з якою гравець буде падати) 
        self.speed_gravitation = speed_gravitation
        #змінна, яка відповідає за те, чи відбувається стрибок(в дан. ситуац. змінна має значення False, тому стрибок не відбувається)
        self.is_jump = False
        #швидкість, з якою гравець буде стрибати 
        self.speed_jump = 10
        #лічильник для стрибка
        self.count_jump = 0
        #зупинка гравітації (стоїть за умовченням викл, тобто гравітація надалі працює)
        self.stop_gravitation = False

    #метод(функція) для руху спрайта 
    def sprite_move(self):
                      
        #отримуємо клавіші, які ми натиснули
        keys = pygame.key.get_pressed()
        #якщо натиснута клавіша вправо
        if keys[pygame.K_RIGHT]:
            #задаємо швидкість координаті х в додатньому напрямку (тобто змушуємо спрайт рухатись вправо)
            self.image_player.x += self.speed
            #задаємо змінній значення False, тобто не змінюємо напрямок 
            self.flip_direction = False
            #викликаємо метод animation
            self.animation()
        #якщо натиснута клавіша вліво
        elif keys[pygame.K_LEFT]:
            #задаємо швидкість координаті х у від'ємному напрямку (тобто змушуємо спрайт рухатись вліво)
            self.image_player.x -= self.speed
            #задаємо напрямок віддзеркаленому зображенню 
            self.flip_direction = True
            #викликаємо метод animation для анімації спрайта
            self.animation()
        #якщо не натиснута ніяка клавіша 
        else:
            #створ. шлях до відповідної картинки спрайта
            self.image_player.image_path = 'images/player/stay.png'
            #завантажуємо зображення із належним напрямком
            self.image_player.load_image(direction=self.flip_direction)
    #функція(метод) для анімації спрайта
    def animation(self):
        #об'єднуємо шлях до кожного спрайта із його індексом(створ. повний шлях до кожного спрайта)
        self.image_player.image_path = f'images/player/{self.number_of_costume}.png'
        #викликаємо функцію load_image відносно спрайта
        self.image_player.load_image(direction=self.flip_direction)
        #збільшуємо значення лічильника на одиницю
        self.count_animation += 1
        #якщо знач. лічильника дорів. 5 
        if self.count_animation == 5:
            #змінюємо індекс спрайта на наступний 
            self.number_of_costume += 1
            #якщо індекс спрайта більше або дорів. 7 
            if self.number_of_costume >= 7:
                #задаємо індекс першого спрайта
                self.number_of_costume = 1
            #задаємо початкове значення лічильника 
            self.count_animation = 1
    #функція(метод) для того, щоб гравець міг падати вниз
    def gravitation(self, window_settings):
        #якщо гравець не торкається до нижньої сторони ігрового вікна
        if self.image_player.y + self.image_player.height <= window_settings['height'] and self.stop_gravitation == False:
            #змушуємо гравця падати вниз
            self.image_player.y += self.speed_gravitation
            #створ. шлях до певної картинки спрайта
            self.image_player.image_path = 'images/player/down.png'
            #завантажуємо зображення із належним напрямком
            self.image_player.load_image(direction=self.flip_direction)
        #якщо гравець все ж торкається до нижньої сторони вікна
        else:
            #задаємо лічильнику значення 25, щоб гравець міг в майбутньому стрибнути 
            self.count_jump = 25
            #стрибок не відбувається
            self.is_jump = False
    #функція(метод) для того, щоб гравець міг стрибати 
    def jump(self):
        #отримуємо клавіші, які ми натиснули 
        keys = pygame.key.get_pressed()
        #якщо натиснута клавіша пробіл або клавіша зі стрілкою вгору
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            #срибок відбувається 
            self.is_jump = True
        #якщо відбувається стрибок
        if self.is_jump:
            #якщо значення лічильника більше нуля 
            if self.count_jump > 0:
                #гравець стрибає вгору
                self.image_player.y -= self.speed_jump
                #зменшуємо значення лічильника на одиницю
                self.count_jump -= 1
                #створ. шлях до необхідного костюму спрайта
                self.image_player.image_path = 'images/player/up.png'
                #завантажуємо костюм(зображення) із належним напрямком  
                self.image_player.load_image(direction=self.flip_direction)
    # функція колізія верха блока
    def collision_top_block(self, blocks_coordinats):
        #[x_left, y_top, x_right, y_bottom]
        # напевне ми тут знаходим кординати блока
        for cor in blocks_coordinats:
            # умова якщо ми бачимо що кординати гравця ніг торкаються кординати верха блоки то:
            if self.image_player.y + self.image_player.height >= cor[1] and self.image_player.y + self.image_player.height <= cor[1] + self.speed_gravitation and self.image_player.x + self.image_player.width >= cor[0] and self.image_player.x <= cor[2]:
                #то зупиняєм гравітацію
                self.stop_gravitation = True
                #зупинити процес
                break
            else:
                #в іншому випадку гравітація працюватиме надалі
                self.stop_gravitation = False
    #функція колізія низу блока
    def collision_bottom_block(self, blocks_coordinats):
        #напевне ми тут знаходим кординати блока
        for cor in blocks_coordinats:
            #умова якщо кордината голови гравця торкається кординати низу блока то:
            if self.image_player.y <= cor[3] and self.image_player.y >= cor[3] - self.speed_jump and self.image_player.x + self.image_player.width >= cor[0] and self.image_player.x <= cor[2]:
                #зупиняємо або обнуляємо стибок
                self.count_jump = 0
                #зупинити процес
                break

                