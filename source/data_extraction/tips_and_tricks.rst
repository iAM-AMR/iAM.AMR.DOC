
=============================
Data Extraction Tips & Tricks
=============================

Extracting a Factor
-------------------

Defining the factor itself
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Which factors are considered relevant points of comparison, and which are not?**

Factors listed here are considered "unmodifiable" or "immutable", and thus not relevant for our purposes:

- :ref:`Immutable Factors <data_extraction/data_extract_rules:Immutable Factors>`

For examples of extractable factors, please see:

- :ref:`Common Factor Types <data_extraction/form_factor:Common factor types>`


Selecting exposed and referent groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Groups are otherwise referred to as levels.

**Which is which?**

:ref:`Selecting a Referent Level <data_extraction/data_extract_rules:Selecting a Referent Level>`

**What should I do when a group is not clearly defined (i.e. an "Other" group)?**

:ref:`Non-informative Levels <data_extraction/data_extract_rules:Non-informative Levels>`

**What should I do when there are more than two designated groups in the study?**

:ref:`Multiple Discrete Levels (Categories) <data_extraction/data_extract_rules:Multiple Discrete Levels (Categories)>`

:ref:`Non-informative Levels <data_extraction/data_extract_rules:Non-informative Levels>`


Selective Media
---------------

About Selective Media
~~~~~~~~~~~~~~~~~~~~~

A *growth medium* (plural *media*) or *culture medium* is a fluid designed to support the growth of microorganisms. There are many different types of media; some examples related to the iAM.AMR project include: MacConkey agar (for gram-negative bacteria), and XLD agar (commonly used for Salmonella spp.).

When compounds are added to media to select for the growth of specific organisms, it is referred to as *selective media*. However, it is important to differentiate the uses of selective media in the context of Antimicrobial Susceptibility Testing (AST):

#. to broadly exclude unwanted organisms  
#. to select for desired organisms  
#. as a simple AST  

Selective media are routinely used to broadly exclude unwanted organisms (purpose 1). For example, MacConkey agar is used to exclude gram-positive organisms when culturing gram-negatives. And media supplemented with third-generation cephalosporins (3GCs) are used to exclude other, faster-growing organisms while culturing *Campylobacter* spp. 

.. note:: This is an important example to note. *Campylobacter* are considered intrinsically resistant to 3GCs. The use of 3GCs is not selecting for *Campylobacter* based on this resistance – it’s excluding other, non-resistant organisms. This is in contrast to the example below, where fluoroquinolones are used to select for specific *Campylobacter*.

Selective media can also be used to select for specific organisms based upon a specific trait, such as antimicrobial resistance (purpose 2). In contrast to the previous example, we could add a fluoroquinolone to the medium to select for only fluoroquinolone-resistant *Campylobacter* – susceptible *Campylobacter* will be inhibited by the antimicrobial. 

Finally, selective media can be used as an AST in and of itself (purpose 3). Adding a suspect organism to selective media (and watching to see if it grows) can answer binary questions (e.g. is this organism resistant?). This gives no information on the level of resistance. To determine the level of resistance, this process must be repeated with various levels of selective compound (akin to broth dilution methodologies). 

Selective Media in CEDAR
~~~~~~~~~~~~~~~~~~~~~~~~

- In the context of data extraction, we only consider “selective media” as used for purpose 2: *to select for desired organisms*. 
- As per our data extraction rules, we prefer results from non-selective media where available. 
- There is a separate field for indicating where selective media are used for growth/culture, and for the AST itself (which can also be via selective media, as described above). 

.. hint:: Another way to think of this distinction: we only consider media “selective“ in the context of data extraction where the added compound could differentiate between organisms of the same species, based on an acquired resistance. 



