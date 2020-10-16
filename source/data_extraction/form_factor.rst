

=============================
The Add or Edit a Factor Form
=============================

Summary
-------
The *Add or Edit a Factor Form* handles factor-level data extraction.


.. raw:: html

  <iframe src="https://giphy.com/embed/PjwvIXLnnMF0ytRpcp" width="480" height="300" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/PjwvIXLnnMF0ytRpcp">via GIPHY</a></p>



|br|

Title
-----
Create a title to describe the factor in title case. 

The title should be simple, direct, and give no experimental context -- the title should be generic, as to easily identify comparable factors between studies. There are two specific cases recognized: 

- where the factor solely describes antimicrobial use, the title should be recorded in the format "<Antimicrobial> Use", where <Antimicrobial> is the antimicrobial used

- where the factor describes production type (i.e. a comparison between conventional, and organic, ABF, or free-range production), the title should be recorded as "Production Type"


|br|

Description
-----------
Create a description to provide context in sentence case.

The description should include relevant experimental conditions, not captured elsewhere in data extraction. This includes details such as the identity and quantity of antimicrobials administered, duration of exposure, prior antimicrobial use, etc.. 

For example, the factor titled "Chlortetracyline Use" may have a description: "Chlortetracyline, administered in feed (days 17 - 78, 164 - 206), as Aureomycin 100-g at 11 ppm. Isolates cultured on agar amended with 4 μg/ml TET-HCL."

Note that this is a particularly data-rich example -- many factors will not be recorded with that level of detail because it is not reported in the literature.


|br|

Host and microbe
----------------
Select a host and microbe from the dropdown menus. Once you select a host, you will be able to select a host sub-type. Likewise, once you select a microbe, you will be able to select a microbe sub-type. 

.. attention:: The sub-type will only be shown correctly if the type used in the last record selected is a parent of the sub-type. For example -- for a reference with two factors -- if the first factor was for cattle, and the second factor for chicken: while the cattle factor is in focus (selected), the cattle sub-type will be shown, but the chicken sub-type will disappear (and vice-versa). This also applies to the microbe and microbe sub-type dropdown, and similarly applies to the AMU field.

Do not be alarmed if the sub-types seem to disappear when extracting from a paper with multiple host or microbe types -- the data are still there, but not visable. You can check the data are still there by selecting the record (by interacting with one of the fields, or clicking in the white-space around the fields).


|br|

Location
--------
Location (Loc.) refers to the location of the factors' data in the text. This is generally a table or figure. However, if the data are in the body of the text, use page (pg.) and paragraph (para.) numbers to indicate the location. Always use the physical page number if available.  If only the electronic page number is available (the page in the PDF), use the electronic page number (epg.).


|br|

Result
------
Result refers to the format of the factors' data. Data are presented in one of several formats: 

- as contingency tables (counts of AMR+, AMR-, and totals)
- as prevalence tables (percentages of AMR+, AMR -, and totals)
- as relative risks
- as odds ratios

When multiple data formats are available, we always prefer **contingency tables** (count data), followed by prevalence tables, and finally odds ratios or relative risk. You only need to extract one format of data for a given factor.


|br|

Stage
-----
Select both an allocation and observtion production stage:

- The *allocation stage* refers to the production stage at which the exposed and referent groups are effectively established, and where the factor effectuates change.

- The *observation stage* refers to the production stage at which the effects of the factor are observed, and where sampling was performed.

.. tip:: A study which involves the retail sampling of organically- and conventionally-raised chicken products to determine the effect of production type would have an allocation stage of *Farm*, and a observation stage of *Retail*, as the factor effectuates changes on-farm, but these are measured at retail.


|br|

AMR
---
Select the ingredient to which resistance was assayed. As you begin to type, the field will be auto-completed from the list of available ingredients. If you cannot locate the appropriate ingredient, try :ref:`exploring the available ingredients <03_activities/literature_extract:Selecting an Antimicrobial>`.


|br|

Exposed and referent groups
---------------------------
Describe both the exposed and referent groups, in title case.

The exposed and referent groups are allocated as described in the literature (i.e. if the authors use 'wood curl bedding' as the exposure, and 'flax bedding' as the referent, it should be recorded as such). 

If no allocation is provided, the interventionist practice should be used as the exposure, and the default practice should be used as the referent (i.e. 'doing something' is the exposure, 'doing nothing' is the referent). 

The exception to these rules is *Antimicrobial Use*. Where the factor describes antimicrobial use -- regardless of how the authors allocate the exposed and referent groups -- the exposure should always be antimicrobial use, and the referent should always be no use. Additionally, the factor should be recorded in the format "<Antimicrobial> Use" (where <Antimicrobial> is the antimicrobial used), and "No Use".

For example, if a study compares the prevalences of resistance in broilers administered ceftiofur, the exposure should be recorded as "Ceftiofur Use" and the referent as "No Use".


|br|

Result or analysis unit
-----------------------
Select the unit of analysis (i.e. the unit allocated to the exposed and referent groups). Generally, this will be at the isolate or sample level, but some analyses are conducted at the flock, herd or farm levels.


|br|

AMU
---
Select the ingredients used as part of the factor. As you begin to type, the field will be auto-completed from the list of available ingredients. Then, select 'Add AMU' to add the ingredient to the list. Likewise, highlight the ingredient and select 'Delete AMU' to remove it from the list.

Refer to the :ref:`selecting an antimicrobial <03_activities/literature_extract:Selecting an Antimicrobial>` section for details on how to extract data for factors including multiple ingredients.


Selecting an Antimicrobial
~~~~~~~~~~~~~~~~~~~~~~~~~~
We use the WHO's ATCvet index as our controlled vocabulary for recording antimicrobial resistance (AMR) and antimicrobial use (AMU).

The process of selecting an antimicrobial to describe AMR (i.e. the resistance assayed) is straightforward, owing to the fact only one antimicrobial is assayed at a given time, and there are a limited number of antimicrobials included in most antimicrobial susceptibility tests (ASTs).

The process of selecting antimicrobial(s) to describe AMU is more complex, as multiple antimicrobials may be used at a given time, and in a greater number of combinations.

Regardless of whether you are selecting an antimicrobial for AMR or AMU, the goal is the same -- to find the most appropriate and specific ATCvet code that describes the antimicrobial(s).

.. note:: You do not need to have direct knowledge of, or work with the ATCvet codes directly. When we say *'select an ATCvet code'*, what we really mean is *'select the most appropriate ingredient(s), represented in the ATCvet index'*.

Below, we use the terms *ingredient*, *antiinfective* and *antimicrobial*, and these are largely interchangable for our purposes. An *ingredient* is a generic term for an item described in the index. An *antiinfective* is an umbrella term for an ingredient with anti-infective properties (e.g. an antimicrobial, antiparasitic, or a compound like copper sulphate that has antimicrobial properties). And an *antimicrobial* is an ingredient with antimicrobial properties, generally recognized as a 'drug'. 

An AST generally includes at least one traditional *antiinfective*, and may include one or more additional *active ingredients* (e.g. chlortetracycline and copper supplementation) or an adjuvant (e.g. penicillin with a beta-lactamase inhibitor).

.. hint:: When the study uses a drug that specifies a different form than what appears in ATCvet, (e.g. -tartarate, -sulfate, -free acid, -chloride, copper, ccfa, etc) do not attach a note to the reference. Instead, in the factor description field, write "drug administered as X". e.g. *tylosin* (official name in ATCvet) may be administered as *tylosin tartrate.*


ATCVet Code Reference
~~~~~~~~~~~~~~~~~~~~~
You can explore the ATCVet codes using the **Search ATCvet by AM** form. 

This form allows you to enter a single ingredient, and view all codes where that ingredient is included. Additionally, it will show you the class (level 4 grouping) to which the ingredient belongs, other ingredients in that class, and any combinations in which it may be involved outside of the class (level 3 grouping).

.. tip:: You can view the entire ATCvet index by opening the table *s_atc_vet* in the *Navigation Pane*.

Selecting an ATCvet Code with one ingredient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Select the appropriate ingredient. 


Two ingredients
~~~~~~~~~~~~~~~

An antiinfective and adjuvant
+++++++++++++++++++++++++++++
Select the appropriate combination of ingredients. Generally, the adjuvant is not explicitly listed, but is specified by class. 

e.g. *amoxicillin and clavulanic acid* would be recorded as *amoxicillin and beta-lactamase inhibitor*.

An antiinfective and active ingredient
++++++++++++++++++++++++++++++++++++++
If the ingredients include an antiinfective and another active ingredient...

... and the antiinfective and active ingredient are **explicitly specified** as a combination:
  - select the appropriate combination

    - e.g. *cefepime and amikacin*

... and the antiinfective and active ingredient are **not explicitly specified** as a combination, but **belong to the same class**, or level 4 grouping ...
 ... and a non-specific **class combination exists** ...
  - select the appropriate non-specific combination

    - e.g. oxytetracycline and tigecycline used together would be recorded as *chlortetracycline, combinations*

 ... and a non-specific **class combination does not exist** ...
  - select the appropriate non-specific combination from the *Combinations of Antibacterials* level 3 grouping as described below
  
    - note that this is an uncommon outcome, as most classes include non-specific combinations

... and the antiinfective and active ingredient are **not explicitly specified** as a combination, and **do not belong to the same class**, or level 4 grouping ...
 ... and **one** of the ingredients is included in the *Combinations of Antibacterials* level 3 grouping ...
  - select the appropriate combination
  - additionally, select the individual ingredients

    - e.g. chlortetracycline and sulfamethazine used together would be recorded as *tetracyclines, combinations with other antibacterials*, *chlortetracycline*, and *sulfadimidine*

 ... and **more than one** of the ingredients is included in the *Combinations of Antibacterials* level 3 grouping ...
  - select the appropriate combination using the order of preference below
  - additionally, select the individual ingredients

    1. quinolones 
    2. cephalosporins 
    3. macrolides 
    4. polymyxines 
    5. penicillins 
    6. aminoglycosides 
    7. tetracyclines 
    8. amphenicols 
    9. lincosamides 
    10. sulfonamides

    - e.g. ciprofloxacin and amoxicillin used together would be recorded as *quinolones, combinations with other antibacterials* (not *penicillins, combinations with other antibacterials*), *ciprofloxacin*, and *amoxicillin*
    - e.g. amoxicillin and chlortetracycline used together would be recorded as *penicillins, combinations with other antibacterials* (not *tetracyclines, combinations with other antibacterials*), *amoxicillin*, and *chlortetracycline*


Idiosyncracies of the ATCvet index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Common alternative ingredient names
+++++++++++++++++++++++++++++++++++
The following ingredients have commonly used alternative names -- only the official name is given by ATCvet:

==============  =======================
Common Name     ATCvet Name
==============  =======================
Cephalothin     cefalotin
Cephradine      cefradine
Flavomycin      bambermycin
Penicillin G    benzylpenicillin
Penicillin V/K  phenoxymethylpenicillin
Sulfamethazine  sulfadimidine
Sulfisoxazole   sulfafurazole
==============  ======================= 

Order of ingredients
++++++++++++++++++++

Combinations with sulfonamides are almost always specified with the sulfonamide first
  
  - e.g. *sulfadimidine and trimethoprim*

