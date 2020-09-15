import numpy as np
import matplotlib.pyplot as plt

'''The function 'roll' uses a custom probability distribution to roll a die of a given range. If the die
    is even sided, the distribution is defined by splitting the number of sides in 2, and for i in 
    range(n/2, 0, -1), the probability of that side being chosen is P = C * r**i, where C is a constant
    chosen so that (in the end) the probabilities sum to 1. For i in range(n/2+1, n+1), the probabilities
    are mirrored so that n/2+1 has the same chance as n/2, n/2+2 has the same chance as n/2-1, ... , and
    n has the same chance as 1. If the die is odd sided, there are two sides of equal length with the 
    median in between. The two sides are handled similarly as to the even case, and a probability is
    assigned to the median that satisfies 'As r goes to 0, the distribution approaches a constant
    distribution.' and 'As r goes to 1, the distribution approaches the uniform distribution.'''


def roll(a, b, n, r=.85):
    if r != 1.0:
        if (b+1 - a) % 2 == 0:
            k = int((b+1-a)/2)
            even_dist_prob = [0.5 * (r ** i) * ((1.-r) / (1 - r ** k)) for i in range(k-1, -1, -1)] + \
                             [0.5 * (r ** i) * ((1.-r) / (1 - r ** k)) for i in range(0, k)]
            print(even_dist_prob[0:k])
            sample = np.random.choice(np.arange(a, b+1), size=n, p=even_dist_prob)
            return sample
        elif (b+1 - a) % 2 == 1:
            k = int((b-a)/2)
            odd_dist_prob = [0.5 * ((2*k*r) / (2*k+1)) * (r ** i) * ((1.-r) / (1 - r ** k))
                             for i in range(k-1, -1, -1)] + \
                            [1 - (2*k*r) / (2*k+1)] + \
                            [0.5 * ((2*k*r) / (2*k+1)) * (r ** i) * ((1.-r) / (1 - r ** k))
                             for i in range(0, k)]
            print(odd_dist_prob[0:k+1])
            sample = np.random.choice(np.arange(a, b + 1), size=n, p=odd_dist_prob)
            return sample
    else:
        sample = np.random.choice(np.arange(a, b+1), size=n)
        return sample

if __name__ == "__main__":
    n = 20
    p = 7

    one_sample = roll(1, n, 10**p, r=.85)
    plt.hist(one_sample, density=False, bins = np.arange(1, n+2) - 0.5, rwidth=0.8)
    plt.xticks(np.arange(1, n+1))
    print(one_sample[0:20])
    print('Max', np.max(one_sample))
    print('Min', np.min(one_sample))
    print('Avg', np.average(one_sample))
    plt.show()
