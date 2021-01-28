
=============================
Data Extraction Tips & Tricks
=============================

Factor-Level Extraction
-----------------------

Defining the factor itself
~~~~~~~~~~~~~~~~~~~~~~~~~~

What do I do if...

... it is not clear which factors are considered relevant points of comparison, and which are not
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Factors listed here are considered "unmodifiable" or "immutable", and thus not relevant for our purposes:

- :ref:`Immutable Factors <data_extraction/data_extract_rules:Immutable Factors>`

For examples of extractable factors, please see:

- :ref:`Common Factor Types <data_extraction/form_factor:Common factor types>`
- :ref:`Binary and Continuous Factors <data_extraction/data_extract_rules:Binary and Continuous Factors>`

... I'm confused about how to extract a factor
++++++++++++++++++++++++++++++++++++++++++++++
If you're confused about a factor, reach out on Slack for clarification. Additionally, add a :ref:`note <data_extraction/form_reference:Notes and Issues Tab>` to indicate why the factor was extracted in that way.

... I want to compare conventional, ABF, organic, 'welfare' or 'humane' production systems
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`Common Factor Types <data_extraction/form_factor:Production type>`

Selecting exposed and referent groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: Groups are otherwise referred to as levels.

What do I do if...

... I am not sure which is which?
+++++++++++++++++++++++++++++++++

:ref:`Selecting a Referent Level <data_extraction/data_extract_rules:Selecting a Referent Level>`

... a group is not clearly defined (i.e. an "Other" group)?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`Non-informative Levels <data_extraction/data_extract_rules:Non-informative Levels>`

... there are more than two designated groups in the study?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`Multiple Discrete Levels (Categories) <data_extraction/data_extract_rules:Multiple Discrete Levels (Categories)>`

:ref:`Non-informative Levels <data_extraction/data_extract_rules:Non-informative Levels>`

Selecting the sample type
~~~~~~~~~~~~~~~~~~~~~~~~~

Which sample type should be extracted if multiple (i.e. fecal, water, dirt...) sample types are available?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`Sample Type <data_extraction/data_extract_rules:Sample Type>`

Choosing the microbe subtype
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What do I do if...

... a microbe subtype is not listed in the dropdown in CEDAR
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

For Salmonella species:

- :ref:`Salmonella Species <data_extraction/data_extract_rules:Provisional Rules>`

Factor data
~~~~~~~~~~~

What do I do if...

... the data are only available in a figure
+++++++++++++++++++++++++++++++++++++++++++
If factor data are only available in a figure (i.e. no numbers are given on a graph, or in text), and the numerical value cannot be determined with certainty (i.e. is not zero or 100%), indicate this using the :ref:`notes <data_extraction/form_reference:Notes and Issues Tab>` field, and skip extracting the factor.

... multiple data formats (i.e. a contingency table and a prevalence table) are available for a factor
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`Multiple Data Formats <data_extraction/data_extract_rules:Factor Data>`

... measurements are provided for multiple time points
++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`Multiple Production Stages <data_extraction/data_extract_rules:Multiple Measurements>`

:ref:`Multiple Timepoints Within a Single Production Stage <data_extraction/data_extract_rules:Multiple Measurements at a Single Stage>`

:ref:`Multiple Timepoints Within the Farm Stage <data_extraction/data_extract_rules:Multiple Measurements at Farm>`

... the study uses SIR (Susceptible, Intermediate, and Resistant)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If a study includes an 'Intermediate' category, add the intermediate isolates/prevalence to the resistant category (i.e. we round up intermediate to resistant).

... odds ratios from both multi-variable and univariable analyses are available
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`Odds Ratio Extraction <data_extraction/data_extract_rules:Factor Data>`

... there are zero observations of resistance in both the exposed and referent groups
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`Zero Observations of Resistance <data_extraction/data_extract_rules:Factor Data>`

... the results are in log(Odds) or an estimate/coefficient of a logistic regression
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Recall that the Odds Ratio = e^x, where x is the coefficient.

... the data are presented only as a relative risk
++++++++++++++++++++++++++++++++++++++++++++++++++

We cannot use relative risk at this time. Do not extract the factor's data, but indicate the omission by attaching a note to the associated reference through the :ref:`Notes and Issues tab <data_extraction/form_reference:Notes and Issues Tab>`.

... the study reports multi-drug resistance (MDR)
+++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`MDR Rules <data_extraction/data_extract_rules:Resistances and MDR>`

... the study reports genomic data on AMR
+++++++++++++++++++++++++++++++++++++++++

:ref:`Genomic data <data_extraction/data_extract_rules:Provisional Rules>`

General
-------

What do I do if...

... there are no factors to extract
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If there are no factors to extract, indicate this using the :ref:`Exclude Extraction Reason <data_extraction/form_reference:Exclusion Status>` field, and skip the reference.

... an item I need is missing from a dropdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If an item is missing from a dropdown (i.e. a non-free-text field), reach out on Slack. If the decision is made to use an alternative item in the list, add a note to justify this replacement. 