

Data Extraction
===============

Overview
--------
This section provides instructions for data extraction into CEDAR. If you are not familiar with CEDAR, please see the :ref:`entry on CEDAR <02_project/CEDAR:The CEDAR Database>`.

There are two types of data you will be extracting: reference-level data, which provides context for the outcome, and factor-level data, which describes the outcome itself. These data are entered in a reference-level form, and a factor-level form respectively.

On the *Add or Edit a Reference* form, you will extract reference-level information such as:

- study location
- study design
- reporting methods

On the *Add or Edit a Factor* form, you will extract factor-level information such as:

- the exposed and referent groups
- the host, microbe, and resistance tested
- counts, rates, or odds ratios describing the effect of the factor

Geographic versions of CEDAR_forest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To simplify data extraction, two versions of the CEDAR back-end *CEDAR_forest* were created: *CEDAR_forest_east* for access from the GoC network, and *CEDAR_forest_west* for access from outside the GoC network.




Add or Edit a Reference
-----------------------


Add or Edit a Factor
--------------------



Selecting an Antimicrobial
--------------------------
We use the WHO's ATCvet index as our controlled vocabulary for recording antimicrobial resistance (AMR) and antimicrobial use (AMU).

The process of selecting an antimicrobial to describe AMR (i.e. the resistance assayed) is straightforward, owing to the fact only one antimicrobial is assayed at a given time, and there are a limited number of antimicrobials included in most antimicrobial susceptibility tests (ASTs).

The process of selecting antimicrobial(s) to describe AMU is more complex, as multiple antimicrobials may be used at a given time, and in a greater number of combinations.

Regardless of whether you are selecting an antimicrobial for AMR or AMU, the goal is the same -- to find the most appropriate and specific ATCvet code that describes the antimicrobial(s).

.. note:: You do not need to have direct knowledge of, or work with the ATCvet codes directly. When we say *'select an ATCvet code'*, what we really mean is *'select the most appropriate ingredient(s), represented in the ATCvet index'*.

Below, we use the terms *ingredient*, *antiinfective* and *antimicrobial*, and these are largely interchangable for our purposes. An *ingredient* is a generic term for an item described in the index. An *antiinfective* is an umbrella term for an ingredient with anti-infective properties (e.g. an antimicrobial, antiparasitic, or a compound like copper sulphate that has antimicrobial properties). And an *antimicrobial* is an ingredient with antimicrobial properties, generally recognized as a 'drug'. 

An AST generally includes at least one traditional *antiinfective*, and may include one or more additional *active ingredients* (e.g. chlortetracycline and copper supplementation) or an adjuvant (e.g. penicillin with a beta-lactamase inhibitor).

ATCVet Code Reference
~~~~~~~~~~~~~~~~~~~~~
You can explore the ATCVet codes using the **Search ATCvet by AM** form. 

This form allows you to enter a single ingredient, and view all codes where that ingredient is included. Additionally, it will show you the class (level 4 grouping) to which the ingredient belongs, other ingredients in that class, and any combinations in which it may be involved outside of the class (level 3 grouping).

.. tip:: You can view the entire ATCvet index by opening the table *s_atc_vet* in the *Navigation Pane*.

Selecting an ATCvet Code with one ingredient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Select the appropriate ingredient. 


Two ingredients
~~~~~~~~~~~~~~~~~~~~~~

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

- combinations with sulfonamides are almost always specified with the sulfonamide first
  
  - e.g. *sulfadimidine and trimethoprim*

