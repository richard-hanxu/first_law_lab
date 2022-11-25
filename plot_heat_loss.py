import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import uncertainties as unc

currentPath = os.getcwd()

def plot_heat_transfer(df : pd.DataFrame):
    fig, ax = plt.subplots()
    ax.grid(axis="x")
    ax.set_title("T and Q Vs. Time, (40 Deg C, 70 PSI) ")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (Deg C)")
    time = df["Time(s)"][750:]
    temp = df["T1(DegC)"][750:]
    energy = df["Heater Energy (kJ)"][750:]

    plt.xticks(np.arange(0, 710, step=25))
    labels = ax.xaxis.get_ticklabels()
    for i in range(len(labels)):
        if i % 4 != 0:
            labels[i].set_visible(False)

    twin1 = ax.twinx()
    twin1.set_ylabel("Heat Transferred (kJ)")
    ax.set_ylim(0, 90)
    twin1.set_ylim(0, 150)
    p1 = ax.scatter(time, temp, s=2, c="b", label="Temperature")
    p2 = twin1.scatter(time, energy, s=2, c="r", label="Cumulative Heat Added")
    ax.yaxis.label.set_color("b")
    twin1.yaxis.label.set_color("r")

    ax.legend(handles=[p1, p2])
    plt.show()

df = pd.read_csv(os.path.join(currentPath, "data/L2PRT2B_format.csv"))
plot_heat_transfer(df)
