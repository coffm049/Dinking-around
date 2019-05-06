import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use("seaborn-colorblind")

# number of replicate experiments and the resolution of each (how many points are taken.
reps = 4
res  = 20

exp= np.repeat(np.arange(1, reps +1 ), res) 

x= np.tile(np.arange(0,res, 1), reps)
y= x * 4
noise = np.random.normal(0, 2, res*reps)
df = pd.DataFrame({'exp' : exp, 'indep' : x, 'dep' : y, 'noise' : noise, 'real' : y + noise})
# plotting directly from pandas
#df.plot(x= 'indep', y= 'real', kind = 'scatter')
#plt.show()

experiments = np.unique(exp)



# plot all together
fig,ax = plt.subplots()

for experiment in experiments :
    df.sub = df[df['exp'] == experiment]
    ax.scatter(df.sub['indep'], df.sub['real'], label = "Experiment " +  str(experiment))
ax.set_title("Title name")
ax.set_xlabel("Independent variable")
ax.set_ylabel("Dependent variable")
plt.legend()
plt.show()



# plot separately
#fig, ax = plt.subplots(4)

#for experiment in experiments :
#    df.sub = df[df['exp'] == experiment]
#    ax[experiment - 1].plot(df.sub['indep'], df.sub['real'])
#plt.show()

fig.set_size_inches([1,1])
fig.savefig("delete.png")
