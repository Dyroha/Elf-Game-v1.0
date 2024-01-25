import pandas as pd
from simulation import *
import matplotlib.pyplot as plt
import statistics

elves = [Character(), Lumberjack(), OneManBand(), Cosy(), WinterWitch(), ReindeerWrangler(), Meteorologist(), Mystic()]
sim = Simulation([7,14,21], elves)
out = sim.runSimulation(1000)
# print([(type(x).__name__ , x.getAverageEarnings()) for x in out])
# print(out[1].run_earnings)
fig, axis = plt.subplots(1,8, figsize=(10,6), sharey=True)
for x in range(len(out)):
    df = pd.DataFrame({'Earnings':out[x].run_earnings})
    print('''type(out[x]).__name__  + '''": mean = %2d, median = %2d, standard deviation = %2d" % (statistics.mean(df['Earnings']), statistics.median(df["Earnings"]), statistics.stdev(df['Earnings'])))
    df['Earnings'].value_counts(sort=False, bins=range(0,20000,500)).plot.bar(ax=axis[x], xticks=[], yticks=[], title='''type(out[x]).__name__''', align="edge", width=1.0)

fig.tight_layout()  
plt.show()
