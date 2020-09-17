
=====================
Data Extraction Rules
=====================



Data Extraction Rules
---------------------

Immutable Factors
~~~~~~~~~~~~~~~~~

Immutable factors are defined as those that are not practically modifiable or reproducible. These include factors such as:

- unique comparison groups or locations

  - Barn A *vs.* Barn B
  - Sweden *vs.* Switzerland

- breed or type of animal

  - Ross chicks *vs.* Cobb chicks
  - Swedish Friesian vs. Swiss Holsteins

- life stage or production stage  

  - egg *vs.* chick *vs.* broiler
  - grow-finish *vs.* farrow-to-finish
  - farm *vs.* abattoir *vs.* retail
  
- unique years/periods of time

  - 1998 *vs.* 1999

Immutable factors should not be extracted.

.. admonition:: Important

   If a reason for the comparison is given, such as a growth promoter ban/change in related industry policy, factors comparing unique years/periods of time may be valid for extraction. For instance, one period of time might represent pre-ban conditions, while the next might represent post-ban conditions. In this case, the factor title should be "<Antimicrobial(s)> Ban", and any antimicrobials available for use pre-ban, as well as any available both pre- and post-ban that were specifically mentioned, should be tagged as if the factor is an AMU factor. Any information about the prevalence of actual growth promoter use pre-ban (and sometimes post-ban) should be provided in the factor description and/or reference notes.

Binary and Continuous Factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a factor is binary (i.e. two discrete outcomes, such as "Yes" and "No"), it shall be extracted. 

When a factor is continuous (e.g. a one unit increase in the predictor results in an X unit increase in the outcome) it shall not be extracted.  

Selecting a Referent Level
++++++++++++++++++++++++++

Binary factors consist of a referent and exposure group (e.g. your control and exposure groups respectively). The referent should generally be defined as the default practice in industry, or the least interventionist, while the exposure is the less common, or more interventionist approach. See above for more details. 

Multiple Discrete Levels (Catagories)
+++++++++++++++++++++++++++++++++++++

When a factor has multiple levels (e.g. low, medium, and high), the factor shall be extracted seperately for each level, using the same referent level.  

For example, for a factor with levels low, medium, and high, the factor is extracted as low *vs.* medium, and low *vs.* high. The factor medium *vs.* high shall not eb extracted. The choice of referent level is described above.

Non-informative Levels
^^^^^^^^^^^^^^^^^^^^^^

An exception is non-informative levels, which shall not be extracted.

For example, for a factor with levels 'red', 'blue', and 'other', the factor is only extracted as red *vs.* blue, because the 'other' is not part of a defined set, and cannot be inferred from the comparison. But, where levels are drawn from a defined set, they shall be extracted (these are few and far-between). For example, for a factor with levels 'summer', 'winter', 'other', the factor is extracted as 'summer' *vs.* 'winter' and 'summer' *vs.* 'other', as the 'other' can be inferred.


Factor Data
~~~~~~~~~~~

When multiple data formats are available, we always prefer **contingency tables** (count data), followed by rate tables, and finally odds ratios or relative risk. You only need to extract one format of data for a given factor.


Resistances and MDR
~~~~~~~~~~~~~~~~~~~

All factors related to antimicrobial resistance should be extracted, including those related to non-traditional antimicrobials (e.g. ionophores, coccidiostats, and metals). They should be extracted as finely as possible where specified (e.g. ceftiofur-resistance, rather than third-generation cephalosporin resistance).

Multi-drug resistance (MDR) should not be extracted, because the specific combination of resistances is impossible to compare to across studies/situations. However, if you are presented with MDR data, it may be possible to tease out antimicrobial-specific data. Before you do - ensure that the individual antimicrobial data For example, imagine that 'X' and 'Y' number of isolates were tested for each 'Poor' and 'Good' producers, as in the study below:

.. figure:: /assets/figures/mdr_example.png
   :align: center

   An example of an MDR table using rates from Spears (1990).

We can tease out this information by adding up the occurence of resistance across all profiles, to calculate the number of resistant organisms.

+---------------+------------------------------------------------------+------------------------------------------------------+
| Antimicrobial | AMR+ in Poor Producers                               | AMR+ in Good Producers                               |
+---------------+------------------------------------------------------+------------------------------------------------------+
| GM            | (0.19)(X) +   (0.579)(X) + (0.744)(X)                | (0.218)(Y) +   (0.902)(Y) + (0.451)(Y)               |
+---------------+------------------------------------------------------+------------------------------------------------------+
| SU            | (0.19)(X) +   (0.579)(X) + (0.1074)(X) + (0.0992)(X) | (0.218)(Y) +   (0.902)(Y) + (0.827)(Y) + (0.0977)(Y) |
+---------------+------------------------------------------------------+------------------------------------------------------+
| AM            | (0.0165)(X)                                          | (0.0376)(Y)                                          |
+---------------+------------------------------------------------------+------------------------------------------------------+


Multiple Measurements
~~~~~~~~~~~~~~~~~~~~~

Often, factors may be assessed at multiple time-points. For example, swine may be sampled for resistant organisms at birth, weaning, growing-finishing, and again at abattoir.  

As a general rule, where the *allocation* and *observation stages* are the same, the **Measurement Closest to Human Exposure** or **MCHE** should be extracted.  

Where the *allocation* and *observation stages* differ, the **MCHE** within the *allocation* stage should be extracted (if available). These rules, and their exceptions, are described below.  

Multiple Measurements at a Single Stage
+++++++++++++++++++++++++++++++++++++++

Where multiple measurements are available at a single production stage (i.e. the *allocation* and *observation stages* are the same), the measurement closest to human exposure should be extracted, except

... where there are missing or unavailable data at the time-point closest to human exposure

.. admonition:: Example

   Resistance was assayed at days 10, 20, and 30 of production for the exposed group, but only at days 10 and 20 for the referent group.  
   
   Day 20 is extracted.

- where the time-point is not applicable to the Canadian context

  e.g. a measurement at >36 days into broiler production, past the point of harvest in Canadian industry.

Multiple Measurements at Farm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Where multiple measurements are available at the **on-farm stage** for **cattle** and **swine**, a measurement should be extracted at the end of each production sub-stage. This includes the following:

- Cattle

  - Stage 1
  - Stage 2

- Swine
  
  - Stage 1
  - Stage 2

See the production basics section for more information.

Multiple Measurements at Multiple Stages





Provisional Rules
~~~~~~~~~~~~~~~~~


3.	Genomic data – record if AMR prevalence given + note what gene in description (can leave AMR dropdown empty – tetA and tetB are available in AMR dropdown though!), otherwise make a note (eg, CFU/g, gene copies, etc.). 

5.	Salmonella species – combine if AMR prevalence given for more than one Salmonella species
