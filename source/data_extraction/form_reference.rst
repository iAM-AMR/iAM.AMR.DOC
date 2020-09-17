

================================
The Add or Edit a Reference Form
================================

Summary
-------
The *Add or Edit a Reference Form* handles reference-level data extraction.


|br|

Main Tab
---------
The *Main Tab* includes bibliograpic information, study identifiers, and reference exclusion status.


Bibliographic Information
~~~~~~~~~~~~~~~~~~~~~~~~~
The title, author, and publication year should already be extracted. Do not edit these fields; updated bibliographic data is managed in Mendeley.

Extract the publisher (journal).


Study Identifiers
~~~~~~~~~~~~~~~~~
Extract the DOI (preferred), or PMID (if available).

The Bibtex key is a unique string representing the reference. The Bibtex key may be blank; do not add one here.


Exclusion Status
~~~~~~~~~~~~~~~~
If the reference should be excluded, set *is excluded* to **TRUE**. Additionally, provide an exclusion reason.


|br|

Study Design Tab
----------------
The *Study Design Tab* includes study design information, and study reporting characteristics.

Study Design
~~~~~~~~~~~~
Select a study design from the dropdown menu. Then, extract additional detail from the text. The detail should include information such as:

- unit selection process
- experimental group allocation
- experimental conditions

Then, extract the sampling method from the text. This can be as simple as the sample type (e.g. "fecal samples collected from fresh pats on the barn floor"), or may include additional information (e.g. "Two clinical swabs per steer were inserted approximately 5 cm into the rectum and rotated until covered with a uniform amount of feces.") if available.

AST
~~~

AST Method
++++++++++
Select the antimicrobial susceptibility testing method used in the study. 

Explicit (Enumerated) Breakpoints
+++++++++++++++++++++++++++++++++
A reference contains explicit, enumerated breakpoints when the level(s) at which isolates were considered resistant are reported in the text. Explicit breakpoints are reported differently for different antimicrobial susceptibility testing (AST) methods:

- for dilution-based assays, concentrations will be reported in µg/mL
- for diffusion-based assays, zone diameters will be reported in mm

For example, `Awosile et al. (2018) <https://doi.org/10.3168/jds.2017-13277>`_ include explicit breakpoints:

  The following antimicrobial agents were tested with the resistance breakpoints presented in parentheses: ampicillin (≥32 µg/mL), amoxicillin-clavulanic acid (≥32/16 µg/mL), chloramphenicol (≥32 µg/mL), ceftriaxone (≥4 µg/mL), ceftiofur (≥8 µg/mL), ciprofloxacin (≥1 µg/mL) cefoxitin (≥32 µg/mL), gentamicin (≥16 µg/ mL), kanamycin (≥64 µg/mL), nalidixic acid (≥32 µg/ mL), streptomycin (≥64 µg/mL), sulfisoxazole (≥512 µg/mL), trimethoprim-sulfamethoxazole (≥4/76 µg/ mL), and tetracycline (≥16 µg/mL).

But, references that only include reporting to the effect of "the results were interpreted according to CLSI | EUCAST | NARMS | CIPARS guidelines" do not include explicit breakpoints. For example, from `Diarra et al. (2007) <https://doi.org/10.1128/AEM.01086-07>`_: 

  The MIC results were interpreted according to the breakpoints of the CLSI and the 2005 Canadian Integrated Program for Antimicrobial Resistance Surveillance (CIPARS) guidelines.

Or from `Cameron-Veas et al. (2018) <https://doi.org/10.1016/j.tvjl.2018.02.002>`_:

  An isolate was identified as susceptible or resistant, based on the epidemiological cut-off value (ECOFF) defined by the European Committee of Antimicrobial Susceptibility Testing (EUCAST, 2016).


.. tip:: Studies that use diffusion-based assays often report the concentration of the disks -- this is not an explicit breakpoint. Instead an explicit breakpoints would be given as diameters (in mm).


MIC Table
+++++++++
An MIC table contains counts (or frequencies) of isolates that are inhibited at each dilution range. If a factor has an MIC table, it almost always gives explicit breakpoints; these breakpoints are often indicated in the table using a dark line. An example of an MIC table is provided below:

.. figure:: /assets/figures/example_MIC_table.png
   :align: center

   An example of an MIC table from Avrain et al. (2003).


|br|

Location Tab
------------
Select the country in which the study was conducted. If the location of study is not explicitly reported, it can be inferred from the PI's institution. Note, some countries are listed with their full (infrequently used) names; check all variations if you cannot locate a country.

If a more precise location is provided (e.g. state, province, canton), add an entry for each applicable sub-region. If the precise location provided does not map to the specified sub-regions, select *Other*, and provide more detail. If no precise location is provided, select *Other* from the sub-region list, and leave the detail blank.

For example, if a study was conducted in Ohio and Michigan of the United States of America, select "United States of America" as the location, and include two sub-regions, "Ohio" and "Michigan". If the study was described as being conducted "in the mid-western USA", select "United States of America" as the location, and include an entry with sub-region "other", and detail "mid-west".

.. hint:: If the location is not stated in the text, you can infer it from the PI's home institution.


|br|

History Tab
-----------
The data extraction process can be broken down into steps; the *History tab* tracks the progress of the references as they move along each of these steps toward completion.

Each time a user completes an *activity*, they must update the reference history by adding an entry in the tab. This includes when a user completes an activity previously assigned to another user; the user should always add an entry for all completed activities.

.. hint::
   
   Think of the history tab as tracking milestones; any time the reference reaches a new stage of completion or verification, the history should be updated. This is used to infer the completeness and reliability of the data for downstream activities.


Activities
++++++++++

Activities are generic terms for steps in the data extraction process; always select the appropriate, specific step when updating the reference history.

In brief, the life cycle of a reference consists of these activities:

- the reference is imported
- the reference is assigned
- the reference is extracted (or extracted in duplicate)
- the reference is reviewed
- the reference is (optionally) signed-off on by a senior user


Steps
+++++

+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status                          | Definition                                                                                                                                                                                      |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| imported                        | The reference has been imported into the database from |br| the   literature search.                                                                                                            |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| import_single                   | The reference had been extracted in a previous version (V1) |br| of   CEDAR, and was imported here (replicate 1 of 2).                                                                          |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| import_dual                     | The reference had been extracted in a previous version (V1) |br| of   CEDAR, and was imported here (replicate 2 of 2).                                                                          |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| import_reviewed                 | The reference had been extracted in a previous version (V1) |br| of   CEDAR, and was imported here (already reviewed).                                                                          |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| assigned                        | The reference has been assigned to a user for data extraction.                                                                                                                                  |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| extracted_excluded |br| _single | The reference has been extracted (replicate 1 of 2). |br| Or, the   reference has been excluded.                                                                                                |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reviewed_single                 | The reference has been extracted (singular extraction), |br| and a second   user has reviewed and corrected any errors or omissions |br| (or concurs the   reference should be excluded).       |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| signed_off_single               | The reference has been extracted (singular extraction), |br| and a senior   user has reviewed and corrected any errors or omissions |br| (or concurs the   reference should be excluded).       |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| recheck_single                  | The reference has been extracted, but upon review |br| the original   extractor (select their name here, not yours) |br| must re-check the   reference. |br| Check the notes field for details. |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| extracted_dual                  | The reference has been extracted in duplicate (replicate 2 of 2).                                                                                                                               |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reviewed_dual                   | The reference has been extracted in duplicate, |br| all conflicts were   resolved.                                                                                                              |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| signed_off_dual                 | The reference has been extracted in duplicate, |br| all conflicts were   resolved by a senior user.                                                                                             |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Life Cycle of a Reference
+++++++++++++++++++++++++

.. figure:: /assets/figures/reference_history.png
   :align: center

   The life cycle of a reference.


|br|

Notes and Issues Tab
--------------------
The *Notes and Issues tab* allows users to add notes to the reference, describing issues like:

- problems with data extraction
- additional context
- omitted factors
- level data

Attach a seperate note for each concern.


