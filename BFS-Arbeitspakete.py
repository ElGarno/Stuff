import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arbeitspakete_map = {
  1: 'Gesamtkopplung',
  2: 'Nachbearbeitung und Scan der bisher abgeg. Var',
  3: 'Pulstest der bisher abgeg. Var.',
  4: 'Abguss der gekoppelt optimierten Geo',
  5: 'Nachbearbeitung und Scan gekoppelt opt. Geo',
  6: 'Pulstest gekoppelt optimierte Geo',
  7: 'Abschlussbericht'
}

risiko_APs = np.array([0.4, 0.2, 0.3, 0.1, 0.2, 0.3, 0.0])
aufwand_APs = np.array([20, 3, 1, 2, 2, 1, 10])

roadmap_df = pd.DataFrame([risiko_APs, aufwand_APs], columns=arbeitspakete_map.values())
zipped_roadmap = zip(risiko_APs, aufwand_APs)

X = np.arange(1, 8)
# plt.figure()
# roadmap_df.plot(kind="bar", rot=0)
# plt.xticks([1, 2], rotation='vertical')
# plt.tick_params(axis='x', labelsize=6)
# plt.ylabel('Abgeschätztes Risiko')
# plt.title('Aufwands- und Risikoschätzung')
# plt.plot()
# plt.show()

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
rgb_max = 255.0
bar1 = ax1.bar(X + 0.0, risiko_APs*100, label='Risiko', color=(223.0/rgb_max, 0.0, 36.0/rgb_max), width=1.0/3.0)
bar2 = ax2.bar(X + 1.0/3.0, aufwand_APs, label='Aufwand', color=(90/rgb_max, 124/rgb_max, 145/rgb_max), width=1.0/3.0)
bar_labels = [bar1, bar2]
ax1.legend(bar_labels, [bar_id.get_label() for bar_id in bar_labels])
ax1.set_xticks(X)
ax1.set_xticklabels(['AP1', 'AP2', 'AP3', 'AP4', 'AP5', 'AP6', 'AP7'], rotation='vertical', fontsize=6)
ax1.set_ylabel('Abgeschätztes Risiko in %')
ax1.set_ylim([0, 100])
ax2.set_ylabel('Aufwand in AT')
plt.title('Aufwands- und Risikoschätzung')
plt.plot()
plt.grid()
plt.show()
fig.savefig('Aufwand_Risiko_AP_BFS.png')
