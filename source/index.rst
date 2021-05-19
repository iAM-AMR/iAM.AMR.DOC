

.. image:: assets/figures/iam.amr.logo.png
   :alt: The iAM.AMR project logo.

=================================
The iAM.AMR Project Documentation
=================================

Background
----------
Antimicrobial resistance (AMR) refers to the ability of microorganisms to withstand the effects of antimicrobials (to which they were formerly susceptible). In short, AMR reduces (or eliminates) our ability to treat certain types of infections. 

While the primary driver (cause) of AMR is human *antimicrobial use* (AMU), we're also concerned with animal AMU in the agri-food production system; AMU may increase AMR in zoonotic pathogens, and Canadians may be exposed to these pathogens through the consumption of microbially-contaminated foods.


Project
-------
The goal of the iAM.AMR project is to quantify the relative contribution of each *bug-drug-commodity* combination to Canadians’ overall exposure to resistant pathogens arising from the agri-food production system.

To that end, we searched the literature to identify factors affecting resistance, and used these factors in an integrated assessment model (IAM) framework to characterize the prevalence of AMR along the farm-to-fork continuum. Ultimately, we describe the number of servings at risk for each bug-drug-commodity combination.

This framework allows us to acheive a secondary objective: to understand how broad changes (e.g. encouraging a practice, or withdrawing an antimicrobial) can influence the entire agri-food system.


Scope
-----
The iAM.AMR project focuses on four [food-animal species | commodities]: 

- broiler chicken | chicken
- swine | pork
- dairy cattle or beef cattle | beef
- turkey | turkey

The iAM.AMR project focuses on four microbes:

- E.coli
- Salmonella Spp.
- Campylobacter Spp.
- Enterococcus Spp.

The iAM.AMR project focuses on resistance to drugs of human importance, including:

- macrolides
- tetracyclines
- fluoroquinolones
- third-generation cephalosporins


See the `Model Directory repository <https://goto.iam.amr.pub/repo-models>`_ for an up-to-date list of models and locations.


.. toctree::
   :caption: Welcome
   :maxdepth: 1

   /00_main/get_started
   /00_main/background
   /00_main/prostructure

.. toctree::
   :caption: CEDAR Database
   :maxdepth: 2
   :numbered:

   /cedar_database/cedar
   /cedar_database/data_extract_getting_started
   /cedar_database/form_reference
   /cedar_database/form_factor

.. toctree::
   :caption: Data
   :maxdepth: 2
   :numbered:

   /data_extraction/search
   /data_extraction/primary_screening
   /data_extraction/data_extract_rules
   /data_extraction/tips_and_tricks
   /data_extraction/processing_cedar_queries
   /data_extraction/sawmill
..   /02_project/Data_Extract_Notes

.. toctree::
   :caption: Models
   :maxdepth: 2
   :numbered:

   /models/ana_get_started.rst
   /models/analytica.rst
   /models/mod.rst
   /models/architecture.rst
   /models/hub.rst

.. toctree::
   :caption: Technology
   :maxdepth: 2
   :numbered:

   /09_technology/software.rst
   /09_technology/git
   /09_technology/add_page

.. toctree::
   :caption: Reference
   :maxdepth: 2
   :numbered:

   /10_reference/style_guide
   /10_reference/documentation
   /10_reference/data_harmonization
   /10_reference/math_stats




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
