from vpython import canvas, sphere, vector, color, rate
import random

# Создаем трехмерное окно
scene = canvas(title="3D Симуляция частиц", width=800, height=600)

# Границы коробки
L = 5

# Создаем список частиц
particles = []
for _ in range(30):
    # Случайная позиция и скорость
    pos = vector(random.uniform(-L, L), random.uniform(-L, L), random.uniform(-L, L))
    vel = vector(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2))

    # Визуальный объект сферы
    p = sphere(pos=pos, radius=0.3, color=color.cyan)
    p.velocity = vel
    particles.append(p)

dt = 0.01
while True:
    rate(100) # Ограничение скорости анимации

    for p in particles:
        p.pos = p.pos + p.velocity * dt

        # Отскок от 3D стен
        if abs(p.pos.x) > L: p.velocity.x *= -1
        if abs(p.pos.y) > L: p.velocity.y *= -1
        if abs(p.pos.z) > L: p.velocity.z *= -1
