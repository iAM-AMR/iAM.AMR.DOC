

Selecting Factors for Models
============================

This section is a guideline for the process of determining which factors are eligible for inclusion in the iAM models. You can begin this process after receiving your timber.

.. important:: If you make any corrections to the factors in your query of timber (which is likely unavoidable!), please make a note of which ones you have corrected, and always keep a copy of your initial query. As you evaluate each of your factors, whether individually or by discussing with an industry expert, please document these discussions as well, as well as any decisions and rationale regarding inclusion in or exclusion from your model. Eventually, this information will be captured within :ref:`CEDAR <cedar_database/cedar_database:Introduction>`.


Factor Identifier
~~~~~~~~~~~~~~~~~
The factor identifier is automatically generated by the :ref:`sawmill R package <data_extraction/Sawmill:The sawmill R Package>`, in the format **A#####_Name_of_Factor** where:

* **A** is either 'R' for a standard factor, or 'M' for a meta-analysis
* **#####** is the factor or meta-analysis number

Where multiple factors inform a single node:

* and one or more of the factors is a meta-analysis, use the meta-analysis identifier with the lowest number
* and all of the factors are not meta-analyses, use the identifier with the lowest number
* and all of the factors are meta-analyses, use the identifier with the lowest number

In some instances, it may be appropriate to deviate from this schema – care should be taken to maintain consistency despite these deviations.


Correct Factor Extraction
-------------------------

The process of model-building also serves as a chance to correct any errors that were made during the data extraction process.

Upon receiving your data query, the first thing you should do is run it through :ref:`Sawmill <data_extraction/sawmill:Introduction>`. This will catch the biggest problems with the raw data for you, but *not all of them!* **This is why manual validation of all data against the full-text of each paper is a crucial step in the model-building process.** Please see below for further detail.

.. caution::
   Model-building is an iterative process, so you will need to run your query through Sawmill **multiple** times.
   It is unavoidable that corrections will be made to both the raw data (the numbers used to calculate the odds ratio), as well as fields like the factor title. 
   These changes affect other fields generated by sawmill that are then entered into the models.

Check the scrap pile
~~~~~~~~~~~~~~~~~~~~

Sawmill will produce a file called the scrap pile if it was unable to calculate an odds ratio for one or more of the rows of data in your timber (where each row of data = a given factor's association with resistance to an individual antimicrobial). If you’re not sure what sawmill or timber is please see :ref:`Sawmill <model_building/sawmill:Introduction>`. There’s also a more detailed rundown of the scrap pile :ref:`here <model_building/processing_cedar_queries:Scrap pile>`.

In most cases, rows end up in the scrap pile because they were extracted incorrectly, with one or more of the numerical fields necessary for odds ratio calculation missing from the timber. In this case, you will need to check the text of the paper to see if the key field(s) are available or not. If they are available, you can simply correct the row(s) (please follow the instructions :ref:`here <model_building/selecting_factors:Check all factors and resistance outcomes>` when making this correction) and rerun your timber through sawmill. If the paper does *not* contain the fields you are missing, or does not provide them in the needed units, the row(s) will have to be excluded.

Check the reference notes
~~~~~~~~~~~~~~~~~~~~~~~~~

Besides the raw timber file, notes made by the data extractors are also provided to you.
These notes often specify challenges with interpreting the data, or fields they were uncertain about when extracting. As such, these notes are an excellent guide for pinpointing potential errors with the extracted factors and associations with resistance.

Check all factors and resistance outcomes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The steps in this section should be followed for **each and every row of data in your timber**. 
You can start with anything that was placed into the scrap pile during your first run-through sawmill, as this is where the most significant errors will be, and then expand out to the rest of your timber.
This may take awhile depending on how many rows of data you have in your timber. However, it is an important step to check that the data extraction was done correctly, **for each and every field captured.**

This includes validation of the following against the full-text:

1. Factor title and description
2. The host sub-population (i.e. weaner pigs, finishing pigs, dairy calves, feedlot cows)
3. The microbe and microbial subtype
4. The production stages at which the the factor was applied (i.e. where the factor groups were allocated or where the intervention was applied) and observed (i.e. where the sampling took place).
5. The antimicrobial assayed for resistance
6. The unit of analysis (i.e. this would be isolate if the data is presented as % resistant isolates, or animal if the data is presented as % resistant animals, or flock/pen/herd/sample....etc.)
7. **All of the raw numerical data that goes into the odds ratio calculation** (see :ref:`important sub-section below <model_building/selecting_factors:Checklist for getting the correct odds ratio>`)

... and **all other fields in the timber!**

Checklist for getting the correct odds ratio
++++++++++++++++++++++++++++++++++++++++++++

This process is trickier than it seems! The following steps are key in making sure that your odds ratio is correct (and is correctly calculated by sawmill!):

1. Return to the full text, and determine which data are extractable
2. Make sure that the *res_format* field reflects the format of the extractable raw data: Contingency Table, Prevalence Table, or Odds Ratio. We always prefer raw data if available, so the order of preference if multiple formats are available is Contingency > Prevalence > Odds Ratio.
3. Make sure you have all the fields needed to calculate the odds ratio (see :ref:`here <model_building/sawmill:Acceptable grains>` for a breakdown of the required fields for each format).
4. Make sure you have selected the correct unit of analysis in the *res_unit* field
5. If the format of the extractable data is a Contingency Table or Prevalence Table, make sure that **both the AMR counts/prevalence and the totals are available in the same units**. If the units differ, an odds ratio cannot be correctly calculated, and so the data must be excluded.For example, if AMR prevalence is reported as % resistant isolates, the totals for each group must be reported in # isolates (not # samples or # animals, unless it is explicitly mentioned somehwere in the paper that 1 sample or 1 animal is equivalent to 1 isolate).
6. Make sure that the totals represent the total # of units (i.e. isolates, samples, animals) confirmed to be positive for the same bacteria as that for which resistance is being measured. For example, if the # of ceftiofur-resistant E. coli isolates is being reported, ensure that your totals for each group represent the total number of E. coli isolates, not the total number of coliforms or Enterobacteriaceae, for example, as these would encompass other bacterial species that are not E. coli.

.. hint:: If the group totals are not provided in the figure caption, do not despair! They can sometimes be parsed out of the methods section or surrounding text. If you are having difficulty or would like a second pair of eyes, please get in touch with Charly Phillips for assistance.

Other common errors to watch out for
++++++++++++++++++++++++++++++++++++

1. Ensure that there is no selective media usage at the isolation step (see this section for more information: :ref:`About Selective Media <data_extraction/data_extract_rules:About Selective Media>`, as there are important nuances and exceptions to this rule such as for Campylobacter, ESBLs, and when selective media is used as an AST method). In this case, selective media refers to *isolation media that contain antimicrobials to which the bacteria of interest does not have* `intrinsic resistance <https://www.open.edu/openlearn/ocw/mod/oucontent/view.php?id=75461&section=2.1>`_, not other types of selective media that do not contain antimicrobials. As the decision to exclude associations with resistance measured using selective media usage at isolation was made midway through the data extraction process, it is likely that some factors and/or associations with resistance were extracted that do not meet this criteria.

2. Check the prevalence table totals! A common error made during data extraction was to set the totals in prevalence tables to 100 (to represent 100%), but these are actually meant to capture the total **number** of isolates/animals/samples (whatever the correct unit of analysis is) in each group.

.. hint:: Ensure that you have the :ref:`data extraction rules <data_extraction/data_extract_rules:Data Extraction Rules>` open alongside the paper you are validating when completing this process so that you don't miss anything--there is a lot to look out for!

Check These Common Reasons for Exclusion From Modelling
-------------------------------------------------------

.. important:: Remember to document any factors and papers you are excluding for the reasons outlined below or any other reason. 

Factor is not modifiable
~~~~~~~~~~~~~~~~~~~~~~~~

While the general practice was to exclude non-modifiable, or immutable factors such as age, location, or breed :ref:`(read more) <data_extraction/data_extract_rules:Data Extraction Rules>` at either secondary screening or data extraction, it is not always clear whether a factor is modifiable. As such, there may be some non-modifiable factors in your timber that you will need to exclude from your model.

Questions of whether a factor is modifiable or not are also context-dependent, and sometimes warrant consultation with an expert. Especially when it comes to factors related to management practices, a factor may be theoretically modifiable, but the implementation required may be cost prohibitive such that the factor is not practically modifiable.

Appropriate production stage or sub-stage is unclear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It may be difficult to determine the appropriate production stage or sub-stage at which to place a factor in the model.  For instance, a study may state that “pigs from farms across the United States were sampled” without specifying whether these are finisher pigs, nursing piglets, sows, or weaned nursery pigs.

.. Note:: This is especially relevant to cattle and swine, as they spend a significantly longer time at the farm stage—long enough for that farm stage to be split into multiple sub-stages.

Multiple production stages or sub-stages are combined
+++++++++++++++++++++++++++++++++++++++++++++++++++++

It is also possible for data to be aggregated across some combination of the farm, abattoir, and/or retail stages.

Common examples of this particular reason for exclusion are:

1.       One or both groups compared in the factor are representative of aggregated samples from multiple farm sub-stages (i.e. a conventional vs organic production type factor, where AMR data in each comparison group is representative of samples taken from both weaned nursery pigs and finishing pigs)
2.       Broiler and layer chickens are either aggregated together in both comparison groups, or one comparison group is made up of broilers and the other is made up of layers (for example, a production type factor comparing organic broilers with conventional layers would fit into this category. The focus of the comparison is the difference in production type, but the fact that there is an additional difference between the groups (broiler vs layer) acts as a confounder.)
3.       Chickens and turkey (sometimes referred to collectively as poultry in the AMR literature) treated similarly to broiler and layer chickens in point 2

Check These Other Possible Reasons for Exclusion From Modelling
---------------------------------------------------------------

These are a few examples of *possible* reasons for exclusion from modelling. 

.. caution:: These reasons for possible exclusion are highly context-dependent, so please ensure you discuss factors that may fit into these categories with Colleen Murphy.

Stage of AMR measurement differs from the stage of factor application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generally speaking, factors where the site of AMR measurement differs from the site of factor application (i.e. antimicrobial use on the farm, sampled at retail) are *excluded* from our models.

There are a few potential exceptions to this rule, however:

Production type factors measured at retail
++++++++++++++++++++++++++++++++++++++++++

If the effect of a production type factor (say organic vs conventional, which is of course something that applies or is taking place at the farm stage) on AMR is measured via samples of retail meat, the factor *can* be placed at the retail stage in the model. However, if you have other similar production type factors in your timber that are measured via sampling at the farm, you would likely exclude those sampled at retail.

Factors applied at farm and measured at abattoir
++++++++++++++++++++++++++++++++++++++++++++++++

If a factor is applied at the farm to a group of animals that are then followed to the abattoir for sampling, the factor *may* be eligible for inclusion in a model.

There are a few different possibilities for factors that fall into this category:

**Sampling was performed before any processing effects took place, and samples representative of individual animals (such as caecal swabs or droppings) have been taken:** 

The samples are likely representative of the farm stage, and so they *may* be eligible for placement in the model at the farm.

**Sampling was performed before any processing effects take place, and “external” samples have been taken (i.e. a hide or skin swab, or a floor swab of the transport truck):**

The samples are likely representative of the farm and transport stages, and *may* be eligible for placement in the model at the farm.

**Sampling has been performed after processing (most commonly via carcass swab):**

The samples are likely representative of the abattoir stage, and will likely have to be excluded from the model.

.. important:: The important caveat to keep in mind when considering factors applied at farm and measured at abattoir is that conditions occurring during transport are present as confounders. In other words, the measurement of AMR at abattoir is likely influenced by more than just the farm-level factor being reported.

Non-specific antimicrobial use factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some papers may contain general antimicrobial use factors, where the antimicrobial(s) administered are not specified. If there are factors related to the use of specific antimicrobial(s) (i.e. ceftiofur use) eligible for inclusion in your model, these less well-characterized factors (i.e. any antimicrobial use in the last 5 years) can likely be excluded.

Alternatively, these may be run separately from any specific AMU factors (see :ref:`here <model_building/selecting_factors:Determining Which Factors to Run Together>` for more information).

Factors that are not well-characterized
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are factors that are not fully characterized in the paper, where the comparison groups may be difficult to interpret. Here are a few examples:

*Controlling flies with toxin:*

- No info on what the “toxin” is
- The difference between the two groups is not clear: does one control flies with a toxin, while the other does not control flies at all? Or does the other group use an alternative method of control?

*Infrequent disinfection vs frequent disinfection:*

- How often is “infrequent”? How often is “frequent”?
- What is the disinfection agent?
- How are the authors defining disinfection?

The resistance outcome is a combination of antimicrobials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the exception of common combinations, i.e. imipenem and cilastatin, quinupristin and dalfopristin, or combinations of sulfonamides and trimethoprim (i.e. sulfamethoxazole and trimethoprim, sulfadiazine and trimethoprim), which should appear as established options in the data extraction AMR dropdown menu, all other rows of data must report resistance to an individual antimicrobial to be eligible for inclusion in the iAM models.

General resistance, or multidrug resistance, where the resistance outcome is not specified, should also be excluded from models.

.. Tip:: Filter your query on the AMR field, with only blank cells selected. This may identify factors that slipped through the extraction process, with an unspecific or unacceptable combination resistance outcome.

Discuss with an Industry Expert
-------------------------------

Relevancy to the Canadian context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As the objective of the iAM project is to produce models that are applicable to the context of the Canadian agri-food industry, this is an important step in the factor selection process. 

In conjunction with your discussions, you should obtain a copy of your food-commodity's **On-Farm Food Safety Program** and use this to assess the applicability of your factors to the Canadian context. You can find this document on your commodity's industry group's website.

Broadly, a factor may be:

1. Used in Canada
2. If approved for use in Canada, its application or use may impact AMR
   
Factors in the latter category will likely be included in the model, but run separately from the factors representative of the typical Canadian industry to explore “what-if” scenarios.  *These “what-if” scenarios may also include factors not yet approved in Canada, but which have the potential to become relevant through future policy change and are thus worth exploring.*

More specifically, your discussions with an industry expert should be aimed at grouping factors into different categories of applicability to the Canadian context. These categories have been defined for the iAM project as a whole and are outlined in detail :ref:`here <10_reference/style_guide:Terms for Factor Applicability to the Canadian Context>`.

.. Hint:: For food-animal species that spend a longer time at the farm stage before processing (namely cattle and swine), relevancy of a factor may vary between sub-stages of the farm stage. For example, some antimicrobials administered to nursing piglets or weaned nursery pigs may be withdrawn for part or all of the finishing stage due to residue concerns.

Selecting appropriate comparator groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In accordance with our definitions of the factor and comparator groups :ref:`here <10_reference/style_guide:Study Groups>`, the comparator group should be representative of the default situation in Canada. 

The factor and comparator groups were allocated as described in the literature during extraction, but may need to be flipped in the model if the paper's factor group is more representative of the default situation in Canada.

However, the comparator group is not *always* selected to represent the default Canadian situation. Sometimes, the effect of a given predictor in one group, albeit uncommon in Canada, is more topical and relevant to the objectives of the iAM.
In these cases, the comparator group will not reflect the default Canadian situation. 
There are two notable examples of this exception:

1. **Antimicrobial use factors:** where the group being administered antimicrobials should always be designated the factor group, and the group not being administered antimicrobials should always be designated the comparator group
2. **Disinfectant use factors:** where group in which the disinfectant is applied should always be designated the factor group, and the group in which the disinfectant is not applied should always be designated the comparator group

Frequency of occurrence
~~~~~~~~~~~~~~~~~~~~~~~

The frequency of occurrence of each factor in the Canadian context should be determined by consulting with an expert, and captured at the frequency node of your model.

Determining Which Factors to Run Together
-----------------------------------------

Computational limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

The Professional edition of Analytica unfortunately comes with the constraint that a maximum of **23 factor nodes at each production site** (where each production site is farm (and any sub-stages of farm such as nursing piglets, nursery, etc. in pig production), abattoir, or retail) can be *run* at one time.
For example, for pig production, you can run up to 23 factors at the nursery site + up to 23 factors at the finishing site (+ up to 23 factors at each other site in the model) at once.

.. hint:: This constraint does not mean that you cannot *insert* more than 23 factor nodes at a given production site in the model. It is only a restriction on the number of factors that you can select to be included in calculations for a single run of the model.

General guidelines
~~~~~~~~~~~~~~~~~~

After combining your factors and/or associations with resistance as per the :ref:`meta-analysis guidelines <model_building/meta_analysis_guidelines/Meta-analysis Guidelines>`, you will have to determine which factors are still similar enough that they should NOT be run simultaneously so as to avoid "double-counting" their potentially overlapping effects on AMR.
Here are some examples of factors that should not be run simultaneously:

**Subtherapeutic Tetracycline Use and Therapeutic Tetracycline Use:**

These are not similar enough to be combined with meta-analysis. However, they should not be run simultaneously as both deal with tetracycline use.

**Infrequent Disinfection and Frequent Disinfection:**

These are not similar enough to be combined with meta-analysis. However, both involve disinfection and will likely have an overlapping effect.

**Organic Production Type and Antibiotic-Free Production Type:**

All organic production is by default ABF (but not all ABF is organic), so these have overlapping effects. 

When deciding which factor in each of these pairs to run over the other, you *may* want to choose the factor/associations with the larger sample sizes (please note that this is only a suggestion!).

.. Tip:: Your standard error is a proxy for sample size, where a large SE is representative of a small sample size

Generally, the groupings you made as per the :ref:`Terms for Factor Applicability to the Canadian Context <10_reference/style_guide:Terms for Factor Applicability to the Canadian Context>` should act as a guide in terms of what to run simultaneously. Broadly, you'll want to run a set of factors representative of the default Canadian context separately from a set of factors representative of any type of what-if scenario (see :ref:`here <model_building/selecting_factors/Relevancy to the Canadian context>`).

If you have identified similar factors that should not be run simultaneously and are still running into the Analytica limitations, get in touch with Brennan Chapman or Charly Phillips to see if there's a work-a-round for your situation.

Other Model Components
----------------------

The following elements are handled by the :ref:`iAM.AMR.HUB <models/hub:iAM.AMR.HUB>` module:

1. Baseline prevalence and distribution
2. Bacterial recovery at retail
3. Consumption from the Foodbook

But, you should check to ensure that these apply to your model:
 
1. Check to see if your baselines are informed by actual data or placeholder values.
2. If they are informed by placeholder values: check to see if the placeholders are applicable to your scenario. If you have better estimates of the baseline than the default value(s), perhaps informed by your discussions with an expert, use those instead. 

.. note:: The baseline data is informed by count data from CIPARS surveillance reports. The count data is converted into prevalence behind the scenes in Analytica and modelled using a :ref:`beta distribution <10_reference/math_stats:Beta>`. If you have alternative baseline data that you would like to use in your model, however, you can certainly change this within your own model.

Other Recommendations or Conventions
------------------------------------

`Analyticar <https://github.com/iAM-AMR/analyticar>`_ (when we fix it!)

After Modelling
---------------

It is recommended that, once your model is built, you make a causal diagram out of all of your factors. This is a useful exercise to do as you're writing up the Results and Discussions sections of your paper.
