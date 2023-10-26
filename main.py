import csv
import time

planets = []
original = []
steps = 0
steps1 = 0


def show_results(sort, sort1, a1, a2):
    global steps, steps1
    print('Selection sort results: ')
    for row in sort:
        print(str(row[0]) + ", " + str(row[2]))
    print('Average time: ' + str(a1) + ' nanoseconds.')
    print('It took: ' + str(steps) + ' steps to complete.')
    print('------------------------------------------')
    print()
    print('------------------------------------------')
    print('Insertion sort results: ')
    for row in sort1:
        print(str(row[0]) + ", " + str(row[2]))
    print('Average time: ' + str(a2) + ' nanoseconds.')
    print('It took: ' + str(steps1) + ' steps to complete.')


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


# Sorts the list of lists by comparing elements next to each other.
def insertion_sort():
    global planets, original, steps, steps1
    if planets != original:
        planets = original

    for i in range(1, len(planets)):
        cur_planet = planets[i]
        x = float(cur_planet[2])
        j = i - 1
        while j >= 0 and x < float(planets[j][2]):
            planets[j + 1] = planets[j]
            j = j - 1
            steps1 += 1
        planets[j + 1] = cur_planet
    result = planets
    return result


# Compares the mass of each planet. Returns either true or false.
def compare(list, list2):
    return list[2] < list2[2]


# selection sort algorithm
def selection_sort():
    global planets, original, steps
    if planets != original:
        planets = original
    while not sorted(planets, key=lambda x: x[2]):
        for i in range(len(planets)):
            index = i
            for j in range(i + 1, len(planets)):
                if compare(planets[j], planets[index]):
                    index = j

                steps += 1
        # swaps values at each index using a tuple.
        planets[i], planets[index] = planets[index], planets[i]

        steps += 1
    result = planets
    return result


with open('planets.csv') as planet:
    if __name__ == '__main__':
        reader = csv.reader(planet)
        import_data(reader)
        start = time.perf_counter_ns()
        for i in range(100):
            steps = 0
            sort1 = selection_sort()
        end = time.perf_counter_ns()
        start2 = time.perf_counter_ns()
        for i in range(100):
            steps = 0
            sort2 = insertion_sort()
        end2 = time.perf_counter_ns()
        average1 = (end - start) / 100
        average2 = (end2 - start2) / 100
        show_results(sort1, sort2, average1, average2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
