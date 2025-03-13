import pygame
import time


pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")


clock_img = pygame.image.load(r"C:\Users\Глазков Артем\PycharmProjects\PythonProject2\.venv\share\mickeyclock.PNG.png")
clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))  


minute_hand = pygame.image.load(r"C:\Users\Глазков Артем\PycharmProjects\PythonProject2\.venv\share\mickeyclock hand.png")   
second_hand = pygame.image.load(r"C:\Users\Глазков Артем\PycharmProjects\PythonProject2\.venv\share\mickeyclockk.png") 


CENTER = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_img, (0, 0))  

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

   
    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)

    
    minute_rect = rotated_minute.get_rect(center=CENTER)
    second_rect = rotated_second.get_rect(center=CENTER)

    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.flip() 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
