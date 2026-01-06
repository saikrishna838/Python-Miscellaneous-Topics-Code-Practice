from datetime import datetime

date_string = "%d %b %Y"
date_input = input()
datetime_object = datetime.strptime(date_input, date_string)
print(datetime_object)
