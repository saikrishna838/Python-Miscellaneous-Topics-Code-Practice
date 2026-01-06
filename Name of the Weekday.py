from datetime import datetime

date = input()
date_string = "%d %b %Y"
datetime_object = datetime.strptime(date, date_string)
name_of_the_day = datetime_object.strftime("%A")
print(name_of_the_day)