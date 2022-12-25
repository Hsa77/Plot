from Libs import exel_reader, separator
import matplotlib.pylab as plt
import numpy as np

LAST_S = 0
DataSheet = exel_reader()

sep = separator(DataSheet)

for i in sep:
    Axes1 = np.array(sep[i]["Days"]) / 30
    T = (np.array(sep[i]["SnowFall"]) * 100) + LAST_S
    Axes2 = (Axes1 / T) * (-1)
    print(Axes2)
    LAST_S = T[-1]
    plt.plot(Axes1, Axes2)
    plt.title(f'{sep[i]["name"]}')
    plt.show()




