import csv
from matplotlib import pyplot as plt 
from datetime import datetime as dt

filename =  'Edison_weather.csv'

with open(filename) as f:
    reader =  csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, col_hdr in enumerate(header_row):
        print(index, col_hdr)

    dates, high, lows = [], [], []
    for ht in reader:
        try:
            current_date = dt.strptime(ht[0],"%m/%d/%Y")  
            h = int(ht[1])
            l = int(ht[3])      
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            high.append(h)
            lows.append(l)

    #print(high)
    #Plot Data
    fig = plt.figure(dpi=128, figsize=(8, 4))
    plt.plot(dates, high, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, high, lows, facecolor='blue', alpha=0.1)

    #Format Plot
    plt.title("Edison Daily Weather high/low for Jan 2018")
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Temp(f)', fontsize=14)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


