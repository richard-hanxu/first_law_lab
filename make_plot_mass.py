import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import uncertainties as unc

currentPath = os.getcwd()

def plot_mass(df : pd.DataFrame):
    fig, ax = plt.subplots()
    ax.grid(axis="x")
    ax.set_title("Mass Vs. Time, (40 Deg C, 70 PSI)")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Mass Flow Rate (g/min)")
    time = df["Time(s)"]
    flow_rate = df["Mass Flowrate(g/min)"]
    cumulative_mass = np.zeros(len(flow_rate), dtype=float)
    cumulative_mass[0] = flow_rate[0] / 600
    for i in range(1, len(flow_rate)):
        cumulative_mass[i] = cumulative_mass[i - 1] + flow_rate[i] / 600

    plt.xticks(np.arange(0, int(time[len(time) - 1]), step=5))
    labels = ax.xaxis.get_ticklabels()
    for i in range(len(labels)):
        if i % 2 != 0:
            labels[i].set_visible(False)

    twin1 = ax.twinx()
    twin1.set_ylabel("Cumulative Mass (g)")
    ax.set_ylim(0, 60)
    twin1.set_ylim(0, 60)
    p1 = ax.scatter(time, flow_rate, s=2, c="b", label="Mass Flow Rate")
    p2 = twin1.scatter(time, cumulative_mass, s=2, c="r", label="Cumulative Mass")
    ax.yaxis.label.set_color("b")
    twin1.yaxis.label.set_color("r")

    ax.legend(handles=[p1, p2])
    plt.show()

df = pd.read_csv(os.path.join(currentPath, "data/L2PRT1B_format.csv"))
plot_mass(df)