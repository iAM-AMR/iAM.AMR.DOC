

===========
iAM.AMR.HUB
===========

Recall that the iAM.AMR models are organized into stories – collections of different drug-bug-commodity combinations – that together describe an important facet of resistance in the agri-food production system in Canada.

Despite this variability, there are a number of functions and parameters common to all models. To ensure these parameters are consistently available, uniformly implemented, and easily updatable, they are included in a separate filed module, the **iAM.AMR.HUB**.

.. hint:: The Hub module is so named for its hub-and-spoke implementation; each story model (spoke) connects back to the central hub, like spokes on a wheel.

Note, because the Hub module is a filed module  (i.e. is stored in a separate module file), **you must have a copy of both the Hub module AND the story model, to run the story models**.

.. important:: You can download the iAM.AMR.HUB `here <https://github.com/iAM-AMR/iAM.AMR.HUB>`_.

Module Contents
---------------
The Hub module contains the following functions:

-	Get Data (getData)
   A function used to select the data to import from the Hub module into a story model
-	Counts to Prevalence (countPrevalence)  
   A function to calculate a prevalence, represented by a Beta() distribution, from count data in a countTotal table
-	Interleave Tables (Interleave)
   A function to merge two similarly indexed tables, overwriting the data in the target table with matched data where available.


The Hub module supplies the following data:

-	CIPARS-derived baseline probabilities of resistance (see: Baseline)
-	CIPARS-derived retail microbial recovery rate (see: Recovery Rate)
-	commodity consumption rates (see: Consumption Rate)
-	population size by region (see: Population)


The Hub Module also contains the OR Matrix Library.







Hub Data
--------

countTable Data Format
~~~~~~~~~~~~~~~~~~~~~~
Here, we define a **countTotal** table as a table of counts of positives, and of total observations of a trial, indexed by the *CountTotal* index at positions ‘Count’ and ‘Total’ respectively. 

The purpose of a countTotal table is to store the number of positive observations and the number of total observations of a trial – across an arbitrary number of additional indices – in a standardized format, for manipulation using array operations. For example, directly calculating prevalence (Count / Total), or for use in a distribution (specifically the binomial distribution family, which considers the number of successes in a series of independent experiments). See the Math and Stats  Section for more details.

Both the CIPARS-derived baseline probabilities of resistance, and the CIPARS-derived retail microbial recovery rate are specified as countTotal tables.


Baseline
~~~~~~~~
The baseline data are stored as counts (as countTotal tables), or as prevalences, in separate tables for each microbe.   

Why do we separate baseline data into tables by microbe? Or by any index for that matter – why not use one big table? Analytica supports – and is indeed designed for – highly dimensional tables, and we’ve extolled the virtue of Analytica’s Intelligent Array system throughout this documentation. 

We separate them because these tables don’t actually share all of the same indices; the microbial sub-type index changes, depending on the microbe. Recall from our discussion of Analytica’s Intelligent Array system , that when presented with two different indices, Analytica will automatically array-abstract, and fill-in and compute values for each combination of index A and index B. If we were to include Salmonella and Campylobacter sub-types indices in the same table – for example – Analytica would create cells for the intersection of each of these indices, both the parent (i.e. Salmonella or Campylobacter), and the child (i.e. the subtype). The resultant table would have cells such as “Salmonella jejuni” or “Campylobacter Heidelberg”).

This seems simple enough to address (ignore nonsensical combinations), but each nonsensical slice of the table is replicated for each year, region, animal, and antimicrobial. So it’s not just “Salmonella jejuni”, but “Salmonella Enterica jejuni”, “Salmonella Heidelberg Jejuni”, and so on – this quickly becomes computationally prohibitive. 

.. tip:: Often times, we may refer to arrays with multiple, non-congruent indices as “jagged’, because they aren’t of consistent size across each other index.

All of the available baseline data is taken from CIPARS surveillence data, available in the annual reports. 

There is currently no baseline data directly specified as a prevalence.


Recovery Rate
~~~~~~~~~~~~~

To Do.


Consumption Rates
~~~~~~~~~~~~~~~~~

To Do.


Population
~~~~~~~~~~

To Do.




Hub Functions
-------------

Each function is described within its own Description attribute. Where necessary, further information is provided here.

Get Data
~~~~~~~~
The Get Data function takes a table indexed by the baseline indices, and returns a subset of the data, filtered by the provided story-model indices. 

.. note:: If a main-model index is omitted, the table will be returned indexed by the baseline index.


Count to Prevalence
~~~~~~~~~~~~~~~~~~~
The Count to Prevalence function converts a countTotal table into a table of prevalences, represented by a Beta distribution. For more details on the use of the Beta() distribution, see the Math and Stats section.

By default, the function replaces missing count and total values with ‘1’ and ‘15’ respectively. Alternatively, it can return ‘Null’, or a Beta() distribution specified with alternative default count and total values.

.. important:: The defaults specified here are not the direct parameters used in the Beta() distribution. See the Math and Stats section for more details.


Interleave
~~~~~~~~~~
The Interleave function combines two similarly-indexed tables, overwriting data in <<originalData>> with <<newData>> where matched and available.

.. note:: Interleave() respects array abstraction; where <<newData>> is specified with fewer indices than <<originalData>>, <<newData>> is expanded (abstracted) to fit.

By default, Interleave() replaces all data for which there is a match (<<replaceMissing>> = True). To only replace existing data (i.e. replace existing data, not fillng data gaps), set (<<replaceMissing>> = False.


Depreciated Functions
---------------------

To Do.


HUB vs. HUB.GM
--------------

To ensure end-users do not accidently overwrite or change values in the Hub module (and subsequently propagate these changes to all story models), we maintain two different copies of the Hub module: the Gold Master [GM] (iAM.AMR.HUB.GM) and the production copy (iAM.AMR.HUB). 

The Gold Master (a term borrowed from audio and software engineering) is  -- as the name suggests -- the master copy of the Hub module. The GM is where all development (additions, deletions, changes) occurs. The production module is a *protected and encrypted* copy of the mutable (editable) GM module, connected to each of the story models. 

See more details in the `iAM.AMR.HUB repo <https://goto.iam.amr.pub/repo-hub>`_.

iAM.AMR.HUB
   
 - iAM.AMR.HUB is the main, working-copy of the Hub module. 
 - iAM.AMR.HUB is an encrypted, browse-only (non-editable) copy of iAM.AMR.HUB.GM.
 - Download and use iAM.AMR.HUB in your models, or **select this module** if prompted to locate the Hub module by Analytica.
 
iAM.AMR.HUB.GM

 - iAM.AMR.HUB.GM is the secondary, developer copy of the Hub module.
 - iAM.AMR.HUB.GM is an unencrypted, editable copy of iAM.AMR.HUB.
 - Download and edit iAM.AMR.HUB.GM to add new features to the module; **do not select this module** if prompted to locate the Hub module by Analytica.

iAM.AMR.HUB.EX

 - An example model demonstrating the use of the Hub module.


.. important:: The iAM.AMR.HUB module is the module to which the story models are linked. Do not link your story model to the iAM.AMR.HUB.GM module.

What does this mean in practice? To make changes to our Hub module, we first make the changes to the GM. Then, we save a protected copy, overwriting the existing production model. Because the name and location of the Hub module do not change, the story models automatically recognize the new production copy, and any changes are propagated when the story models are opened.

You can think of making changes to the Hub module like making changes to a manuscript. All changes are made in Microsoft Word, before creating a PDF to submit to the journal.

Model Documentation
-------------------

The HUB is equipped with an Analytica library called Model Documentation.
This library provides a way to export all descriptions and definitions for objects in your model to an Excel spreadsheet.

.. figure:: /assets/figures/model_documentation_hub.jpg
    :align: center

    The iAM.AMR.HUB model, with the model documentation library highlighted

Detailed instructions for using this library can be found by clicking on the Model Documentation node (highlighted in the above figure) within the iAM.AMR.HUB itself.

