

==================
Data Harmonization
==================

To ensure CEDAR is interoperable with other databases, existing ontologies were used -- where possible -- to establish controlled vocabularies. 

External Data Sources in CEDAR
------------------------------

Antimicrobials
~~~~~~~~~~~~~~

Use
+++
A list of antimicrobials which may be administered, or to which resistance may be developed.

Description
+++++++++++
The list of antimicrobials was generated from the 2020 edition of the `WHO Collaborating Centre for Drug Statistics Methodology’s <https://www.whocc.no/>`_ `ATCvet system <https://www.whocc.no/atcvet/atcvet/>`_.

According to the WHO CCDSM:
 ATCvet is a system for the classification of substances intended for therapeutic use in veterinary medicine, and can serve as a tool for the classification of medicinal products. The ATCvet system is based on the same overall principles as the ATC system for substances used in human medicine. In most cases, an ATC code exists which can be used to classify a product in the ATCvet system. The ATCvet code is then created by placing the letter Q in front of the ATC code.

 In both the ATC and the ATCvet systems, preparations are divided into groups, according to their therapeutic use. First, they are divided into anatomical groups (1st level), on the basis of their main therapeutic use. Within most of the 1st level groups, preparations are subdivided into different therapeutic main groups (2nd level). Two levels of chemical/therapeutic/pharmacological subgroups (3rd and 4th levels) provide further subdivisions. At a 5th level, chemical substances are classified.

Data source and notes
+++++++++++++++++++++
The entire catalogue of ATCvet codes was scraped from the WHO CCDSM's website. All entries in anatomical groups QJ and QP, *Antiinfectives for systemic use* and *Antiparasitic products, insecticides and repellents*, were included in CEDAR. 

Where the same chemical substance (drug) appeared multiple times in different anatomical groups (level 1), the order of preference was: QJ > QP > Others.

Where the same chemical substance (drug) appeared multiple times in different therapeutic main groups (level 2), the classification with the broadest scope was preferred. For examaple, *ceftiofur* appears in both QJ01 (ANTIBACTERIALS FOR SYSTEMIC USE) and QJ51 (ANTIBACTERIALS FOR INTRAMAMMARY USE). The QJ01 code is preferred, as it has the broadest application (systemic vs intramammary).

Other antimicrobials that are not included in anatomical groups QJ or QP were added on an ad-hoc basis, as needed.

Additionally, several genes associated with resistance were added alongside the antimicrobials, under the classification closest to the resistance they effect. This allows users to select antimicrobials or genes as the resistance-outcome measured.


Locations
~~~~~~~~~

Use
+++
A list of countries, and sub-country regions where the study was conducted or from which the study population was sourced.

Description
+++++++++++
The list of locations were obtained from the ISO 3166 standard *Codes for the representation of names of countries and their subdivisions*. 

ISO 3166 is a standard published by the International Organization for Standardization (ISO) that defines codes for the names of countries, dependent territories, special areas of geographical interest, and their principal subdivisions (e.g., provinces or states). The official name of the standard is `Codes for the representation of names of countries and their subdivisions.
<https://www.iso.org/iso-3166-country-codes.html>`_

ISO 3166-1 – Codes for the representation of names of countries and their subdivisions – Part 1: Country codes defines codes for the names of countries, dependent territories, and special areas of geographical interest. It defines three sets of country codes:

 -	ISO 3166-1 alpha-2 – two-letter country codes which are also used to create the ISO 3166-2 country subdivision codes and the Internet country code top-level domains.  

 -	ISO 3166-1 alpha-3 – three-letter country codes which may allow a better visual association between the codes and the country names than the 3166-1 alpha-2 codes.  

 -	ISO 3166-1 numeric – three-digit country codes which are identical to those developed and maintained by the United Nations Statistics Division, with the advantage of script (writing system) independence, and hence useful for people or systems using non-Latin scripts.  

ISO 3166-2 – Codes for the representation of names of countries and their subdivisions – Part 2: Country subdivision code defines codes for the names of the principal subdivisions (e.g., provinces, states, departments, regions) of all countries coded in ISO 3166-1.

ISO 3166-3 – Codes for the representation of names of countries and their subdivisions – Part 3: Code for formerly used names of countries[4] defines codes for country names which have been deleted from ISO 3166-1 since its first publication in 1974.

The ISO 3166-1 standard currently comprises 249 countries, 193 of which are sovereign states that are members of the United Nations. Many dependent territories in the ISO 3166-1 standard are also listed as a subdivision of their parent country in the ISO 3166-2 standard.

Data source and notes
+++++++++++++++++++++
The `UNECE <http://www.unece.org/cefact/codesfortrade/codes_index.html>`_ provides a list of the ISO 3166-1 codes.


