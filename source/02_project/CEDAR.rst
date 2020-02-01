

The CEDAR Database
==================

The *Collection of Epidemiologically Derived Associations with Resistance* or *CEDAR* database is the central repository of epidemiological data for the iAM.AMR project.

Introduction
------------

What is a database?
~~~~~~~~~~~~~~~~~~~
A **database** is a structured set of data, organized a way that makes it easy to search for, select, and retrieve specific subsets of information. There is no one defining characteristic that makes a ‘database’ a ‘database’, but one can usually differentiate a database from a simpler application by its formal structure, and rigidly defined data-relationships.

.. tip:: We often use the term ‘database’ to refer to the sum of the data, the data structure, and the software used to create, manipulate, and access the database. However, we can more accurately refer to the data and its structure as the database, and the software as the **database management system** or **DBMS**.

Why use a database?
~~~~~~~~~~~~~~~~~~~
There are numerous benefits of using a database to store large amounts of complex data, most of which become evident when we contrast a database against a spreadsheet or **flat-file**.

Take a look at the table below, which includes demographic and political information for some of Canada’s largest cities (circa 2020). This represents a flat-file approach.

===========  ==========  ====================  ================  ==========
City         Province    Population (2016)     Premier           Party
===========  ==========  ====================  ================  ==========
Toronto      Ontario     5,429,524             Doug Ford         OPC   
Montreal     Quebec      3,519,595             François Legault  CAQ   
Vancouver    BC          2,264,823             John Horgan       NDP   
Calgary      Alberta     1,237,656             Jason Kenney      UCP   
Edmonton     Alberta     1,062,643             Jason Kenney      UCP   
Winnipeg     Manitoba    711,925               Brian Pallister   PCM   
Quebec City  Quebec      705,103               François Legault  CAQ   
Hamilton     Ontario     693,645               Doug Ford         OPC   
Guelph       Ontario     132,397               Doug Ford         OPC   
===========  ==========  ====================  ================  ==========

There are two obvious drawbacks to this approach. The first is practical -- this table contains a number of duplicate values, which increase the size of the table, and add opportunities for input error.

The second is more conceptual, in that this table has no singular purpose -- if you had to title it, what would that title be? When we mix heterogenous data (i.e. demographic data with political data), we often lose clarity, and forget where we stored data, or with whom that data should be shared.

The alternative is a **relational database**, which involves organizing our complex data, and defining relationships between the disparate parts. Take a look at the tables below.

==  ===========  ====================  
ID  City         Population (2016)   
==  ===========  ==================== 
01  Toronto      5,429,524             
02  Montreal     3,519,595             
03  Vancouver    2,264,823             
04  Calgary      1,237,656             
04  Edmonton     1,062,643             
05  Winnipeg     711,925               
02  Quebec City  705,103               
01  Hamilton     693,645               
01  Guelph       132,397               
==  ===========  ====================

==  ==========  ================  ==========
ID  Province    Premier           Party
==  ==========  ================  ==========
01  Ontario     Doug Ford         OPC   
02  Quebec      François Legault  CAQ   
03  BC          John Horgan       NDP   
04  Alberta     Jason Kenney      UCP   
05  Manitoba    Brian Pallister   PCM   
==  ==========  ================  ==========

Now each table has a singular theme or purpose, and is clear in the information it conveys. We have fewer error-prone entries (e.g. the names of the premieres), and fewer duplicate datapoints. And by matching the IDs in the table, we can recreate the main table if necessary, or share component parts without sharing the entire data collection. The benefits of a database approach are evident, even at this small of a scale.

What is the terminology?
~~~~~~~~~~~~~~~~~~~~~~~~
A **relational database** is a collection of **tables**, linked together by  **relationships**.

A **table** contains data, and consists of rows and columns. The **rows** -- also known as **tuples** or **records** -- are sets of data related to a single object. These sets consist of multiple, named elements of data, organized into **columns** -- also known as **attributes** or **fields**.

A **relationship** defines how we match data between tables. Often, this matching is done via unique **primary key** or **ID**.

A **form** is a graphical user-interface for entering data into the database.

A **query** is a request we pass to the database to retrieve a specific subset of records and fields, constrained by criteria we specify.

How do we store and access a database?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generally, databases are separated into two parts: a **front-end** and a **back-end**.  The front-end consists of the user-interface, through which we enter, manipulate, and retrieve data. The back-end consists of the data, organized into tables, and other storage formats.

.. tip:: The front-end and back-end can be thought of as a web browser and website respectively; the distributed front-end retrieves the information and displays it to the user, from the centralized back-end.

This configuration allows multiple users to simultaneously access and work with the same, always up-to-date set of information. However, it is important to note that the location of the back-end must be a server accessible to all users. 


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


