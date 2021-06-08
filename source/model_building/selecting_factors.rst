

Selecting Factors for Models
============================

This section is a guideline for the process of determining which factors are eligible for inclusion in the iAM models. You can begin this process after receiving your timber.

.. important:: If you make any corrections to the factors in your query of timber (which is likely unavoidable!), please make a note of which ones you have corrected, and always keep a copy of your initial query. As you evaluate each of your factors, whether individually or by discussing with an industry expert, please document these discussions as well, as well as any decisions and rationale regarding inclusion in or exclusion from your model. Eventually, this information will be captured within :ref:`CEDAR <cedar_database/cedar_database:Introduction>`.

Correct Factors
---------------

The process of model-building also serves as a chance to correct any errors that were made during the data extraction process.

Upon receiving your data query, the first thing you should do is run it through sawmill<link> :ref:`sawmill<data_extraction/sawmill:Introduction>`. Further steps are outlined below.

Check the scrap pile
~~~~~~~~~~~~~~~~~~~~

Sawmill will produce a file called the scrap pile if it was unable to calculate an odds ratio for one or more of the factors in your timber. If you’re not sure what sawmill or timber is please see <link>. There’s also a more detailed rundown of the scrap pile here <link>.

In some cases, these factors may have been extracted incorrectly, with one or more of the numerical fields necessary for odds ratio calculation missing from the timber. In this case, you will need to check the text of the paper to see if the key field(s) are available or not. If they are available, you can simply correct the factor and rerun it through sawmill. If the paper does not contain the fields you are missing, it will have to be excluded.

Check the prevalence table totals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are singled out for specific correction because a common error made during data extraction was to set the totals in prevalence tables to 100 (to represent 100%), but these are actually meant to capture the total number of isolates/animals/samples (whatever the correct unit of analysis is) in each group.

Check all factors
~~~~~~~~~~~~~~~~~

This may take awhile depending on how many factors you have in your query. However, it is an important step to check that the data extraction was done correctly, for each and every field captured.

Check these common reasons for exclusion
----------------------------------------

Factor is not modifiable
~~~~~~~~~~~~~~~~~~~~~~~~

While the general practice was to exclude non-modifiable, or immutable factors such as age, location, or breed <link> at the data extraction phase, it is not always clear whether a factor is modifiable. As such, there may be some non-modifiable factors in your query that you will need to exclude from your model.

Questions of whether a factor is modifiable or not are also context-dependent, and sometimes warrant consultation with an expert. Especially when it comes to factors related to management practices, a factor may be theoretically modifiable, but the implementation required may be cost prohibitive such that the factor is not practically modifiable. For example, liquid feeding systems in swine production require specialized, expensive equipment, so a major renovation would be required in order to convert to this system.

Selective media used at isolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Midway through the data extraction process, a decision was made to exclude factors for which selective media was applied at the isolation step. For the rationale behind this decision, please see here(__).

As this decision was only made midway through the process, it is likely that some factors were extracted that do not meet this criteria.

Appropriate production stage or sub-stage is unclear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It may be difficult to determine the appropriate production stage or sub-stage at which to place a factor in the model.  For instance, a study may state that “pigs from farms across the United States were sampled” without specifying whether these are finisher pigs, nursing piglets, sows, or weaned nursery pigs.

Multiple production stages or sub-stages are combined
+++++++++++++++++++++++++++++++++++++++++++++++++++++

It is also possible for AMR prevalence data to be aggregated across some combination of the farm, abattoir, and/or retail stages.

Other common examples of this particular reason for exclusion are:

1.       One or both groups compared in the factor are representative of aggregated samples from multiple farm sub-stages (i.e. a conventional vs organic production system factor, where AMR data in each comparison group is representative of both weaned nursery pigs and finishing pigs)
2.       Broiler and layer chickens are either aggregated together in both study groups, or one study group is made up of broilers and the other is made up of layers (even if this is not the focus of the comparison, i.e. a production system factor may compare organic broilers with conventional layers)
3.       Chickens and turkey (sometimes referred to collectively as poultry) treated similarly to broiler and layer chickens in point 2

.. Note:: This is especially relevant to cattle and swine, as they spend a significantly longer time at the farm stage—long enough for that farm stage to be split into multiple sub-stages.

Check these possible reasons for exclusion
------------------------------------------

Stage of AMR measurement differs from the stage of factor application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generally speaking, factors where the site of AMR measurement differs from the site of factor application (i.e. antimicrobial use on the farm, sampled at retail) are excluded from our models, as it is unclear which production stage they should be placed at.

There are a few potential exceptions to this rule, however:

Production system factors measured at retail
++++++++++++++++++++++++++++++++++++++++++++

If a production system factor (say organic vs conventional) is measured via retail meat samples, the factor can be applied at the retail stage in the model. However, if you have an abundance of factors eligible for modelling, including production system factors that are measured at farm, you should exclude those measured at retail.

Factors applied at farm and measured at abattoir
++++++++++++++++++++++++++++++++++++++++++++++++

If a factor is applied at the farm to a group of animals that are then followed to the abattoir for sampling, the factor may be eligible for inclusion in a model.

There are a few different possibilities for factors that fall into this category:

**Sampling was performed before any processing effects took place, and samples representative of individual animals (such as caecal swabs or droppings) have been taken:** 

The samples are likely representative of the farm stage.

**Sampling was performed before any processing effects take place, and “external” samples have been taken (i.e. a hide or skin swab, or a floor swab of the transport truck):**

The samples are likely representative of the farm and transport stages.

**Sampling has been performed after processing (most commonly via carcass swab):**

The samples are likely representative of the abattoir stage.

Un-specific antimicrobial use factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some papers may contain general antimicrobial use factors, where the antimicrobial(s) administered are not specified. If there is a large enough number of factors related to the use of specific antimicrobial(s) (i.e. ceftiofur use) eligible for inclusion in your model, these less well-characterized factors can likely be excluded.

Alternatively, these may be run separately from any specific AMU factors.

Factor is not well-characterized
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are factors that are not fully characterized in the paper, where comparison groups may be difficult to interpret. Here are a few examples:

Controlling flies with toxin:

- No info on what the “toxin” is
- The difference between the two groups is not clear: does one control flies with a toxin, while the other does not control flies at all? Or does the other group use an alternative method of control?

Infrequent disinfection vs frequent disinfection:

- How often is “infrequent”? How often is “frequent”?
- What is the disinfection agent/how are the authors defining disinfection?

The resistance outcome is a combination of antimicrobials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the exception of common combinations, i.e. imipenem and cilastatin, quinupristin and dalfopristin, or sulfamethoxazole and trimethoprim, which should appear as established options in the data extraction AMR dropdown menu, other factors must be associated with individual resistance outcomes to be eligible for inclusion in the iAM models.

General resistance, or multidrug resistance, where the resistance outcome is not specified, should also be excluded from models.

.. Tip:: Filter your query on the AMR field, with only blank cells selected. This may identify factors without that slipped through the extraction process, with an unspecific or combination resistance outcome.

Discuss with an industry expert
-------------------------------

Relevancy to the Canadian context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As the objective of the iAM project is to produce models that are applicable to the context of the Canadian agri-food industry, this is an important step in the factor selection process. There are two ways a factor may be relevant to the Canadian context:

1. It is used in Canada
2. There is a possibility of use/application in Canada AND this application/use could impact AMR
   
Factors in the second category will likely be included in the model, but run separately from the factors representative of the typical Canadian industry to explore “what-if” scenarios.

.. Hint:: For food-animal species that spend a longer time at the farm stage before processing (namely cattle and swine), relevancy of a factor may vary between sub-stages of the farm stage. For example, some antimicrobials administered to nursing piglets or weaned nursery pigs may be withdrawn for part or all of the finishing stage due to residue concerns.

Frequency of occurrence
~~~~~~~~~~~~~~~~~~~~~~~

The frequency of occurrence of each factor in the Canadian context should be determined by consulting with an expert, and captured at the frequency node of your model.

If you have too many factors in your model…
-------------------------------------------

If you are looking to cut down on the number of factors in your model, or need to due to Analytica constraints, a good place to start is to identify papers that are measuring the same factor, in the same host or host sub-population. For example, you might have two papers measuring the effect of ceftiofur use in piglets. In this case, you can choose to include only the study with the larger sample size to cut down on factors.

.. Tip:: Your standard error is a proxy for sample size, where a large SE is representative of a small sample size

Other model components
----------------------

The following elements are handled by the iAM.AMR.HUB<link> module:

1. Baseline prevalence and distribution
2. Bacterial recovery at retail
3. Consumption from the Foodbook