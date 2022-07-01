
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

1. **Baseline Probability**: unit is the isolate if informed by CIPARS data (e.g., the baseline probability of resistant E. coli would be the number of resistant E. coli isolates divided by the total number of E. coli isolates assayed for resistance)
2. **Factors**: unit varies depending on the extracted data
3. **Frequencies of Occurrence**: unit is the farm (e.g., 50% of swine farms in Canada use penicillins)
4. **Bacterial Recovery Rate at Retail**: this represents the proportion of servings of a particular meat type that are contaminated with a particular bacteria (unit = serving) (e.g., 33% of retail chicken servings sampled by CIPARS were contaminated with Salmonella)
5. **Prevalence of Servings Contaminated with AMR Bacteria**: this represents the proportion of servings of a particular meat type that are contaminated with a particular resistant bacteria (unit = serving) (e.g., 90% probability (prevalence) of resistant Salmonella at retail in chicken (from factors) * 33% of chicken meat servings contaminated with Salmonella = 29.7% of servings of chicken meat contaminated with resistant Salmonella)
6. **Consumption Rate**: this represents the proportion of people consuming a particular type of meat in a one-week period (unit = persons)
7. **Exposure**: this represents the number of persons consuming a particular meat type who are at risk of ingesting antimicrobial-resistant bacteria from this meat in a one-week period (unit = persons)

As a result of the variety of units used in the iAM modelling framework, this assumption applies across the model. 

Other Assumptions
~~~~~~~~~~~~~~~~~

1. It is assumed that each CIPARS retail meat sample used to determine the bacterial recovery rate at retail is the same size as an average-sized serving of meat
2. It is assumed that everyone who consumes a particular type of meat consumes at least one average-sized serving in a one-week period

Model Structure and Inputs
--------------------------

Those of you writing papers on iAM.AMR models will likely have a table in your Methods section that describes the model inputs, their values, and the data sources used. 

Up-to-date Content
~~~~~~~~~~~~~~~~~~

If you're looking for a more detailed (and up-to-date!) overview of the model equations, input parameters, and distributions, check out the :ref:`iAM.AMR.HUB model <models/hub:iAM.AMR.HUB>`. You can click through the definitions of any inputs (like the baseline probability and bacterial recovery rate), as well as the functions used to calculate distributions for these inputs.

.. tip:: You can export this model-related information from Analytica and into a spreadsheet using the Model Documentation library in Analytica. There are instructions for accessing the Model Documentation library :ref:`here <models/hub:Model Documentation>`. 

Example Structure
~~~~~~~~~~~~~~~~~

An example layout of the structure for such a table can be found in `Courtney Primeau's thesis <https://atrium.lib.uoguelph.ca/xmlui/handle/10214/17935>`_.
Chapter 3 pertains to the iAM.AMR model that she developed. Relevant tables begin at page 126.

.. important:: Our terminology has changed from Exposure/Referent (Table 3.1) to Factor/Comparator, see up-to-date terminology :ref:`here <10_reference/style_guide:Communications Style Guide>`.

.. important:: We have switched to using the standard error of the log(odds ratio) (as opposed to the standard error of the odds ratio) in the models since this thesis was written. Our R package, sawmill, is set up to deliver the odds ratio and the standard error of the log(odds ratio) as outputs for the models, see :ref:`here <model_building/processing_cedar_queries:Planks>`.

