#--- Trying to import csv file with some data
#--- y tick is not going well

import csv
import matplotlib.pyplot as plot
import numpy as np
import datetime

with open('stocks_move.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    data = list(csv_reader)
    data = np.array(data)

xs, sp500, fb, exxon, pg, apl, pfi, amz, sf  =[], [], [], [], [], [], [], [], []
for i in range(0,len(data)):
    xs.append(datetime.datetime.strptime(data[i][0],'%Y-%m-%d'))
    sp500.append(int(data[i][1]))
    fb.append(int(data[i][2]))
    exxon.append(int(data[i][3]))
    pg.append(int(data[i][4]))
    apl.append(int(data[i][5]))
#    pfi.append(data[i][6])
    amz.append(int(data[i][7]))
    sf.append(int(data[i][8]))


locs, labs = plot.yticks()
print(sp500)
plot.yticks(range(-100,500+1, 50))
plot.plot(xs, sp500, label='sp500')
plot.plot(xs, fb, label="fb")
plot.plot(xs, exxon, label="exxon")
plot.plot(xs, pg, label="P&G")
plot.plot(xs, apl, label="Apple")
#plot.plot(xs, pfi, label="Pfizer")
plot.plot(xs, amz, label="Amazon")
plot.plot(xs, sf, label="Salesforce")
plot.title("Stock price monthly move")
plot.gca().legend((header))
plot.legend(loc = 'upper left')
plot.show()