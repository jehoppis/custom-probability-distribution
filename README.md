# custom-probability-distribution
I was inpsired by Dungeons and Dragons to come up with an alternative to rolling a die with a uniform distribution.

The function 'roll' creates a custom probability distribution on the integers j satisfying a <= j <= b with a parameter r (r for ratio). As r goes to 0, the probability distribution approaches either a constant distribution on the median if there are an odd number of integers or a 50-50 distribution on the middle two integers if there are an even number of integers. As r goes to 1, the probability distribution approaches a uniform distribution. 
