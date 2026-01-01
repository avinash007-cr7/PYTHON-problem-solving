# Read entire file as a single string
file = open("sensor_data.txt", "r")
data = file.read()
file.close()

lines = data.splitlines()   # split file into lines

readings = []               # list to store sensor values

# Extract numeric values, ignore comment lines
for line in lines:
    if line.startswith("#"):
        continue
    if line != "":
        readings += [float(line)]

# Total number of readings
total_readings = len(readings)

# Minimum and Maximum distance
min_distance = min(readings)
max_distance = max(readings)

# Count approach and back-off
approach = 0
backoff = 0

for i in range(1, total_readings):
    if readings[i] < readings[i - 1]:
        approach += 1
    elif readings[i] > readings[i - 1]:
        backoff += 1

# Print results
print("Total number of sensor readings:", total_readings)
print("Minimum distance recorded:", min_distance)
print("Maximum distance recorded:", max_distance)
print("Number of times robot approached the wall:", approach)
print("Number of times robot backed off:", backoff)
