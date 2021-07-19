

Meta-analysis Guidelines
========================

Combining Factors with Meta-analysis
-------------------------------------

Meta-analysis is a statistical approach for combining data from multiple studies, often used to increase statistical power, or resolve uncertainty in effect size or direction. The simplest way to think of a meta-analysis is as a weighted average of the included observations, where the weighting accounts for the statistical properties of the studies.

Meta-analysis is used in the iAM.AMR project to derive a single effect estimator where multiple studies, or multiple observations within a study, are available to describe a given factor.

When should meta-analysis be performed?
---------------------------------------

Meta-analysis must only be performed where the effect measure, and the study populations, are identical or highly similar. Therefore, meta-analysis should **never** be performed:

* across food-animal species (species)
* across sub-populations of food-animals (such as between piglets and finishing pigs)
* across bacterial species (microbes)
 
  * including between Campylobacter jejuni and conventional
 
* across classes of antimicrobials (and sometimes even within an antimicrobial class)
 
  * see :ref:`Rules for Combining Resistance Outcomes <model_building/meta_analysis_guidelines:Meta-Analysis Rules>` for more specific guidance
 
* across classes or sub-classes of antimicrobials
 
  * see :ref:`Rules for Combining Resistance Outcomes <model_building/meta_analysis_guidelines:Meta-Analysis Rules>` for more specific guidance
 
* across production stages
 
  * this includes where the effective stage is the same, but the measurement is taken at a different stage.

When a measurement is available for the same stage of production, the same food-animal and food-animal sub-population, pathogen, and antimicrobial (or sub-class of antimicrobial), as one or more others, they may be included in one of four types of meta-analysis:
  
Within Study, Same Antimicrobial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where multiple measurements are available describing the same factor, for the same resistance, the measurements should be combined using meta-analysis.

.. tip:: Two comparable sub-populations comprise the study population (e.g. barn A and barn B), and ceftiofur resistance is assayed for each. Meta-analysis is conducted for these observations.

Within Study, Same Antimicrobial Class (or Sub-Class)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where multiple measurements are available describing the same factor, for the same class or sub-class of resistance, the measurements should be combined using meta-analysis. 

.. tip:: Resistance to ceftiofur and ceftriaxone are both included in the assay. Meta-analysis is conducted for these observations, and the resistance is reported at the sub-class level (third-generation cephalosporin resistance).

Resistance to ceftiofur and ceftriaxone are both included in the assay, and there are two comparable sub-populations which comprise the study population. Meta-analysis is conducted for all of these observations, and the resistance is reported at the sub-class level (third-generation cephalosporin resistance).

Across Studies, Same Antimicrobial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where multiple measurements are available describing the same factor, for the same resistance, and the experimental conditions are comparable, the measurements should be combined using meta-analysis.

.. tip::
    Two studies measure the effect of production type (e.g. organic vs. conventional) on ceftiofur resistance. Meta-analysis is conducted for these observations.
 
Across Studies, Same Antimicrobial Class (or Sub-Class)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
Where multiple measurements are available describing the same factor, for the same class or sub-class of resistance, and the experimental conditions are comparable, the measurements should be combined using meta-analysis.
     
.. Tip:: Two studies measure the effect of production type (e.g. organic vs. conventional), one on ceftiofur resistance, and the other on ceftriaxone resistance. Meta-analysis is conducted for these observations.
    

Meta-analysis Rules
-------------------

Resistance Outcomes
~~~~~~~~~~~~~~~~~~~

*Generally*, two or more factors may be combined using meta-analysis if their resistance outcomes belong to the same antimicrobial class or sub-class.

.. Tip:: Check that you have the correct antimicrobial class for each of your resistance outcomes. The ATC vet codes (the classification system we use in CEDAR) sometimes classify them slightly differently than they should be.

The table below outlines some common antimicrobials, their antimicrobial class, and which other antimicrobials they may or may not be combined with via meta-analysis. If an “M” is present in the Meta-analysis Status column for a particular antimicrobial, that antimicrobial may be combined with other antimicrobials marked with an “M” that share the same antimicrobial class (and *likely* may also be combined with other antimicrobials within that same antimicrobial class that are not listed here). Antimicrobials which are the only entries for their corresponding antimicrobial class, and for which the Meta-analysis Status column is blank may also *likely* be able to be combined with other antimicrobials within that same antimicrobial class that are not listed here.

======================================== ================================== ====================
Antimicrobial                            Antimicrobial Class                Meta-analysis Status
======================================== ================================== ====================
cefalotin                                1GC                                M 
cefazolin                                1GC                                M 
cefalexin                                1GC                                M
cefotaxime                               3GC                                M 
cefpodoxime                              3GC                                M 
ceftiofur                                3GC                                M
ceftriaxone                              3GC                                M 
cefpirome                                4GC           
spectinomycin                            aminocycitol                       M 
amikacin                                 aminoglycoside
apramycin                                aminoglycoside
dihydrostreptomycin                      aminoglycoside
gentamicin                               aminoglycoside
kanamycin                                aminoglycoside
neomycin                                 aminoglycoside
streptomycin                             aminoglycoside
tobramycin                               aminoglycoside
chloramphenicol                          amphenicol                         M 
florfenicol                              amphenicol                         M
imipenem and cilastatin                  carbapenem
cefoxitin                                cephamycin
trimethoprim                             diaminopyrimidine
sulfamethoxazole and trimethoprim        diaminopyrimidine with sulfonamide M 
sulfadiazine and trimethoprim            diaminopyrimidine with sulfonamide M 
ciprofloxacin                            fluoroquinolone                    M
enrofloxacin                             fluoroquinolone                    M
marbofloxacin                            fluoroquinolone                    M
azithromycin                             macrolide                    
furazolidone                             nitrofuran derivatives             M
nitrofurantoin                           nitrofuran derivatives             M
amoxicillin                              penicillin                         M
ampicillin                               penicillin                         M 
tiamulin                                 pleuromutilins
amoxicillin and beta-lactamase inhibitor potentiated penicillin
nalidixic acid                           quinolone
sulfafurazole                            sulfonamide                        M 
sulfamethoxazole                         sulfonamide                        M 
chlortetracycline                        tetracycline                       M
oxytetracycline                          tetracycline                       M
tetracycline                             tetracycline                       M
======================================== ================================== ====================

.. Important:: For amoxicillin, ampicillin, and piperacillin, it is important to verify that the indications in this table pertain to situations where these antimicrobials are present alone and not in combinations such as amoxicillin and clavulanic acid, sulbactam (i.e. ampicillin sulbactam), tazobactam (i.e. piperacillin tazobactam), etc. When present alone, they may be combined via meta-analysis (amoxicillin & ampicillin & piperacillin). They may also be combined when present in combination (e.g. amoxicillin and clavulanic acid & ampicillin and sulbactam). However, “alone” and a combination **should not** be combined via meta-analysis (e.g. amoxicillin & amoxicillin and clavulanic acid).


Genomic resistance outcomes
+++++++++++++++++++++++++++

Only resistance outcomes pertaining to the exact same gene may be combined using meta-analysis. Different genes which confer (or may confer) resistance to the same antimicrobial class or individual antimicrobial should **not** be combined (i.e. tetA and tetB), nor should they be combined with any phenotypic outcomes.

.. Tip:: Gene subgroups (such as blaCTX M1, blaCTX M2) should not be combined with one another.

Different units of analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Factors measured using different units of analysis (i.e. isolate and flock) may be combined with meta-analysis.

Production type factors
~~~~~~~~~~~~~~~~~~~~~~~

Factors comparing organic and conventional production may be combined with factors comparing antimicrobial-free and conventional production. As all organic production is by default antimicrobial-free, but not all antimicrobial-free production is organic, the meta-analysis result should be reported as an antimicrobial-free vs conventional production comparison.

Antimicrobial use factors
~~~~~~~~~~~~~~~~~~~~~~~~~

The following AMU-related factor pairings may be combined using meta-analysis:

1.       Different routes of administration: i.e. feed and water

The following AMU-related factor pairings **should not** be combined using meta-analysis:

1.       Subtherapeutic AMU and Therapeutic AMU
2.       Therapeutic AMU and Prophylactic AMU (and other similar pairings where the “intent” of the AMU is not the same, including those involving Metaphylactic AMU)
3.       Continuous AMU and Pulsed AMU

.. Note:: To make decisions based on the above three pairings, the authors of a paper must have made an explicit designation in their paper as to the type of dosage, intent, or temporal pattern of the AMU (for example, a clear indication of whether a particular dosage is subtherapeutic or not). If numerical values for the dosage are the only information provided, for instance, we would not attempt to classify that ourselves as subtherapeutic, therapeutic, etc.

A good general rule of thumb is to keep any unknown AMU regimes separate from known dose regimes. For instance, a generic “tylosin use (any use)” factor, where no indication is given as to the duration, intent, or dosage of use should not be combined with a “continuous tylosin use” or a “therapeutic tylosin use” factor. However, two generic “tylosin use” factors may be combined.

Feed additive factors
~~~~~~~~~~~~~~~~~~~~~

For factors related to the use of feed additives such as probiotics and prebiotics, use caution when combining different brands (check the ingredients first). Generally, different brands of additives should not be combined.

How is the meta-analysis performed?
-----------------------------------

Please see :ref:`Adding meta-analysis groupings <model_building/processing_cedar_queries:Adding meta-analysis groupings>` for instructions on how to prepare your timber for meta-analysis.

Our :ref:`sawmill R package <model_building/sawmill:The sawmill R Package>` performs meta-analysis using the **Metafor Package**.

We use a random-effects model.
 
There are a number of ways to estimate heterogeneity:

- Restricted Maximum Likelihood (REML)
  
  - default, requires convergence (it’s ML, so iterative)
  
- DerSimonian-Laird
  
  - a Olaf-approved alternative (non-iterative) 

We use **REML**. We calculate the effect size based on Odds Ratio (technically log-OR), and SE of the log-OR.

For more details on the math behind the meta-analysis go :ref:`here. <10_reference/math_stats:Meta-analysis>`