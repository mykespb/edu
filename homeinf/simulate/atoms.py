import tkinter as tk
import random
import math

WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 25
RADIUS = 12

class Particle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.uniform(RADIUS, WIDTH - RADIUS)
        self.y = random.uniform(RADIUS, HEIGHT - RADIUS)
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 4)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        # Случайный цвет для каждого атома
        color = random.choice(["#ff3366", "#00ffcc", "#ffff33", "#3399ff"])
        self.id = canvas.create_oval(self.x-RADIUS, self.y-RADIUS, self.x+RADIUS, self.y+RADIUS, fill=color, outline="")

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Отскок от стен
        if self.x - RADIUS < 0:
            self.x = RADIUS
            self.vx *= -1
        elif self.x + RADIUS > WIDTH:
            self.x = WIDTH - RADIUS
            self.vx *= -1

        if self.y - RADIUS < 0:
            self.y = RADIUS
            self.vy *= -1
        elif self.y + RADIUS > HEIGHT:
            self.y = HEIGHT - RADIUS
            self.vy *= -1

    def update_position(self):
        self.canvas.coords(self.id, self.x-RADIUS, self.y-RADIUS, self.x+RADIUS, self.y+RADIUS)

def resolve_collisions(particles):
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p1 = particles[i]
            p2 = particles[j]
            
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            dist = math.hypot(dx, dy)
            
            if dist < RADIUS * 2 and dist > 0:
                # Физика упругого удара (обмен скоростями)
                nx = dx / dist
                ny = dy / dist
                kx = p1.vx - p2.vx
                ky = p1.vy - p2.vy
                p = nx * kx + ny * ky
                
                if p > 0: # Движутся навстречу друг другу
                    p1.vx -= p * nx
                    p1.vy -= p * ny
                    p2.vx += p * nx
                    p2.vy += p * ny
                
                # Разведение застрявших частиц
                overlap = (RADIUS * 2) - dist
                p1.x -= nx * overlap * 0.5
                p1.y -= ny * overlap * 0.5
                p2.x += nx * overlap * 0.5
                p2.y += ny * overlap * 0.5

def run_simulation():
    for p in particles:
        p.move()
    resolve_collisions(particles)
    for p in particles:
        p.update_position()
    
    root.after(16, run_simulation) # ~60 FPS

# Инициализация окна Linux Mint (Tkinter)
root = tk.Tk()
root.title("Симуляция атомов в Linux Mint")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#111118")
canvas.pack()

particles = [Particle(canvas) for _ in range(NUM_PARTICLES)]

run_simulation()
root.mainloop()
