import pandas as pd
import datetime
import warnings
warnings.simplefilter('ignore')


def print_period(period_start, period_end):
    datetime_start = str(datetime.datetime.fromtimestamp(period_start))[11:16]
    datetime_end = str(datetime.datetime.fromtimestamp(period_end))[11:16]
    current_spent = period_end - period_start
    print(datetime_start, '-', datetime_end, str(datetime.timedelta(seconds=int(current_spent))))


today = str(datetime.date.today())

logged_data = pd.read_csv('logger.csv')
timestamps = logged_data[logged_data.date == today].log_timestamp

period_start = timestamps[0]
period_end = timestamps[0]
period_time = 0
total_time = 0

print('Periods:')
for i in range(1, len(logged_data)):
    diff = timestamps[i] - timestamps[i-1]
    if diff < 2:
        period_time += diff
        total_time += diff
    else:
        period_end = timestamps[i-1]
        print_period(period_start, period_end)
        period_start = timestamps[i]
        period_time = 0

if period_end <= period_start:
    period_end = timestamps.values[-1]
    print_period(period_start, period_end)

print('Total:', str(datetime.timedelta(seconds=int(total_time))))
