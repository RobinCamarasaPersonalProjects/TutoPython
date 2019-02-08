import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return np.sin(x)


def ex_1(f, x_min, x_max):
    x = np.linspace(x_min, x_max, 1001)
    plt.plot(x, f(x))
    plt.show()


def ex_2(mu, sigma, nb):
    x = mu + sigma * np.random.randn(nb)
    plt.hist(x)
    plt.show()


def ex_3():
    mean = np.load('../data/mean_score.npy')
    men_height = np.load('../data/men_height.npy')
    std_score = np.load('../data/std_score.npy')
    fig, ax = plt.subplots()
    ax.bar(men_height, mean, 0.04, yerr=std_score)
    ax.set_title('Score obtained')
    ax.set_xlabel('Men height')
    ax.set_ylabel('Score')
    fig.tight_layout()
    plt.show()