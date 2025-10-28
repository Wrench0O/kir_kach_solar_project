# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, encoding="utf8") as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object type:", object_type)

    return objects


def parse_star_parameters(line, star):
    parts=line.split()
    if len(parts) != 8:
        raise ValueError(f"Invalid star data line: {line}")
    _, radius, color, mass, x, y, vx, vy = parts

    star.R = float(radius)
    star.color = color
    star.m = float(mass)
    star.x = float(x)
    star.y = float(y)
    star.Vx = float(vx)
    star.Vy = float(vy)
    
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    pass  # FIXME: not done yet

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    parts = line.split()
    if len(parts) != 8:
        raise ValueError(f"Invalid planet data line: {line}")

    _, radius, color, mass, x, y, vx, vy = parts

    planet.R = float(radius)
    planet.color = color
    planet.m = float(mass)
    planet.x = float(x)
    planet.y = float(y)
    planet.Vx = float(vx)
    planet.Vy = float(vy)
    
    pass  # FIXME: not done yet...


def write_space_objects_data_to_file(filename, space_objects):
        with open(filename, "w") as file:
            for obj in space_objects:
                file.write(
                    f"{obj.type} "
                    f"{obj.m} "
                    f"{obj.x} {obj.y} "
                    f"{obj.Vx} {obj.Vy} "
                    f"{obj.R}\n"
                )

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
