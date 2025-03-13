import pygame
import time

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Загрузка фона (Микки Маус)
clock_img = pygame.image.load(r"C:\Users\Глазков Артем\PycharmProjects\PythonProject2\.venv\share\mickeyclock.PNG.png")
clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))  # Подгоняем размер

# Загрузка рук (замени на нужные файлы)
minute_hand = pygame.image.load(r"C:\Users\Глазков Артем\PycharmProjects\PythonProject2\.venv\share\mickeyclock hand.png")   # Левая рука (минутная стрелка)
second_hand = pygame.image.load(r"C:\Users\Глазков Артем\PycharmProjects\PythonProject2\.venv\share\mickeyclockk.png")  # Правая рука (секундная стрелка)

# Указываем центр вращения
CENTER = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    screen.fill((255, 255, 255))  # Белый фон
    screen.blit(clock_img, (0, 0))  # Отображаем фон с Микки Маусом

    # Получаем текущее время
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Вычисляем угол поворота (минутная -6° за минуту, секундная -6° за секунду)
    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    # Вращаем руки
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)

    # Получаем прямоугольник для центрирования
    minute_rect = rotated_minute.get_rect(center=CENTER)
    second_rect = rotated_second.get_rect(center=CENTER)

    # Отображаем руки-стрелки
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.flip()  # Обновляем экран

    # Проверка на выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
