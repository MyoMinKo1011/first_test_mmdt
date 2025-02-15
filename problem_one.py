hour_in_year = 365 * 24 # we did not think the leap year if leap year use 366

hour_in_decade = 10 * hour_in_year * 60

print(hour_in_year)
print(hour_in_decade)

age = int(input("Enter your age: "))

age_in_second = age * hour_in_year * 60 * 60

print(age_in_second)


