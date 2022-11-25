import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import uncertainties as unc

currentPath = os.getcwd()

def plot_heat_transfer(df : pd.DataFrame):
    fig, ax = plt.subplots()
    ax.grid(axis="x")
    ax.set_title("Actual Vs. Theoretical Heat Transfer per Deg C (40 Deg C, 40 PSI)")
    ax.set_ylabel("Heat Added (kJ)")
    ax.set_xlabel("Temperature (Deg C)")
    temp = df["T1(DegC)"][3000:3695]
    cumul_heat_added = df["Heater Energy (kJ)"][3000:3695]
    theor_heat_added_x = np.arange(26.0, 40.1, 0.1)

    plt.xticks(np.arange(26, 40.5, step=0.5))
    labels = ax.xaxis.get_ticklabels()
    for i in range(len(labels)):
        if i % 4 != 0:
            labels[i].set_visible(False)

    ax.set_xlim(26.0, 40.5)
    ax.set_ylim(0, 60)
    p1 = ax.scatter(temp, cumul_heat_added, s=2, c="b", label="Experimental Results")
    # c_v * m * (x - T_0), 
    # T_0 for Trial A = 26.3, B = 30.3, C = 38.1, D = 36.3
    # c_v for Trial A = 70.3, B = 71.8, C = 120.9, D = 76.77
    # m for Trial A = .04867, B = .05153, C = .03194, D = .04991
    p2, = ax.plot(theor_heat_added_x, 70.3 * 0.04867 * (theor_heat_added_x - 26.3), c="r", label="Constant c_v")
    ax.yaxis.label.set_color("b")

    ax.legend(handles=[p1, p2])
    plt.show()

df = pd.read_csv(os.path.join(currentPath, "data/L2PRT2A_format.csv"))
plot_heat_transfer(df)
