import matplotlib.pyplot as plt
import csv
from datetime import datetime
from pathlib import Path
from matplotlib.dates import DateFormatter, AutoDateLocator

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

ax.xaxis.set_major_locator(AutoDateLocator(maxticks=14))
# ax.xaxis.set_major_locator(plt.MaxNLocator(nbins=15))
ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=12))
ax.xaxis.set_major_formatter(DateFormatter("%b-%d"))
fig.autofmt_xdate()

plt.show()


# for index, column_header in enumerate(header_row):
#    print(index, column_header)

# ax.set_aspect('equal')
