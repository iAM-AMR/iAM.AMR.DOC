

==============
Model Overview
==============

Current Models and Model Status
-------------------------------

The current models -- and model status -- can be found in the GitHub repository.



Organization via stories
++++++++++++++++++++++++
The models are organized primarily by ‘stories’, or bug-drug-host combinations of particular interest. Existing stories and their corresponding models are available in the iAM.AMR GitHub repository. 


Model Building
~~~~~~~~~~~~~~
Once the data are extracted from the literature, collated in -- and queried from -- the database, and processed by the R package, they are included in a model built around a robust model framework.

The iAM.AMR models are designed to predict the frequency of exposure of Canadians (and specifically, Ontarians) to antimicrobial-resistant bacteria from agri-food products. To do so, the models follow agri-food production along the farm-to-fork continuum – where possible, from birth (or hatch), through rearing, slaughter, processing, retail, and finally human consumption.

The models start with a baseline prevalence of resistance, derived from the earliest sampling point we have available – ideally as close to birth (or hatch) as possible. This prevalence of resistance is affected by practices at each stage of production; we term these practices ‘factors’ which affect resistance. These factors are grouped by stage of production: on-farm, at abattoir, and at retail. 

.. note:: The models only include binary factors (i.e. those described by yes or no). This means that a factor may be considered in one of two ways: as a risk (i.e. it increases the prevalence of resistance) or as being protective (i.e. it decreases the prevalence of resistance). It is important to note that this perspective (risk vs. protective) depends on the scenario. For example, changing the litter material of broiler chickens from straw to wood curls may increase the prevalence of resistance (a risk) – but if we have a scenario in which all litter material is already wood curls, this factor is only informative when we flip it, and consider the protective effect of changing the material to straw.

At each stage of production, we take the prevalence of resistance from the previous stage (e.g. baseline for on-farm, on-farm for abattoir, etc.) and update it, considering the effect of each factor (in combination with all others), and how often that factor is implemented in Canadian industry. We then pass this updated prevalence of resistance to the next stage. The calculations used to update the prevalence at each stage are identical, though as you will likely notice, we have more factors at the on-farm stage than any other.

After calculating the final prevalence of resistance at retail, we use the prevalence of bacterial contamination at retail (i.e. the recovery rate of the bacteria, derived from national surveillance programmes), estimates of population size, and consumer consumption behaviours, to derive the final output of the model -  the number of servings of the agri-food product that are contaminated with antimicrobial-resistant bacteria in a one week period
