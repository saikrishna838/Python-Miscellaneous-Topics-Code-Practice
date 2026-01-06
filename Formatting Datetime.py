from datetime import datetime

date_format = "%b %d %Y %I:%M%p"
date_input = input()

datetime_obj = datetime.strptime(date_input, date_format)

output_format = "%d/%m/%Y %H:%M:%S"
formatted_date = datetime.strftime(datetime_obj, output_format)

print(formatted_date)
