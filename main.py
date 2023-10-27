"""Output sample:

Selection sort results:
Mercury, 0.33
Mars, 0.642
Venus, 4.87
Earth, 5.97
Uranus, 86.8
Neptune, 102.0
Saturn, 568.0
Jupiter, 1898.0
Average time: 5400.41 nanoseconds.
It took: 14 steps to complete.
------------------------------------------

------------------------------------------
Insertion sort results:
Mercury, 0.33
Mars, 0.642
Venus, 4.87
Earth, 5.97
Uranus, 86.8
Neptune, 102.0
Saturn, 568.0
Jupiter, 1898.0
Average time: 2690.0 nanoseconds.
It took: 7 steps to complete.
------------------------------------

Based on the output above, the insertion sort appears to operate faster and with fewer steps
compared to the selection sort. Including the 'compare' function, the selection sort algorithm is
slightly longer than the insertion sort algorithm, making it less efficient as a result.
"""
# Modules imported for additional functionality.
import csv
import time

# Global variables. One is changed as it is sorted, but the other remains the same after the data is imported.
planets = []
original = []


# Displays the results of the sorting algorithms.
def show_results(sort, sort1, a1, a2, steps, steps2):
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
    print('It took: ' + str(steps2) + ' steps to complete.')


# Imports data from the CSV file.
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
        original.append([name, color, mass, dia, density,
                         surface_grav, esc_vel, rot_per, day_len, sun_dist, peri,
                         aph, orb_per, orb_vel, orb_inc, orb_ecc, obl, avg_temp,
                         surf_pressure, moons, rings, mag_field])


# Sorts the list of lists by comparing elements next to each other.
def insertion_sort():
    global planets, original
    steps1 = 0
    planets = list(original)

    for i in range(1, len(planets)):

        cur_planet = planets[i]
        x = float(cur_planet[2])
        j = i - 1
        while j >= 0 and x < float(planets[j][2]):
            planets[j + 1] = planets[j]
            j -= 1
            steps1 += 1
        planets[j + 1] = cur_planet
    result = planets
    return result, steps1


# Compares the mass of each planet. Returns either true or false.
def compare(list, list2):
    return list[2] < list2[2]


# selection sort algorithm
def selection_sort():
    global planets, original
    steps = 0
    planets = list(original)

    size = len(planets)
    for ind in range(size):
        min_ind = ind
        for j in range(ind + 1, size):
            if compare(planets[j], planets[min_ind]):
                min_ind = j
                steps += 1

        # swaps values at each index using a tuple.
        planets[ind], planets[min_ind] = planets[min_ind], planets[ind]
        steps += 1
    result = planets
    return result, steps


# Opens the csv file and runs the program.
with open('planets.csv') as planet:
    if __name__ == '__main__':
        reader = csv.reader(planet)
        import_data(reader)
        start = time.perf_counter_ns()
        for i in range(100):
            sort1, steps = selection_sort()
        end = time.perf_counter_ns()
        start2 = time.perf_counter_ns()
        for k in range(100):
            sort2, steps2 = insertion_sort()
        end2 = time.perf_counter_ns()
        average1 = (end - start) / 100
        average2 = (end2 - start2) / 100
        show_results(sort1, sort2, average1, average2, steps, steps2)
