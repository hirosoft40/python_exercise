#--- Trying to import csv file with some data
#--- y tick is not going well

import csv
import matplotlib.pyplot as plot
import numpy as np

with open('stocks_move.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    data = list(csv_reader)
    data = np.array(data)

xs, sp500, fb, exxon, pg, apl, pfi, amz, sf  =[], [], [], [], [], [], [], [], []
for i in range(0,len(data)):
    xs.append(data[i][0])
    sp500.append(data[i][1])
    fb.append(data[i][2])
    exxon.append(data[i][3])
    pg.append(data[i][4])
    apl.append(data[i][5])
#    pfi.append(data[i][6])
    amz.append(data[i][7])
    sf.append(data[i][8])


locs, labs = plot.yticks()
#loc, labs = plot.xticks()
#print(labs)
plot.yticks(np.arange(0, 400, 50.0))
# plot.xticks(labs[1:])
# plot.plot(xs, sp500)
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