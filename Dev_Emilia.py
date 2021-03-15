from matplotlib import pyplot as plt
from matplotlib import dates as mplDates
import numpy as np
from datetime import datetime

plt.xkcd()


# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# plt.xticks([])
# plt.yticks([])
# ax.set_ylim([-30, 10])

data_time = ["07/12/2020", "07/16/2020", "07/17/2020", "07/20/2020", "07/23/2020", "07/28/2020", "07/30/2020", "08/04/2020",
             "08/10/2020", "08/31/2020", "09/15/2020", "10/02/2020", "12/07/2020"]
data_weight = [3340, 3400, 3440, 3560, 3600, 3780, 3840, 3980, 4130, 4580, 4860, 5500, 7050]
x_values = [datetime.strptime(d, "%m/%d/%Y").date() for d in data_time]
x_values_conv = mplDates.date2num(x_values)

# For lobal axis
hfmt = mplDates.DateFormatter('%d/%m')



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_major_formatter(hfmt)
ax.set_title('Sumo-Emilia auf der Waage')
ax.set_xlabel('Datum')
ax.set_ylabel('Gewicht [g]')
ax.plot(x_values_conv, data_weight, linewidth=2)
ax.scatter(x_values_conv, data_weight)
ax.grid()
ax.xaxis.grid(linewidth=1.0)
ax.yaxis.grid(linewidth=1.0)
plt.savefig("Sumo_Emilia.pdf", bbox_inches = "tight")
plt.show()
