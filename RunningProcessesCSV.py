#create a CSV file that lists all running processes and has columns for process ID #, name, executable path, CPU usage, and mem usage. 

#processes = []

#for resource in processes:

#def find_procs_by_name(name)

import os  # Importing the os module for operating system related functionalities
import psutil  # Importing the psutil module for getting system and process information
import csv  # Importing the csv module for reading and writing CSV files

#pip install psutil on terminal 

# Get a list of all the running processes

processes = []

for proc in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent', 'memory_info']):
    # Iterating over the running processes and appending relevant information to the 'processes' list
    processes.append([proc.info['pid'], proc.info['name'], proc.info['exe'],
                      proc.info['cpu_percent'], proc.info['memory_info'].rss])

# Write the process information to a CSV file
with open('running_processes.csv', mode='w', newline='') as file:
    # Opening a CSV file in write mode and setting newline='' to avoid extra spacing between rows
    writer = csv.writer(file)  # Creating a CSV writer object
    writer.writerow(['Process ID', 'Name', 'Executable Path', 'CPU Usage', 'Memory Usage'])
    # Writing the header row with column names
    for process in processes:
        # Iterating over the list of processes
        writer.writerow(process)
        # Writing each process's information as a row in the CSV file
print("CSV file has been created successfully.")

