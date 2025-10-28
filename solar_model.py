# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = 0
    body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        dx = obj.x - body.x
        dy = obj.y - body.y
        r2 = dx**2 + dy**2
        if r2 == 0:
            continue  # чтобы избежать деления на ноль

        r = r2**0.5
        # Закон всемирного тяготения: F = G * m1 * m2 / r²
        F = gravitational_constant * body.m * obj.m / r2

        # Разложение силы по осям:
        Fx = F * dx / r
        Fy = F * dy / r

        # Суммируем вклады от всех тел
        body.Fx += Fx
        body.Fy += Fy
        

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    **dt** - шаг по времени
    """

    # Ускорения
    ax = body.Fx / body.m
    ay = body.Fy / body.m

    # Изменение скоростей
    body.Vx += ax * dt
    body.Vy += ay * dt

    # Изменение координат (равнопеременное движение)
    body.x += body.Vx * dt
    body.y += body.Vy * dt



def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
