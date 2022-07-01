

Communications Style Guide
==========================

General Conventions
-------------------

Appending a suffix on 'model' requires the insertion of a second 'l':  

- e.g. 'modeller'; 'modelling'

The following should always be hyphenated or (not hyphenated) as follows:

- Model-builder
- End-user
- Farm-to-fork pathway
- Agri-food chain

Conventions for Analytica Terms
-------------------------------

The following should always be capitalized:

- Intelligent Array

The proper name of functions and objects should always be capitalized where refering to a generic function or object: 

- e.g. 'Choice function'; 'Table()'; 'Uniform function'

The names of specific objects should always be capitalized and italicized. The type of object is not capitalized or italicized:

- e.g. 'the *Interface* index'; 'the *Frequency* node'

Common Definitions
------------------

Antimicrobial resistance: 
   An in vitro measure to interpret a bacteria’s ability to resist compounds intended to inhibit bacterial growth and/or kill the bacteria.

Baseline probability (p\ :sub:`o`\):
   The prevalence of antimicrobial resistance at the earliest site of measurement in the defined agri-food chain (e.g., prevalence of antimicrobial resistance in broiler chicks at placement in the barn). 

Estimated probability (p\ :sub:`E`\):
   The estimated probability of antimicrobial resistance leaving a node in the iAM.AMR after adjustment of the baseline probability by the 1) odds ratios, and 2) frequencies of occurrence of factors potentially associated with antimicrobial resistance. Depending on the location of the node in the model, the estimated probability may become the baseline probability of resistance for the next node (e.g., baseline for abattoir node (p\ :sub:`A`\) or baseline for retail node (p\ :sub:`R`\)) or the final probability in the model (F\ :sub:`P`\). 

Factor: 
   A measured observation, such as antimicrobial use, different types of management systems, disinfectant use at slaughter plants, and packaging at retail. 

iAM.AMR: 
   Integrated Assessment Model for Antimicrobial Resistance.

Integrated assessment model: 
   A modelling approach that synthesizes data from many sources (e.g., different areas of study, varying methods, diverse disciplines, scales of measurement, sources of uncertainty) that intends to address some of the complexity within systems to support decision-making and/or policy interventions.

Local sensitivity analysis: 
   An approach to describe changes in a model outcome(s) at a single node (e.g., estimated probability) with a change (including infinitesimal changes) in one or more of the other input model parameters (e.g., baseline probability, odds ratio).    

Node: 
   An element within the iAM.AMR that represents a particular site (e.g., farm) within the system of interest (e.g., broiler chicken production industry).

Scenario: 
   Antimicrobial resistance to an antimicrobial/antimicrobial class in a specific bacterial genus/species in a defined host population (e.g., extended-spectrum cephalosporin-resistant Salmonella from broiler chicken).

Site: 
   A generic location (e.g., farm) in the system of interest (e.g., broiler chicken production industry) that is represented by a node in the iAM.AMR.

Study Groups
~~~~~~~~~~~~
   
Study groups should be named as follows:

**Comparator group**: The group which represents the default practice in Canadian industry, or the least interventionist. The legacy term for this group is the referent group.

**Factor group**: The group which represents the less common, or more interventionist group. The legacy term for this group is the exposed group.
   
.. note:: If a study has more than two groups, all groups except the Comparator should be titled Factor 1, Factor 2, etc. For example, a study examining the effect of AMU on AMR may have multiple factor groups, each representing a slightly different dosage or treatment regime.

Key Words
~~~~~~~~~
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" are to be interpreted as described in `RFC 2119 <https://www.ietf.org/rfc/rfc2119.txt>`_:

MUST
   This word, or the terms "REQUIRED" or "SHALL", mean that the definition is an absolute requirement of the specification.
MUST NOT   
   This phrase, or the phrase "SHALL NOT", mean that the definition is an absolute prohibition of the specification.
SHOULD
   This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course.
SHOULD NOT   
   This phrase, or the phrase "NOT RECOMMENDED" mean that there may exist valid reasons in particular circumstances when the particular behavior is acceptable or even useful, but the full implications should be understood and the case carefully weighed before implementing any behavior described with this label.
MAY
   This word, or the adjective "OPTIONAL", mean that an item is truly optional. An implementation which does not include a particular option MUST be prepared to interoperate with another implementation which does include the option, though perhaps with reduced functionality. In the same vein an implementation which does include a particular option MUST be prepared to interoperate with another implementation which does not include the option (except, of course, for the feature the option provides).

Common Acronyms
~~~~~~~~~~~~~~~
AAFC
   Agriculture and Agri-food Canada

AMR
   Antimicrobial Resistance

AMU
   Antimicrobial Use

CFIA
   Canadian Food Inspection Agency

CIPARS
   Canadian Integrated Program for Antimicrobial Resistance Surveillence

CSS
   Cascading Style Sheets

GRDI
   Genomics Research and Development Initiative

HC
   Health Canada

NSD
   National Service Desk

PHAC
   Public Health Agency of Canada

SSC
   Shared Services Canada

3GC
   Third-generation Cephalosporins

Terms for Factor Applicability to the Canadian Context
------------------------------------------------------

This terminology is used to describe factor applicability to the Canadian context, and should act as a guide for selecting which factors to run separately or together in the models.
We consider the applicability separately in three different time periods: Past, Present, Future. This avoids us requiring terms referencing potential changes between time periods.

These terms can be applied nationally or regionally depending on the circumstance; the terms 'standard' and 'uncommon' should not be interpreted in a geographical context (at least for now). For example, a standard practice implemented only in Alberta is still considered a standard practice, even though it may not be used in other regions.

While each of these categories has a different degree of frequency of occurrence within Canada (i.e. the frequency of occurrence of a standard practice would be closer to 100% relative to the other categories), we have not ascribed specific frequency thresholds to these categories--their purpose is to provide a qualitative categorization.

Standard Practice
~~~~~~~~~~~~~~~~~

These practices are widely adopted in industry, or are common responses to predictable exogenous events.

For example: biosecurity practices, therapeutic antimicrobial use, endemic disease treatment.

Uncommon Practice
~~~~~~~~~~~~~~~~~

These practices are adopted by a subset of industry, are used for production of a niche product, or are responses to unpredictable exogenous events.

For example: alternative health products, probiotics, competitive exclusion products, unusual disease treatment.

Banned
~~~~~~

These are practices that are not used in Canada, or are not permitted by strongly enforced policy.

For example: use of `banned drugs <https://www.canada.ca/en/health-canada/services/drugs-health-products/veterinary-drugs/list-banned-drugs.html>`_

Discouraged
~~~~~~~~~~~

These are practices that are discouraged by legislation or industry bodies, are recognized as “bad-practice”, or are being phased out of practice in pending legislation or industry action.

These include practices not currently used in Canada, but would otherwise fall into this category if adopted.

For example: use of Category I antimicrobials for growth promotion.


Not Adopted
~~~~~~~~~~~

These are practices that have not been considered, or could not be practically implemented in Canada.

For example: out-wintering in extreme conditions

Unknown / other
~~~~~~~~~~~~~~~