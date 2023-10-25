import csv
import time

planets = []
original = []


def import_data(reader):
    global planets, original
    for row in reader:
        if row[0] == 'Planet':
            continue
        name = row[0]
        color = row[1]
        mass = float(row[2])
        dia = row[3]
        density = row[4]
        surface_grav = row[5]
        esc_vel = row[6]
        rot_per = row[7]
        day_len = row[8]
        sun_dist = row[9]
        peri = row[10]
        aph = row[11]
        orb_per = row[12]
        orb_vel = row[13]
        orb_inc = row[14]
        orb_ecc = row[15]
        obl = row[16]
        avg_temp = row[17]
        surf_pressure = row[18]
        moons = row[19]
        if row[20] == 'Yes':
            rings = True
        elif row[20] == 'No':
            rings = False
        if row[21] == 'Yes':
            mag_field = True
        elif row[21] == 'No':
            mag_field = False
        planets.append([name, color, mass, dia, density,
                        surface_grav, esc_vel, rot_per, day_len, sun_dist, peri,
                        aph, orb_per, orb_vel, orb_inc, orb_ecc, obl, avg_temp,
                        surf_pressure, moons, rings, mag_field])

    original = planets


def insertion_sort():
    global planets
    if planets != original:
        planets = original
    for i in range(len(planets)):
        index = i
        for j in range(i + 1, len(planets)):
            if compare(planets[j], planets[index]):
                index = j
        planets[i], planets[index] = planets[index], planets[i]
    result = planets
    return result


def compare(list, list2):
    return list[2] < list2[2]


# selection sort algorithm
def selection_sort():
    global planets
    low = float('inf')
    if planets != original:
        planets = original
    for row in planets:
        mass = planets[row][2]
        if mass < low:
            pass
        # planets[row], planets[index] = planets[index], planets[i]
    result = planets
    return result


with open('planets.csv') as planet:
    if __name__ == '__main__':
        reader = csv.reader(planet)
        import_data(reader)
        for row in planets:
            print(row)

        sort1 = selection_sort()
        for row in planets:
            print(row)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
