temperatures = [36.6,38.2,37.1,39.0,36.9,37.5,35.8,38.7]
temperatures.append(36.4)
print(f"Readings: {len(temperatures)}")
print(f"Highest:  {max(temperatures)}")
print(f"Lowest:  {min(temperatures)}")
print(f"Average: {round(sum(temperatures) / len(temperatures), 1)}")
fevers = 0
for temp in temperatures:
    if temp >=37.5:
       fevers += 1
print(f"Fevers: {fevers}")
