# Probability

- [Probability](#probability)
  - [Resources](#resources)
  - [Tasks](#tasks)
    - [Task0](#task0)
    - [Task1](#task1)
    - [Task2 (code is incomplete)](#task2-code-is-incomplete)
    - [Task3,4](#task34)
    - [Task5](#task5)
    - [Task8](#task8)

## Resources

* [Poisson Distribution](https://onlinestatbook.com/2/probability/poisson.html)
  * Zero factorial, `0!` is equal to `1`.
## Tasks

### Task0

* [finding lambda](https://www.youtube.com/watch?v=AS0cLTiVrRY)

* [numpy.random.poisson](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.poisson.html)

### Task1

Use [piosson distribution](#resources) to calculate p of a given mu (lambtha in this project's code)


### Task2 (code is incomplete)

[Poisson CDF](https://en.wikipedia.org/wiki/Cumulative_distribution_function) refers the the probability of "at most" x value. Contrast with PDF (proabability of exactly) that was used in task1

* for example, the CDF of 3 is equal to the PDF of 3 + PDF of 2 + PDF of 1 + PDF of 0

[formula](https://en.wikipedia.org/wiki/Poisson_distribution): `e^(-λ) * Σ(j=0, [k]) λ^j / j!`

### Task3,4

[exponential distribution](https://byjus.com/maths/exponential-distribution/) uses `lambda = 1/average` in it's formulae.

x represents the time, so it must be higher than 0 to have any probability above 0.
* in this task, **0 must not be considered a special case**. It will instead return an impossible probability value.

### Task5

cumulative exponential distribution formula can be found [here](https://www.statology.org/exponential-distribution/)

### Task8

[z-score](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/z-scores/a/z-scores-review)

In most resources:
* σ is standard deviation
* σ^2 is variance
* μ is mean
* x is data point in question
* z is z-score
