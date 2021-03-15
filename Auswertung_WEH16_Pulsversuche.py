from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

dict_pulsprueflinge = {'#test_housing': [14, 15, 9, 10, 11, 12, 1, 2, 3, 4],
                       'wall-thickness': [0.8, 0.7, 0.35, 0.93, 0.26, 0.65, 0.7, 1.24, 1.03, 1.3],
                       'load changes': [16000., 600., 8500., 169000., 100., 16600., 40000., 10000000., 232000.,
                                        10000000.]}

df_pulsating_tests = pd.DataFrame(dict_pulsprueflinge, columns=['#test_housing', 'wall-thickness', 'load changes'])
df_pulsating_tests.sort_values(by=['wall-thickness'], inplace=True)
df_pulsating_tests = df_pulsating_tests[~df_pulsating_tests['#test_housing'].isin([14, 15])]

# plot
# sns.set()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Load-changes over material thickness', fontsize=14)
ax.set_xlabel('Wall thickness [mm]', fontsize=12)
ax.set_ylabel('Load changes [-]', fontsize=12)
ax.set_yscale('log')
ax.plot(df_pulsating_tests['wall-thickness'], df_pulsating_tests['load changes'], linewidth=2)
ax.scatter(df_pulsating_tests['wall-thickness'], df_pulsating_tests['load changes'])
ax.grid()
ax.xaxis.grid(linewidth=1.0)
ax.yaxis.grid(linewidth=1.0)
plt.savefig("testrig.png", bbox_inches="tight")
plt.show()
