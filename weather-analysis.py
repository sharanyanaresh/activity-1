# Weather data for Gandhinagar (last 10 days)
temperature = [34, 35, 33, 36, 37, 38, 36, 35, 34, 33]
humidity = [45, 48, 50, 47, 46, 44, 43, 42, 41, 40]

aqi = [92, 95, 90, 98, 100, 105, 102, 97, 94, 93]

def average(data):
    return sum(data) / len(data)

def median(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

results = f"""
Weather Analysis – Gandhinagar (Last 10 Days)

Temperature:
Average: {average(temperature)}
Median: {median(temperature)}

Humidity:
Average: {average(humidity)}
Median: {median(humidity)}

AQI:
Average: {average(aqi)}
Median: {median(aqi)}
"""

print(results)

with open("results.txt", "w") as file:
    file.write(results)

