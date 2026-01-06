from datetime import datetime, timedelta

date_time_string = input()
n = int(input())

date_obj = datetime.strptime(date_time_string, '%b %d %Y')
date_after_five_year = date_obj + timedelta(days=n*365)
print(date_after_five_year)