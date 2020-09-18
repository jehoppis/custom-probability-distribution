import numpy as np
import matplotlib.pyplot as plt


def roll(d, split=None, r=[.5, .5], weight_left=.5, n=1):
    weight_right = 1. - weight_left
    if split is None:
        split = d/2
    split = int(split)
    r_left = r[0]
    r_right = r[1]
    if r_right == 1.:
        p_right = [1./(d-split) for _ in range(d-split)]
    elif 0 < r_right < 1:
        p_right = [(r_right ** i) * ((1.-r_right) / (1-r_right**(d-split))) for i in range(d-split)]
    if r_left == 1.:
        p_left = [1./split for _ in range(split)]
    elif 0 < r_left < 1:
        p_left = [(r_left**i) * ((1.-r_left) / (1-r_left ** split)) for i in range(split-1, -1, -1)]
    p_total = np.concatenate((weight_left*np.array(p_left), weight_right*np.array(p_right)))
    print(p_total)
    sample = np.random.choice([i for i in range(1, d+1)], size=n, p=p_total)
    return sample


if __name__ == "__main__":
    d_ = 20
    power = 7
    r_ = [.85, .75]
    split_ = 14
    weight = .65

    one_sample = roll(d_, split=split_, r=r_, weight_left=weight, n=10**power)
    counts, bins = np.histogram(one_sample, bins=np.arange(1, d_+2) - 0.5,)
    plt.hist(bins[:-1], bins, weights=counts/10**power, density=False,
             label=f'1d{d_}, r={r_}, split={split_}, weight_left={weight}', rwidth=0.8)
    plt.xticks(np.arange(1, d_+1))
    plt.ylabel('Relative Frequency')
    print(one_sample[0:20])
    print('Avg', np.average(one_sample))
    print('Median', np.median(one_sample))
    plt.legend()
    plt.show()

