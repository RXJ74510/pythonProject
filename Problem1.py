import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sorted_ages = sorted(ages)
print(sorted_ages)
min_age = sorted_ages[0]
max_age = sorted_ages[-1]
ages.append(min_age)
ages.append(max_age)

median = statistics.median(ages)
mean = sum(ages)/len(ages)
range = max_age - min_age