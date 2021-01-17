import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rain_amounts = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain_amount = float(row[3])
        except ValueError:
            print(f'Missing rain total for {current_date}')
        else:
            dates.append(current_date)
            rain_amounts.append(rain_amount)


#plotting rain
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rain_amounts, c='blue')

#formatting plot
ax.set_title('Rain Amounts in Sitka for 2018', fontsize=24)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rain Amounts', fontsize= 16)
ax.tick_params(axis= 'both', which= 'major', labelsize=16)

plt.show()
