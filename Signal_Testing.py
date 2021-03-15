import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
import seaborn as sns


y = np.random.rand(1000)
x = np.arange(0, 0.5, 0.0005)
win = scipy.signal.hann(15)
filtered = scipy.signal.convolve(y, win, mode='same') / sum(win)

fig, axs = plt.subplots(nrows=2, sharex=True, sharey=True)

axs[0].plot(x, y, linestyle="-", marker=".", lw=0.3, markersize=1, color="red", alpha=0.5)
axs[0].set_title("Noisy Signal (HS)")


axs[1].plot(x, y, linestyle="", marker=".", color="red", markersize=1)
axs[1].plot(x, filtered, color="deepskyblue")
axs[1].set_title("filtered")
axs[1].set(xlabel="time [s]")


plt.savefig("filtering.pdf", bbox_inches="tight")
plt.show()

for i in range(8):
    y_new = y + 0.1*(i+1) * np.random.rand(1000) - 0.1*i * np.random.rand(1000)
    filtered_new = scipy.signal.convolve(y_new, win, mode='same') / sum(win)

    rms = np.sqrt(np.mean(np.square(filtered_new-filtered)))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Anomaly detection', fontsize=14)
    ax.set_xlabel('Time [s]', fontsize=12)
    ax.plot(x, filtered, color="gray", alpha=0.8)
    ax.plot(x, filtered_new, color="black")
    if rms > 0.08:
        color_fill = "lightcoral"
    else:
        color_fill = "lightgreen"
    ax.fill_between(x, filtered, filtered_new, color=color_fill)
    ax.grid()
    ax.set_ylim([0, 1])
    ax.xaxis.grid(linewidth=1.0)
    ax.yaxis.grid(linewidth=1.0)
    plt.savefig("AD_{}.png".format(i), bbox_inches="tight")
    plt.show()

sns.set()

y_new = y + 0.4 * np.random.rand(1000) - 0.4 * np.random.rand(1000)
filtered_new = scipy.signal.convolve(y_new, win, mode='same') / sum(win)

fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

axs[0, 0].plot(x, filtered, color="deepskyblue", alpha=0.3)
axs[0, 0].plot(x, filtered*1.5, color="darkorchid")
axs[0, 0].set_title("HigherScaling")

# ax.plot(x, y, linestyle="-", marker=".", lw=0.3, markersize=1, color="r", alpha=0.5)
# ax.set_title("Noisy Signal (HS)")

axs[0, 1].plot(x, filtered, color="deepskyblue", alpha=0.3)
axs[0, 1].plot(x, filtered+0.1, color="darkorchid")
axs[0, 1].set_title("Shift")

axs[1, 0].plot(x, filtered, color="deepskyblue", alpha=0.3)
axs[1, 0].plot(x, filtered_new, color="darkorchid")
axs[1, 0].set_title("Noise")

axs[1, 1].plot(x, filtered, color="deepskyblue", alpha=0.3)
x2 = 2*x
y2 = y[0:500]
filtered_2 = scipy.signal.convolve(y2, win, mode='same') / sum(win)
axs[1, 1].plot(x2[0:500], filtered_2, color="darkorchid")
axs[1, 1].set_title("Frequency")

plt.savefig("Different_anomalies.pdf", bbox_inches="tight")
plt.show()



