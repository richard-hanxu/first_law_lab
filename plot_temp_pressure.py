import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import uncertainties as unc

currentPath = os.getcwd()

def plot_heat_transfer(df : pd.DataFrame):
    fig, ax = plt.subplots()
    ax.grid(axis="x")
    ax.set_title("T and P Vs. Time, (60 Deg C, 70 PSI) ")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (Deg C)")
    time = df["Time(s)"]
    temp = df["T1(DegC)"]
    pressure = df["P1(PSI)"]

    plt.xticks(np.arange(0, time[len(time) - 1], step=5))
    labels = ax.xaxis.get_ticklabels()
    for i in range(len(labels)):
        if i % 2 != 0:
            labels[i].set_visible(False)

    twin1 = ax.twinx()
    twin1.set_ylabel("Pressure (PSI)")
    ax.set_ylim(0, 90)
    twin1.set_ylim(0, 80)
    p1 = ax.scatter(time, temp, s=2, c="b", label="Temperature")
    p2 = twin1.scatter(time, pressure, s=2, c="r", label="Pressure")
    ax.yaxis.label.set_color("b")
    twin1.yaxis.label.set_color("r")

    ax.legend(handles=[p1, p2])
    plt.show()

df = pd.read_csv(os.path.join(currentPath, "data/L2PRT1D_format.csv"))
plot_heat_transfer(df)
