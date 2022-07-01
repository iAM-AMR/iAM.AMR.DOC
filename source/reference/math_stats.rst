

Math and Stats
==============





Beta
----
Prevalence, in the context of epidemiology, is the proportion of a population expressing a characteristic of interest. A deterministic estimate of prevalence can be calculated as k/n, where k is the number of ‘positive’ units, and ‘n’ represents the total number of units assayed.

Alternatively, we can express our estimate of prevalence probabilistically, using a Beta distribution. In this context, we think of each assay as a Bernoulli trial (or as a series of binomial trials).


Meta-analysis
-------------

Meta-analysis is a technique for aggregating the findings of related studies.

A meta-analysis is basically a weighted average of the effect where:

- Generally, we use an inverse weighting scheme, where studies are weighted by the inverse of their variance
- Higher variance = small sample size = less certainty = less weight in average

Types of Models
~~~~~~~~~~~~~~~

A fixed-effects model assumes each study demonstrates a common intervention effect:

- There is a true, constant, but unknown effect - variation arises from sampling error
- Applicable when all possible studies/objects are enumerated
- Goal of internal validity

A random effects model assumes there is a common mean intervention effect:

- There is a mean, unknown effect - variation arises from sampling error and differences between studies
- Useful when we can’t enumerate all studies/objects; or we expect more to arise in future
- Goal of external validity

“the relative weights assigned under random effects will be more balanced than those assigned under fixed effects. As we move from fixed effect to random effects, extreme studies will lose influence if they are large, and will gain influence if they are small.”