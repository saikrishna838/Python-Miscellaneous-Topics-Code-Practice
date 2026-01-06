from datetime import datetime, timedelta

start_date_string = input()
end_date_string = input()

start_date = datetime.strptime(start_date_string, '%b %d %Y')
end_date = datetime.strptime(end_date_string, '%b %d %Y')

number_of_days = (end_date - start_date).days

for i in range(number_of_days + 1):
    print(start_date + timedelta(days=i))