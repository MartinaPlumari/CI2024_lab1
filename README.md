# CI2024_lab1
First lab of the Computational Intelligence course

## Set Cover Optimization Problem

Solution to the Set Cover Optimization Problem based on the Steepest Step RMHC algorithm. I added an adaptive temperature mechanism to the algorithm finding better results especially for the third configuration.
Some other versions of the algorithm were tested but the results were not as good as the ones presented here.
Unfortunately, I was not able to run many tests with the bigger configurations because of the time it took to run the algorithm, and this resulted in not so good performances for the last three configurations.

## Results

In the following table I report the best result I got for the configuration I set on the `set-cover.py` file.

| Instance | Universe Size | Num Sets | Density | Cost           | Taken Sets %   | Num of Steps   |
|----------|---------------|----------|---------|----------------|----------------|----------------|
|     1    |      100      |    10    |    .2   |   279          |      90.0%     |    2070        |
|     2    |      1000     |    100   |    .2   |   6593         |      20%       |    2590        |
|     3    |      10000    |    1000  |    .2   |   236615       |      5.6%      |    8950        |
|     4    |      100000   |   10000  |    .1   |   49241019     |      19.61%    |    2800        |
|     5    |      100000   |   10000  |    .2   |   101652323    |      18.9%     |    4230        |
|     6    |      100000   |   10000  |    .3   |   170117391    |      20.23%    |    2840        |

## References

I mainly based my work on the theory and the code shown to us during lesson. I also learned by exchanging ideas with my collegue Daniel Bologna.
