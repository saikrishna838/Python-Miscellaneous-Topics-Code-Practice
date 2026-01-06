from datetime import datetime
year_a, year_b = input().split()

mondays = 0
months = range(1, 13)

for year in range(int(year_a), int(year_b) + 1):
    for month in months:
        date_time_object = datetime(year, month, 1)
        name_of_weekday = datetime.strftime(date_time_object, "%A")
        if name_of_weekday == "Monday":
            mondays += 1
        

    
print(mondays)