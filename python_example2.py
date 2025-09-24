import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import sys

def python_example2(samples=10000):
    rng = np.random.default_rng()
    data = rng.normal(100, 6, (samples, 2))

    fig, axs = plt.subplots(2,2, figsize=(10,8))

    axs[0,0].hist2d(data[:,0], data[:,1], bins=100, range=[[50,150],[50,150]], cmap='viridis')
    axs[0,0].set_title("2D Gaussian")

    data2 = np.vstack([data, rng.uniform(50,150,(samples//3,2))])
    axs[0,1].hist2d(data2[:,0], data2[:,1], bins=100, range=[[50,150],[50,150]], cmap='viridis')
    axs[0,1].set_title("2D Gaussian + offset")

    u = rng.uniform(0,1,samples*10)
    xvals = 1/(1-u*(1-1/11))*10 + 40
    yvals = rng.uniform(50,150, samples*10)
    data3 = np.vstack([data, np.column_stack([xvals, yvals])])
    axs[1,0].hist2d(data3[:,0], data3[:,1], bins=100, range=[[50,150],[50,150]], cmap='viridis', norm=LogNorm())
    axs[1,0].set_title("2D Gaussian + offset2")

    data4 = np.vstack([data, rng.normal(100,20,(samples//2,2))])
    axs[1,1].hist2d(data4[:,0], data4[:,1], bins=100, range=[[50,150],[50,150]], cmap='viridis')
    axs[1,1].set_title("Double 2D Gaussian")

    fig.tight_layout()
    fig.savefig("canvas2d_py.png")

if __name__ == "__main__":
    samples = 10000
    if len(sys.argv) > 1:
        samples = int(sys.argv[1])
    python_example2(samples)






