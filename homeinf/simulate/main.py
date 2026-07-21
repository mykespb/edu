import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Настройки окна и симуляции
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Симуляция движения частиц (атомов)")
CLOCK = pygame.time.Clock()
FPS = 60

# Цвета
BACKGROUND_COLOR = (20, 20, 30)
PARTICLE_COLOR = (0, 255, 200)

# Параметры частиц
NUM_PARTICLES = 50
PARTICLE_RADIUS = 8
MIN_SPEED, MAX_SPEED = 2, 5

class Particle:
    def __init__(self):
        # Случайное начальное положение в пределах экрана
        self.x = random.uniform(PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS)
        self.y = random.uniform(PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS)
        
        # Случайное направление и скорость
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        self.radius = PARTICLE_RADIUS
        self.mass = PARTICLE_RADIUS  # Масса пропорциональна радиусу для физики

    def move(self):
        # Обновление координат
        self.x += self.vx
        self.y += self.vy

        # Отскок от левой и правой стен
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= -1
        elif self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.vx *= -1

        # Отскок от верхней и нижней стен
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= -1
        elif self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy *= -1

    def draw(self, surface):
        # Отрисовка частицы
        pygame.draw.circle(surface, PARTICLE_COLOR, (int(self.x), int(self.y)), self.radius)

def handle_collisions(particles):
    # Проверка столкновений между всеми парами частиц
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p1 = particles[i]
            p2 = particles[j]

            # Расстояние между центрами
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            distance = math.hypot(dx, dy)

            # Если расстояние меньше суммы радиусов — произошло столкновение
            if distance < p1.radius + p2.radius:
                # Направление столкновения (нормаль)
                if distance == 0: continue # Защита от деления на ноль
                nx = dx / distance
                ny = dy / distance

                # Относительная скорость
                kx = p1.vx - p2.vx
                ky = p1.vy - p2.vy
                p = 2 * (nx * kx + ny * ky) / (p1.mass + p2.mass)

                # Обновление скоростей после упругого удара
                p1.vx -= p * p2.mass * nx
                p1.vy -= p * p2.mass * ny
                p2.vx += p * p1.mass * nx
                p2.vy += p * p1.mass * ny

                # Разведение заступивших друг за друга частиц (устранение застревания)
                overlap = (p1.radius + p2.radius) - distance
                p1.x -= nx * overlap * 0.5
                p1.y -= ny * overlap * 0.5
                p2.x += nx * overlap * 0.5
                p2.y += ny * overlap * 0.5

# Создание пула частиц
particles = [Particle() for _ in range(NUM_PARTICLES)]

# Главный цикл программы
running = True
while running:
    # Обработка событий (выход из программы)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление физики
    for particle in particles:
        particle.move()
    handle_collisions(particles)

    # Отрисовка
    SCREEN.fill(BACKGROUND_COLOR)
    for particle in particles:
        particle.draw(SCREEN)

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()

