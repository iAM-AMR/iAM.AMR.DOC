

Data Extraction
===============

Getting Started
---------------
This section provides instructions for data extraction into CEDAR. If you are not familiar with CEDAR, please review the :ref:`section on CEDAR <02_project/CEDAR:The CEDAR Database>`.

There are two types of data you will be extracting: reference-level data, which provides context for the outcome, and factor-level data, which describes the outcome itself. These data are entered in a reference-level form, and a factor-level form respectively.

On the *Add or Edit a Reference* form, you will extract reference-level information such as:

- study location
- study design
- reporting methods

On the *Add or Edit a Factor* form, you will extract factor-level information such as:

- the exposed and referent groups
- the host, microbe, and resistance tested
- counts, rates, or odds ratios describing the effect of the factor




Common Concerns
---------------

What do I do if ...

... there are no factors to extract
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If there are no factors to extract, indicate this using the notes field, and skip the reference.

... the data are only available in a figure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If factor data are only available in a figure (i.e. no numbers are given on a graph, or in text), and the numerical value cannot be determined with certainty (i.e. is not zero or 100%), indicate this using the notes field, and skip extracting the factor.

... the data are presented only as a relative risk?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We cannot use relative risk at this time. Do not extract the factor's data, but indicate the omission in the notes field.

... I'm confused about how to extract a factor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you're confused about a factor, reach out on Slack for clarification. Additionally, add a note to indicate why the factor was extracted in that way.

... an item I need is missing from a dropdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If an item is missing from a dropdown (i.e. a non-free-text field), reach out on Slack. If the decision is made to use an alternative item in the list, add a note to justify this replacement. 

... the results are in log(Odds) or an estimate/coefficient of a logistic regression?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Recall that the Odds Ratio = e^x, where x is the coefficient.

... there are multiple measurements of the same factor?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
See below.

... the study uses SIR (Susceptible, Intermediate, and Resistant)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a study includes an 'Intermediate' category, add the intermediate isolates/rate to the resistant category (i.e. we round up intermediate to resistant).

... I want to compare conventional, ABF, organic, 'welfare' or 'humane' production systems?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that these alternative systems are not the same. While all organic is ABF (antibiotic-free), not all ABF is organic. 'Welfare' and 'humane' production systems are likewise different. 

