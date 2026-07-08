import tkinter as tk
import random
import math

WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 30
RADIUS = 10

class Simulation:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#14141e")
        self.canvas.pack()
        
        self.particles = []
        for _ in range(NUM_PARTICLES):
            x = random.uniform(RADIUS, WIDTH - RADIUS)
            y = random.uniform(RADIUS, HEIGHT - RADIUS)
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            
            # Рисуем круг в tkinter
            obj = self.canvas.create_oval(x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS, fill="#00ffcc", outline="")
            
            self.particles.append({
                "id": obj, "x": x, "y": y,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed
            })
        
        self.update()

    def update(self):
        for p in self.particles:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            
            # Отскок от стен
            if p["x"] - RADIUS < 0 or p["x"] + RADIUS > WIDTH: p["vx"] *= -1
            if p["y"] - RADIUS < 0 or p["y"] + RADIUS > HEIGHT: p["vy"] *= -1
            
            # Перемещаем объект на холсте
            self.canvas.coords(p["id"], p["x"]-RADIUS, p["y"]-RADIUS, p["x"]+RADIUS, p["y"]+RADIUS)
            
        self.canvas.after(16, self.update) # ~60 FPS

root = tk.Tk()
root.title("Симуляция на Tkinter")
sim = Simulation(root)
root.mainloop()
