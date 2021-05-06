

The sawmill R Package
=====================

The **sawmill** R package processes queries from the *CEDAR* (*Collection of Epidemiologically Derived Factors Associated with Resistance*) database, performing quality control, and calculating measures of association (odds ratios).
Optionally, it can also perform meta-analysis.

Introduction
------------

Why is sawmill needed?
~~~~~~~~~~~~~~~~~~~~~~

Each of the iAM.AMR models are informed by one more queries to the CEDAR database. The exported query results are called **timber**. Unfortunately, these raw timber are not usable, as they lack key calculated fields (such as the odds ratio), and have not been screened for simple errors.

What exactly does sawmill do, in brief?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sawmill essentially looks at each factor in the timber, checks that the raw data required to calculate an odds ratio and standard error of the log(odds ratio) are available and usable, and then performs those calculations. 

More details can be found in the sawmill GitHub repository's latest `release notes <https://github.com/iAM-AMR/sawmill/releases>`_, as well as in the :ref:`function help files <data_extraction/Sawmill:Access the function help files>`.

How is sawmill set up?
~~~~~~~~~~~~~~~~~~~~~~

First and foremost, sawmill is an R package. `According to <https://r-pkgs.org/intro.html>`_ Hadley Wickham and Jennifer Bryan:

   *In R, the fundamental unit of shareable code is the package. A package bundles together code, data, documentation, and tests, and is easy to share with others.*

sawmill is set up as a series of **functions**, each of which performs a specific step(s) in the processing pipeline. 

A **function**, according to `R - Functions <https://www.tutorialspoint.com/r/r_functions.htm>`_, is:

   *...a set of statements organized together to perform a specific task.*

Each function is in an individual R script file, where the name of the script file matches the name of the main function it contains. 
All script files can be found in the `R <https://github.com/iAM-AMR/sawmill/tree/master/R>`_ directory of the sawmill GitHub repository.

The pipeline is set in motion by running the main function, *start_mill*, using the following command::

   sawmill::start_mill()

This function calls all other subsequent functions.

.. important:: Before proceeding, you will need to have both R and RStudio installed on your computer. If you do not have them both installed, please see :ref:`R and RStudio <09_technology/software:R and R Studio>`.

Terminology
-----------

In keeping with the logging theme of the sawmill pipeline, the following terminology is used throughout this documentation:

**Raw timber**: the input Excel (*.xlsx*) file of factors, exported from CEDAR, which acts as the input to sawmill.

**Grain**: the set of fields used to define a particular factor (for instance, a prevalence table or a contingency table).

**Processed timber** or **planks**: the processed *.csv* file of factors that sawmill provides as an output.

Navigate RStudio
----------------

.. note:: This section provides only a cursory overview of RStudio, focusing on those features necessary for running sawmill. For a more comprehensive overview, see `Introduction to RStudio <https://dss.princeton.edu/training/RStudio101.pdf>`_.

RStudio's interface looks something like this:

.. figure:: /assets/figures/RStudio_sawmill_open.jpg
   :align: center
   :alt: Image of RStudio's interface.

   RStudio interface with sawmill loaded.

It can be divided into four key regions.

Console
~~~~~~~

R commands can be entered here.

.. figure:: /assets/figures/RStudio_lower_left.jpg
   :align: center
   :alt: Image of RStudio with lower left region highlighted to show location of Console.

   RStudio console.

Script editor
~~~~~~~~~~~~~

This is where R scripts can be viewed and edited. 

Each open script file appears as a tab at the top of this region.

To run a block of code, highlight it in the script editor and click the *Run* button.

.. figure:: /assets/figures/RStudio_upper_left.jpg
   :align: center
   :alt: Image of RStudio with upper left region highlighted to show the location of the script editor.

   RStudio script editor.

Navigation pane
~~~~~~~~~~~~~~~

There are two important tabs in this pane: *Files* and *Help*.

*Files* shows the contents of the current working directory. 
Here, users can navigate to R scripts they wish to view in the script editor.

*Help* is where the individual function :ref:`help files <data_extraction/Sawmill:Access the function help files>` are viewed.

.. figure:: /assets/figures/RStudio_lower_right.jpg
   :align: center
   :alt: Image of RStudio with lower right region highlighted to show the location of the navigation pane.

   RStudio navigation pane.

Build tab
~~~~~~~~~

When the **Build** tab is selected, a package can be installed and/or re-loaded using the *Install and Restart* feature.

.. figure:: /assets/figures/RStudio_upper_right.jpg
   :align: center
   :alt: Image of RStudio with upper right region highlighted to show the location of the build tab.

   RStudio build tab.

How It Works
------------

Acceptable grains
~~~~~~~~~~~~~~~~~

The set of fields used to define a factor (the factor's grain) varies from reference to reference. 
Not all grains can be used to calculate an odds ratio and as such, not all are usable by sawmill.

The formula for the odds ratio requires a complete contingency table, so any acceptable grain must be able to be converted to the following:

========  ====  ====
Group     AMR+  AMR- 
========  ====  ====
Exposed   A     B
Referent  C     D
========  ====  ====

As a result, sawmill is capable of working with the following grains.

Contingency tables
++++++++++++++++++

Contingency tables are usable in two different forms.

.. table:: Contingency Table without Totals
   :widths: 50 10 10 30

========  ====  ====  ======
Group     AMR+  AMR-  Total
========  ====  ====  ======
Exposed   A     B     
Referent  C     D     
========  ====  ====  ======

If AMR- values are not available, totals must be provided.

.. table:: Contingency Table with Totals
   :widths: 50 10 10 30

========  ====  ====  ======
Group     AMR+  AMR-  Total
========  ====  ====  ======
Exposed   A           nexp
Referent  C           nref
========  ====  ====  ======

Prevalence tables
+++++++++++++++++

AMR- prevalences are optional, as they are not used by sawmill.

========  ====  ====  ======
Group     AMR+  AMR-  Total
========  ====  ====  ======
Exposed   P%    (R%)  nexp
Referent  Q%    (S%)  nref
========  ====  ====  ======

.. important:: The values in the total column, unlike the other columns, are counts, not percentages. For instance, *nexp* and *nref* might represent the total numbers of isolates in each group.

Odds ratios
+++++++++++

========  ====  ========  ==================
Lower CI  OR    Upper CI  Significance Value
========  ====  ========  ==================
oddslo    odds  oddsup    pval
========  ====  ========  ==================

.. note:: sawmill will not raise an error if the p-value is not provided, but it cannot calculate one for odds ratio grains.

Access sawmill
--------------

Locate sawmill
~~~~~~~~~~~~~~

The sawmill R package is available at the `iAM.AMR/sawmill GitHub Repository <https://github.com/iAM-AMR/sawmill>`_. 

Open sawmill
~~~~~~~~~~~~

Once at the repository page, scroll down until you see the *README.md* file (captured in the image below). 
This *README* contains important instructions related to sawmill.

.. figure:: /assets/figures/README.jpg
   :align: center
   :alt: Image of README.md file for sawmill on github.

   *README.md* file on GitHub.

Navigate to the `Installation and Use <https://github.com/iAM-AMR/sawmill#installation-and-use>`_ section of this file.

You can choose either the **Bootstrap** installation or the **Standard** installation, depending on your comfort level with R/RStudio and what you intend to use sawmill for. 

.. attention:: Complete steps 1 and 2 of your chosen installation procedure and then return to this documentation. The final steps are related to the use of sawmill and will make more sense upon reading the rest of this page, as well as the related page :ref:`Processing CEDAR Exports <data_extraction/processing_cedar_queries:Processing CEDAR Exports>`.

Navigate sawmill
----------------

Once you have installed sawmill, you may wish to get more familiar with the script files themselves, and/or the accompanying function help files.

.. note:: This section is largely optional, particularly for those who have chosen the **Bootstrap** installation procedure, or those not intending to tweak/make development changes to sawmill. However, it is a useful reference, especially the section on :ref:`Accessing the function help files <data_extraction/Sawmill:Access the function help files>`.

View the R script files
~~~~~~~~~~~~~~~~~~~~~~~

#. Select *Files* in the **Navigation pane**
#. Navigate to the directory where the GitHub repository is saved, and open the *R* directory
#. Open *start_mill.R* and *mill.R* in RStudio. These scripts show the order in which the other main functions are called (in other words, the order of the steps (functions) in the processing pipeline).
#. Open any other *.R* files you would like to examine

Access the function help files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, select *Help* in the **Navigation pane**.

Then, enter the following line into the **Console**::

   ?function_name()

If that does not work, try entering this line::

   ?sawmill::function_name()

For example, if you wanted to view the help file for the *debark* function, you would enter::
   
   ?debark()