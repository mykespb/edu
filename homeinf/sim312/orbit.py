import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. ФИЗИЧЕСКИЕ КОНСТАНТЫ И ПАРАМЕТРЫ ---
G = 6.6743e-11          # Гравитационная постоянная, м^3 / (кг * с^2)
M_earth = 5.972e24      # Масса Земли, кг
R_earth = 6371000       # Радиус Земли, метров
GM = G * M_earth

# --- 2. ДИФФЕРЕНЦИАЛЬНЫЕ УРАВНЕНИЯ ДВИЖЕНИЯ (Закон всемирного тяготения) ---
def orbit_equations(t, state):
    """
    state = [x, y, vx, vy]
    Возвращает производные: [vx, vy, ax, ay]
    """
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    
    # Ускорение a = -G*M * r_vector / r^3
    ax = -GM * x / r**3
    ay = -GM * y / r**3
    
    return [vx, vy, ax, ay]

# --- 3. НАЧАЛЬНЫЕ УСЛОВИЯ (Низкая околоземная орбита) ---
# Спутник на высоте 600 км над поверхностью Земли
altitude = 600000 
r_0 = R_earth + altitude
# Круговая скорость v = sqrt(GM / r). Добавим +10% для эллиптической орбиты
v_0 = np.sqrt(GM / r_0) * 1.1  

initial_state = [r_0, 0, 0, v_0]  # x0, y0, vx0, vy0
t_span = (0, 10000)               # Время симуляции в секундах (~2.7 часа)
t_eval = np.linspace(t_span[0], t_span[1], 500) # Точки времени для анимации

# --- 4. ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ (SciPy) ---
solution = solve_ivp(
    orbit_equations, 
    t_span, 
    initial_state, 
    t_eval=t_eval, 
    method='RK45', 
    rtol=1e-8
)

x_coords = solution.y[0]
y_coords = solution.y[1]

# --- 5. АНИМАЦИЯ И ВИЗУАЛИЗАЦИЯ (Matplotlib) ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

# Рисуем Землю (в масштабе тысяч километров)
earth_circle = plt.Circle((0, 0), R_earth / 1e3, color='#2b5c8f', label='Земля')
ax.add_artist(earth_circle)

# Настройка осей (переводим метры в километры для читаемости)
max_bound = max(np.max(np.abs(x_coords)), np.max(np.abs(y_coords))) / 1e3 * 1.2
ax.set_xlim(-max_bound, max_bound)
ax.set_ylim(-max_bound, max_bound)
ax.set_xlabel('X (км)')
ax.set_ylabel('Y (км)')
ax.set_title('Моделирование эллиптической орбиты спутника (Python 3.12)')

# Элементы анимации
orbit_line, = ax.plot([], [], color='gray', linestyle=':', alpha=0.7, label='Траектория')
satellite, = ax.plot([], [], 'ro', markersize=6, label='Спутник')
ax.legend(loc='upper right')

# Функция инициализации анимации
def init():
    orbit_line.set_data([], [])
    satellite.set_data([], [])
    return orbit_line, satellite

# Функция обновления каждого кадра
def update(frame):
    # Отрисовываем пройденную траекторию до текущего кадра
    orbit_line.set_data(x_coords[:frame] / 1e3, y_coords[:frame] / 1e3)
    # Текущее положение спутника
    satellite.set_data([x_coords[frame] / 1e3], [y_coords[frame] / 1e3])
    return orbit_line, satellite

# Запуск анимации
ani = FuncAnimation(
    fig, 
    update, 
    frames=len(t_eval), 
    init_func=init, 
    interval=20, 
    blit=True, 
    repeat=True
)

plt.show()

