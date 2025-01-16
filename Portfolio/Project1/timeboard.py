import os
import sys
from collections import defaultdict
from tabulate import tabulate

def read_drivers(file_name):
    drivers = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            driver_code = parts[1]
            drivers[driver_code] = {
                'name': parts[2],
                'team': parts[3]
            }
    return drivers

def lap_time(file_name):
    lap_times = defaultdict(list)
    with open(file_name, 'r') as file:
        race_location = file.readline().strip()  
        for line in file:
            driver_code = line[:3]
            time = float(line[3:].strip())
            lap_times[driver_code].append(time)
    return race_location, lap_times

def driver(lap_times):
    driver_stats = {}
    for driver_code, times in lap_times.items():
        fastest_time = min(times)
        average_time = sum(times) / len(times)
        driver_stats[driver_code] = {
            'fastest_time': fastest_time,
            'average_time': average_time
        }
    return driver_stats

def result(drivers, files):
    all_stats = {}
    for file_name in files:
        race_location, lap_times = lap_time(file_name)
        driver_stats = driver(lap_times)

        for driver_code, stats in driver_stats.items():
            if driver_code not in all_stats:
                all_stats[driver_code] = {'name': drivers[driver_code]['name'], 'team': drivers[driver_code]['team']}

            all_stats[driver_code][f'fastest_time_{file_name}'] = stats['fastest_time']
            all_stats[driver_code][f'average_time_{file_name}'] = stats['average_time']

    
    headers = ['Driver Code', 'Name', 'Team']
    headers += [f'Fastest Time {i+1}' for i in range(len(files))]
    headers += [f'Average Time {i+1}' for i in range(len(files))]

    table_data = []
    for driver_code, stats in all_stats.items():
        row = [driver_code, stats['name'], stats['team']]
        for i in range(len(files)):
            row.append(f"{stats.get(f'fastest_time_{files[i]}', 'N/A'):0.3f}")
        for i in range(len(files)):
            row.append(f"{stats.get(f'average_time_{files[i]}', 'N/A'):0.3f}")
        table_data.append(row)

    print(tabulate(table_data, headers=headers, tablefmt='grid'))

def main():
    if len(sys.argv) < 2:
        print("Usage: python f1_lap_times.py <lap_time_files>")
        sys.exit(1)
    drivers = read_drivers('f1_drivers.txt')
    files = ['lap_times_1.txt', 'lap_times_2.txt', 'lap_times_3.txt']
    result(drivers, files)

if __name__ == "__main__":
    main()
