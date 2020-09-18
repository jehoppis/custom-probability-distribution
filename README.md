# custom-probability-distribution
I was inpsired by Dungeons and Dragons to come up with an alternative to rolling a die with a uniform distribution.

The function 'roll' creates a custom probability distribution on the integers j satisfying 1 <= j <= d with parameters split, r=[r_left, r_right], weight_left, and n. The probability distribution is built by splitting the integers from 1 to d into two parts determined by split, and building a probablilty distribution on each part, then taking a weighted sum determined by weight_left. Both distributions are defined using the formula
1+r+r^2+...+r^n = (1-r^(n+1))/(1-r).
The parameter n is the size of the output. In the example picture, n=10^7 was used, then the counts in the histogram were divided by n.
