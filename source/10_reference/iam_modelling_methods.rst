
=========================
iAM.AMR Modelling Methods
=========================

This chapter serves as a reference to anyone writing a paper that describes an iAM.AMR scenario model.
Here, the methodological properties consistent across all iAM.AMR models are described.

Model Assumptions
-----------------

There are a few key assumptions inherent to the iAM.AMR modelling framework.


Independence
~~~~~~~~~~~~

*Assumption One: Factors occur independently of each other both within and across each stage of the farm-to-fork pathway.*

For example, we assume that the occurrence of ceftiofur use at the farm does not change whether or not enrofloxacin use occurs at the farm.
Similarly, we assume that the occurrence of ceftiofur use at the farm does not change whether or not disinfectant use occurs at the abattoir.


Concurrence
~~~~~~~~~~~

*Assumption Two: Factors happen concurrently within each stage of the farm-to-fork pathway.*

For example, we assume that all factors occurring at the abattoir come into effect at the same time.

However, stages can be split into multiple, sequential sub-stages (e.g., the farm stage can be split into nursing piglets, weaned piglets, grower-finisher pigs, etc.).


Units Scale Proportionally
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Assumption Three: All units scale proportionally throughout the model.*

For example, we assume that if 30% of farms are exposed to the effect of a particular factor, then 30% of animals and 30% of their bacteria are also exposed to the effect of that factor.
This allows us to use the farm as the unit for the factors' frequencies of occurrence, while still using data from the literature that represent isolates, samples, animals, etc. to calculate the odds ratio for each factor.

To elaborate further, there are a variety of units used at different parts of the farm-to-fork pathway:

1. **Baseline Probability**: unit is the isolate if informed by CIPARS data (e.g., number of resistant E. coli isolates out of total E. coli isolates assayed for resistance)
2. **Factors**: unit varies depending on the extracted data
3. **Frequencies of Occurrence**: unit is the farm (e.g., 50% of swine farms in Canada use penicillins)
4. **Bacterial Recovery Rate at Retail**: unit is a "serving" of meat contaminated with a particular bacteria (e.g., 33% of retail chicken servings sampled by CIPARS contained Salmonella)
5. **Prevalence of Servings Contaminated with AMR Bacteria**: unit is a "serving" of meat contaminated with a particular resistant bacteria (e.g., 90% probability (prevalence) of resistant Salmonella at retail in chicken (from factors) * 33% of servings of chicken meat contaminated with Salmonella = 29.7% servings of chicken meat contaminated with resistant Salmonella)
6. **Consumption Rate**: this represents the proportion of people (unit = people) consuming a particular type of meat in a one-week period
7. **Exposure**: this represents the number of servings at risk (unit = servings) in a one-week period

Please note the following sub-assumptions to Assumption Three:

1. It is assumed that each CIPARS retail meat sample used to determine the bacterial recovery rate at retail is the same size as an "average sized" serving of meat
2. It is assumed that everyone who consumes a particular type of meat consumes average-sized servings
3. Since the Exposure is calculated by multiplying the prevalence of servings contaminated with AMR bacteria by the number of people consuming the particular type of meat in one week, it may seem that the appropriate unit of Exposure would be the # of people at risk in a one-week period (rather than the # of servings at risk). However, our Assumption Three allows us to assume that the % of servings contaminated with AMR bacteria scales proportionally to the % weekly meat intake of one person that is contaminated with AMR bacteria.

As a result of the variety of units used in the iAM modelling framework, this assumption applies across the model. 


Model Structure and Inputs
--------------------------

If you're looking for a more detailed overview of the model structure, input parameters, and distributions, check out the :ref:`iAM.AMR.HUB model <models/hub:iAM.AMR.HUB>`. You can click through the definitions of any inputs (like the baseline probability and bacterial recovery rate), as well as the functions used to calculate distributions for these inputs.

.. tip:: You can export this model structure information from Analytica using the Model Documentation library in Analytica. There are instructions for accessing the Model Documentation library :ref:`here <models/hub:Model Documentation>`. 

