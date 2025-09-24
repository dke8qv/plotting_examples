import numpy as np
import matplotlib.pyplot as plt

def cpp_example_py(samples=10000):
    rng = np.random.default_rng()
    data = rng.normal(100, 6, size=samples)

    # single histogram
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    counts, bins = np.histogram(data, bins=100, range=(50, 150))
    bin_centers = 0.5*(bins[1:] + bins[:-1])
    ax1.errorbar(bin_centers, counts, yerr=np.sqrt(counts), fmt='o', label="Gauss")
    ax1.set_title("random gauss")
    ax1.set_xlabel("x")
    ax1.set_ylabel("frequency")
    ax1.legend()
    fig1.tight_layout()
    fig1.savefig("canvas1_py.png")
    
    # 2x2 grid
    fig2, axs = plt.subplots(2, 2, figsize=(10, 8))

    # original Gaussian
    counts, bins = np.histogram(data, bins=100, range=(50, 150))
    bin_centers = 0.5*(bins[1:] + bins[:-1])
    axs[0, 0].errorbar(bin_centers, counts, yerr=np.sqrt(counts), fmt='o')
    axs[0, 0].set_title("Gauss;x;frequency")

    # gaussian plus offset
    data2 = np.concatenate([data, rng.uniform(50, 150, size=samples // 3)])
    counts, bins = np.histogram(data2, bins=100, range=(50, 150))
    bin_centers = 0.5*(bins[1:] + bins[:-1])
    axs[0, 1].errorbar(bin_centers, counts, yerr=np.sqrt(counts), fmt='o')
    axs[0, 1].set_title("Gauss+offset")

    # gaussian plus offset2
    u = rng.uniform(0, 1, size=samples * 30)
    xvals = 1 / (1 - u * (1 - 1/11.0))   # sample from 1/x^2 on [1,11]
    xvals = 10 * xvals + 40
    data3 = np.concatenate([data, xvals])
    counts, bins = np.histogram(data3, bins=100, range=(50, 150))
    bin_centers = 0.5*(bins[1:] + bins[:-1])
    axs[1, 0].errorbar(bin_centers, counts, yerr=np.sqrt(counts), fmt='o')
    axs[1, 0].set_yscale("log")
    axs[1, 0].set_title("Gauss+offset2")

    # double gaussian
    data4 = np.concatenate([data, rng.normal(100, 20, size=samples // 2)])
    counts, bins = np.histogram(data4, bins=100, range=(50, 150))
    bin_centers = 0.5*(bins[1:] + bins[:-1])
    axs[1, 1].errorbar(bin_centers, counts, yerr=np.sqrt(counts), fmt='o')
    axs[1, 1].set_title("Double Gaussian")

    fig2.tight_layout()
    fig2.savefig("canvas2_py.pdf")

if __name__ == "__main__":
    cpp_example_py()
    print("Saved plots: canvas1_py.png and canvas2_py.pdf")


