import numpy as np
import matplotlib.pyplot as plt


x_firts = -10
x_last = 10
kf = [-12, -18, 5, 10, -30]
x = np.arange(x_firts, x_last, 0.01)
change_point = []
direct = -1
roots = []

color = '#156e5a'

def expression(x, koefs: list):
    return koefs[0]*x**4*np.sin(np.cos(x)) + koefs[1]*x**3 + koefs[2]*x**2 + koefs[3]*x + koefs[4]

def colorSwitcher():
    global color
    if color == '#156e5a':
        color = '#bd1931'
        return color
    else:
        color = '#156e5a'
        return color

min_point = [x[0], expression(x[0], kf)]
max_point = [x[0], expression(x[0], kf)]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot()
plt.grid()

for i in x:
    if expression(i, kf) == 0 or (expression(i, kf) > 0 and expression(i + 0.01, kf) < 0) or (expression(i, kf) < 0 and expression(i + 0.01, kf) > 0):
        roots.append((round(i, 3)))

for i in range(len(x)-1):
    if direct == -1:
        if expression(x[i], kf) < expression(x[i+1], kf):
            change_point.append((x[i], expression(x[i], kf)))
            direct = 1
            if expression(x[i], kf) < min_point[1]:
                min_point = [x[i], expression(x[i], kf)]
    else:
        if expression(x[i], kf) > expression(x[i+1], kf):
            change_point.append((x[i], expression(x[i], kf)))
            direct = -1
            if expression(x[i], kf) > max_point[1]:
                max_point = [x[i], expression(x[i], kf)]

plt.plot((x_firts, x_last), (0,0), "#949597")
plt.plot((0, 0), (min_point, max_point), "#949597")
plt.xlabel('Oсь x')
plt.ylabel('Oсь y')

x_current = np.arange(x_firts, change_point[0][0], 0.01)
if expression(x_firts, kf) > expression(change_point[0][0], kf):
    plt.plot(x_current, expression(x_current, kf), colorSwitcher(), label=f"От {x_firts} по {round(change_point[0][0], 2)} - промежуток убывания функции")
elif expression(x_firts, kf) < expression(change_point[0][0], kf):
    plt.plot(x_current, expression(x_current, kf), colorSwitcher(), label=f"От {x_firts} по {round(change_point[0][0], 2)} - промежуток возрастания функции")

for i  in range(len(change_point)-1):
    x_current = np.arange(change_point[i][0], change_point[i+1][0], 0.01)
    if expression(change_point[i][0], kf) > expression(change_point[i+1][0], kf):
        plt.plot(x_current, expression(x_current, kf), colorSwitcher(), label=f"От {round(change_point[i][0], 2)} по {round(change_point[i+1][0], 2)} - промежуток убывания функции")
    elif expression(change_point[i][0], kf) < expression(change_point[i+1][0], kf):
        plt.plot(x_current, expression(x_current, kf), colorSwitcher(), label=f"От {round(change_point[i][0], 2)} по {round(change_point[i+1][0], 2)} - промежуток возрастания функции")

x_current = np.arange(change_point[-1][0], x_last, 0.01)
plt.plot(x_current, expression(x_current, kf), colorSwitcher())
if expression(change_point[-1][0], kf) > expression(x_last, kf):
    plt.plot(x_current, expression(x_current, kf), colorSwitcher(), label=f"От {round(change_point[-1][0], 2)} по {x_last} - промежуток убывания функции")
elif expression(change_point[-1][0], kf) < expression(x_last, kf):
    plt.plot(x_current, expression(x_current, kf), colorSwitcher(), label=f"От {round(change_point[-1][0], 2)} по {x_last} - промежуток возрастания функции")

plt.plot(max_point[0], max_point[1], 'black', marker='^', markerfacecolor='#e57029', ms=8, label=f"Максимум функции на отрезке от x = {x_firts} по x = {x_last}\nmax({round(max_point[0], 3)}; {round(max_point[1], 3)})")
plt.plot(min_point[0], min_point[1], 'black', marker='v', markerfacecolor='#4c7ea2', ms=8, label=f"Минимум функции на отрезке от x = {x_firts} по x = {x_last}\nmin({round(min_point[0], 3)}; {round(min_point[1], 3)})")
for i in range(len(roots)):
    plt.plot(roots[i], 0, 'black', marker='D', markerfacecolor='#f5df4e', ms=7, label=f"X{i+1} ≈ {roots[i]}")

plt.legend(fontsize=8, title=f"f(x) = -12x⁴ ∙ sin(cos(x)) - 18x³ + 5x² + 10x - 30", title_fontsize=11)



plt.show()