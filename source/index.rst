

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

- E. coli
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
   :caption: Analytica
   :maxdepth: 2
   :numbered:
   
   /analytica/ana_get_started.rst
   /analytica/analytica.rst
   /analytica/mod.rst

.. toctree::
   :caption: Data
   :maxdepth: 2
   :numbered:

   /data_extraction/search
   /data_extraction/CEDAR
   /data_extraction/data_extract
   /data_extraction/data_extract_rules
   /data_extraction/form_reference
   /data_extraction/form_factor
   /data_extraction/processing_cedar_queries
   /data_extraction/Sawmill
..   /02_project/Data_Extract_Notes

.. toctree::
   :caption: Models
   :maxdepth: 2
   :numbered:

   /models/external_data.rst
   /models/architecture.rst
   /models/hub.rst

.. toctree::
   :caption: Other Activities
   :maxdepth: 2
   :numbered:

   /03_activities/data_harmonization


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

   /10_reference/documentation
   /10_reference/reST
   /10_reference/math_stats

.. toctree::
   :caption: Team
   :maxdepth: 2
   :numbered:

   /team/publications



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
