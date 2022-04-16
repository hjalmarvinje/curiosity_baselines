import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('results/ppo_breakout/run_2/progress.csv')

df = [df['GameScore/Average'], df['intrinsic_rewards/Average']]

sns.set_theme(style="darkgrid")

sns.lineplot(data = df, ci= 'sd')
plt.show()
#print(df['Diagnostics/Iteration'], df['GameScore/Average'])
#plt.plot(df['Diagnostics/Iteration'], df['GameScore/Average'])
#plt.xlabel('Iteration')
#plt.ylabel('GameScore/Average')
#plt.show()

