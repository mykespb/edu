import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. ФИЗИЧЕСКИЕ КОНСТАНТЫ ---
G = 6.6743e-11          # Гравитационная постоянная
M_earth = 5.972e24      # Масса Земли, кг
R_earth = 6371000       # Радиус Земли, м
M_moon = 7.342e22       # Масса Луны, кг
R_moon_orbit = 384400000 # Радиус орбиты Луны (средний), м
R_moon = 1737000        # Радиус Луны, м

# Параметры атмосферы Земли (экспоненциальная модель)
rho_0 = 1.225           # Плотность воздуха у поверхности, кг/м^3
H_scale = 8500          # Характеристическая высота атмосферы, м

# Параметры спутника
m_sat = 500.0           # Масса спутника, кг
A_sat = 4.0             # Площадь поперечного сечения, м^2
C_d = 2.2               # Коэффициент лобового сопротивления

# Скорость вращения Луны вокруг Земли (рад/с)
omega_moon = np.sqrt(G * (M_earth + M_moon) / R_moon_orbit**3)

# --- 2. ДИФФЕРЕНЦИАЛЬНЫЕ УРАВНЕНИЯ ДВИЖЕНИЯ В 3D ---
def complex_orbit_equations(t, state):
    """
    state = [x, y, z, vx, vy, vz]
    Возвращает вектор производных: [vx, vy, vz, ax, ay, az]
    """
    x, y, z, vx, vy, vz = state
    r_vector = np.array([x, y, z])
    r_mag = np.linalg.norm(r_vector)
    v_vector = np.array([vx, vy, vz])
    v_mag = np.linalg.norm(v_vector)
    
    # --- Условие падения на Землю ---
    if r_mag <= R_earth:
        return [0, 0, 0, 0, 0, 0] # Спутник упал, движение прекращено

    # 1. Гравитация Земли
    a_earth = -G * M_earth * r_vector / r_mag**3
    
    # 2. Гравитация Луны (Луна вращается в плоскости XY с наклоном 5 градусов)
    moon_angle = omega_moon * t
    moon_inclination = np.radians(5.14) # Наклон орбиты Луны
    
    x_moon = R_moon_orbit * np.cos(moon_angle)
    y_moon = R_moon_orbit * np.sin(moon_angle) * np.cos(moon_inclination)
    z_moon = R_moon_orbit * np.sin(moon_angle) * np.sin(moon_inclination)
    
    moon_vector = np.array([x_moon, y_moon, z_moon])
    r_sat_moon = moon_vector - r_vector
    r_sat_moon_mag = np.linalg.norm(r_sat_moon)
    
    # Сила притяжения Луны (приливное ускорение относительно центра Земли)
    a_moon = G * M_moon * (r_sat_moon / r_sat_moon_mag**3 - moon_vector / R_moon_orbit**3)

    # 3. Сопротивление атмосферы (зависит от высоты)
    altitude = r_mag - R_earth
    if altitude < 600000: # Атмосфера учитывается до высоты 600 км
        rho = rho_0 * np.exp(-altitude / H_scale)
        # Сила сопротивления направлена против вектора скорости
        drag_force_mag = 0.5 * rho * v_mag**2 * C_d * A_sat
        a_drag = -(drag_force_mag / m_sat) * (v_vector / v_mag)
    else:
        a_drag = np.zeros(3)

    # Полное ускорение
    a_total = a_earth + a_moon + a_drag
    
    return [vx, vy, vz, a_total[0], a_total[1], a_total[2]]

# --- 3. НАЧАЛЬНЫЕ УСЛОВИЯ (Низкая вытянутая орбита для демонстрации торможения) ---
# Намеренно опускаем перигей до 180 км, чтобы показать влияние атмосферы
altitude_start = 180000  
r_0 = R_earth + altitude_start

# Задаем начальную скорость с наклоном в 3D (компонента Vz)
v_circular = np.sqrt(G * M_earth / r_0)
v_0_x = 0
v_0_y = v_circular * 1.05  # Слегка эллиптическая орбита
v_0_z = v_circular * 0.2   # Наклоняем орбиту относительно экватора

initial_state = [r_0, 0, 0, v_0_x, v_0_y, v_0_z]

# Симулируем 120 000 секунд (~33 часа), чтобы увидеть деградацию орбиты
t_span = (0, 120000)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# --- 4. ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ ---
solution = solve_ivp(
    complex_orbit_equations, 
    t_span, 
    initial_state, 
    t_eval=t_eval, 
    method='RK45', 
    rtol=1e-7
)

# Вытаскиваем координаты спутника (переводим в тысячи километров для масштаба графика)
x_sat, y_sat, z_sat = solution.y[0] / 1e3, solution.y[1] / 1e3, solution.y[2] / 1e3

# Отсекаем точки после падения на Землю (где скорость занулилась)
for i in range(1, len(x_sat)):
    if x_sat[i] == x_sat[i-1] and y_sat[i] == y_sat[i-1]:
        x_sat, y_sat, z_sat = x_sat[:i], y_sat[:i], z_sat[:i]
        t_eval = t_eval[:i]
        break

# --- 5. 3D ВИЗУАЛИЗАЦИЯ И АНИМАЦИЯ ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Рисуем Землю в центре
r_e_km = R_earth / 1e3
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
x_e = r_e_km * np.cos(u) * np.sin(v)
y_e = r_e_km * np.sin(u) * np.sin(v)
z_e = r_e_km * np.cos(v)
ax.plot_surface(x_e, y_e, z_e, color='#2b5c8f', alpha=0.6, label='Земля')

# Траектория Луны (масштабированная для понимания направления притяжения)
# Поскольку Луна ОЧЕНЬ далеко (384 тыс. км), на графике мы покажем лишь вектор направления
moon_angles = omega_moon * t_eval
x_m_dir = (R_earth * 2 / 1e3) * np.cos(moon_angles)
y_m_dir = (R_earth * 2 / 1e3) * np.sin(moon_angles)

# Настройка осей графика (фокусируемся на околоземном пространстве)
max_range = r_e_km * 3
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_zlim(-max_range, max_range)

ax.set_xlabel('X (тыс. км)')
ax.set_ylabel('Y (тыс. км)')
ax.set_zlabel('Z (тыс. км)')
ax.set_title('3D-моделирование: задача 3-х тел + торможение в атмосфере')

# Графические объекты для анимации
orbit_line, = ax.plot([], [], [], color='crimson', lw=1.5, label='Траектория падения')
sat_point, = ax.plot([], [], [], 'ro', markersize=5, label='Спутник')
moon_vector_line, = ax.plot([], [], [], color='gray', linestyle='--', alpha=0.5, label='Направление на Луну')

ax.legend(loc='upper left')

def init():
    orbit_line.set_data_mapping = True
    return orbit_line, sat_point, moon_vector_line

def update(frame):
    # Рисуем пройденную спираль
    orbit_line.set_data(x_sat[:frame], y_sat[:frame])
    orbit_line.set_3d_properties(z_sat[:frame])
    
    # Положение спутника
    sat_point.set_data([x_sat[frame]], [y_sat[frame]])
    sat_point.set_3d_properties([z_sat[frame]])
    
    # Линия направления на Луну от центра Земли
    moon_vector_line.set_data([0, x_m_dir[frame]], [0, y_m_dir[frame]])
    moon_vector_line.set_3d_properties([0, 0])
    
    return orbit_line, sat_point, moon_vector_line

ani = FuncAnimation(
    fig, 
    update, 
    frames=len(t_eval), 
    init_func=init, 
    interval=15, 
    blit=False, 
    repeat=False
)

plt.show()

