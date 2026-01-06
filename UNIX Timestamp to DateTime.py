import datetime
zero = datetime.datetime(1970, 1, 1)


U = int(input())
seconds = datetime.timedelta(seconds=U)
result_time = zero + seconds
date_format = "%Y-%m-%d %H:%M:%S"
print(result_time.strftime(date_format))