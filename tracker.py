import time
import pandas as pd
import datetime


logged_data = pd.read_csv('logger.csv')

today = str(datetime.date.today())

timestamps = logged_data[logged_data.date == today].log_timestamp

spent_time_today = 0
for i in range(1, len(timestamps)):
    diff = timestamps[i] - timestamps[i-1]
    if diff < 2:
        spent_time_today += diff

print('Date:', today)
print('Spent:', str(datetime.timedelta(seconds=int(spent_time_today))))

last_timestamp = time.time()
while True:
    time.sleep(0.1)
    timestamp = time.time()
    if timestamp - last_timestamp > 1:
        spent_time_today += timestamp - last_timestamp
        last_timestamp = timestamp
        with open('logger.csv', 'a') as f:
            f.write(today+','+str(timestamp)+'\n')

        print('Spent:', str(datetime.timedelta(seconds=int(spent_time_today))))
