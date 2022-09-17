import os
import pygame

# створюємо клас для зображень
class Image:
    def __init__(self, image_path, width, height, x, y):
        #створюєио змінну image_path, яка відповідає за відносний шлях до картинки у папці проекту
        self.image_path = image_path
        #створюємо змінні ширина і висота
        self.width = width
        self.height = height
        #створюємо змінні координат
        self.x = x
        self.y = y
        #викликаємо метод load_image, який відповідає за завантаження зображення
        self.load_image()
        
    # створюємо функцію для показу зображеннь
    def show_image(self, window):
        # показати картинку
        window.blit(self.scaled_image, (self.x, self.y))
    #створ. функцію для завантаження зображення і вказуємо, що за замовчуванням зображення нарямку не має
    def load_image(self, direction = False):
        # знайти шлях до папку проекту
        self.project_folder_path = os.path.abspath(__file__ + '/..')
        # знайти абсолютний шлях до зображення
        self.absolute_image_path = os.path.join(self.project_folder_path, self.image_path)
        # загрузити картинку за шляхом
        self.loaded_image = pygame.image.load(self.absolute_image_path)
        # відзеркалюємо завантажене зображення і вказуємо, що воно по коордтинаті x має напрямок, а по координаті y не має напрямку 
        self.flipped_image = pygame.transform.flip(self.loaded_image, direction, False)
        # задаємо розміри зображенню
        self.scaled_image = pygame.transform.scale(self.flipped_image, (self.width, self.height))