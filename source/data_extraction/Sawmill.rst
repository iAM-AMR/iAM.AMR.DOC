

The sawmill R Package
=====================

The **sawmill** package processes queries from the *CEDAR* (*Collection of Epidemiologically Derived Factors Associated with Resistance*) database, performing quality control, and calculating measures of association (odds ratios). 

Introduction
------------

Why is sawmill needed?
~~~~~~~~~~~~~~~~~~~~~~

Each of the iAM.AMR models are informed by one more queries to the CEDAR database. The exported query results are called **timber**. Unfortunately, these raw timber are not usable, as they lack key calculated fields (such as the odds ratio), and have not been screened for simple errors.

What exactly does sawmill do, in brief?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sawmill essentially looks at each factor in the timber, checks that the raw data required to calculate an odds ratio and standard error of the log(odds ratio) are available and usable, and then performs those calculations. 

More details can be found in the latest release notes, under the **sawmill** GitHub repository, as well as in the function help files (read on to find out how to access these).

How is sawmill set up?
~~~~~~~~~~~~~~~~~~~~~~

First and foremost, sawmill is an R package. `According to <https://r-pkgs.org/intro.html>`_ Hadley Wickham and Jennifer Bryan:

   *In R, the fundamental unit of shareable code is the package. A package bundles together code, data, documentation, and tests, and is easy to share with others.*

sawmill is set up as a series of **functions**, each of which performs a specific step(s) in the processing pipeline. 

A **function**, according to `R - Functions <https://www.tutorialspoint.com/r/r_functions.htm>`_, is:

   *...a set of statements organized together to perform a specific task.*

Each function is in an individual R script file, where the name of the script file matches the name of the main function it contains. 
All script files can be found in the **R** directory of the sawmill repository on GitHub.

The pipeline is set in motion by running the main function, **start_mill**, using the following command::

   sawmill::start_mill()

This function calls all other subsequent functions.

.. important:: Before proceeding, you will need to have both R and RStudio installed on your computer. If you do not have them both installed, please see :ref:`R and RStudio <09_technology/software:R and R Studio>`.

Navigate RStudio
----------------

.. note:: This section provides only a cursory overview of RStudio, focusing on those features necessary for running sawmill. For a more comprehensive overview, see `Introduction to RStudio <https://dss.princeton.edu/training/RStudio101.pdf>`_.

RStudio's interface looks something like this:

.. figure:: /assets/figures/RStudio_sawmill_open.jpg
   :align: center

   RStudio interface with sawmill loaded.

It can be divided into four key regions.

The console
~~~~~~~~~~~

R commands can be entered here. 

.. figure:: /assets/figures/RStudio_lower_left.jpg
   :align: center

   RStudio console.

The script editor
~~~~~~~~~~~~~~~~~

This is where R scripts can be viewed and edited. 

Each open script file appears as a tab at the top of this region.

To run a block of code, highlight it in the script editor and click the *Run* button.

.. figure:: /assets/figures/RStudio_upper_left.jpg
   :align: center

   RStudio script editor.

The navigation pane
~~~~~~~~~~~~~~~~~~~

There are two important tabs in this pane: **Files** and **Help**.

**Files** shows the contents of the current working directory. 
Here, users can navigate to R scripts they wish to view in the script editor.

**Help** is where the individual function help files are viewed. 

.. figure:: /assets/figures/RStudio_lower_right.jpg
   :align: center

   RStudio navigation pane.

The build tab
~~~~~~~~~~~~~

When the build tab is selected, a package can be installed and/or re-loaded using the *Install and Restart* feature.

.. figure:: /assets/figures/RStudio_upper_right.jpg
   :align: center

   RStudio build tab.

Access sawmill
--------------

The sawmill R package is available in the iAM.AMR/sawmill repository on GitHub. 
To be granted access, please ask the iAM.AMR Repository Administrator for the link.

Once on the repository page, scroll down until you see the *README.md* file (captured in the image below). 
*README.md* contains important instructions related to sawmill.

.. figure:: /assets/figures/README.jpg
   :align: center

   *README.md* file on GitHub.

Navigate to the *Installation and Use* section of this file.
You can choose either the *Bootstrap* installation or the *Standard* installation, depending on your comfort level with R/RStudio and what you intend to use sawmill for. 

.. attention:: Complete steps 1 and 2 of the *Bootstrap* installation or steps 1, 2, and 3 of the *Standard* installation and return to this documentation before completing step 3 of *Bootstrap* or step 4 of *Standard*. These steps are related to the use of sawmill and will make more sense upon reading the rest of this page, as well as the related page :ref:`Processing CEDAR Exports <03_activities/processing_cedar_queries:Processing CEDAR Exports>`.

Navigate sawmill
----------------

.. note:: This section is largely optional, particularly for those who have chosen the *Bootstrap* installation procedure, or those not intending to tweak/make development changes to sawmill. However, it is a useful reference, especially the section about accessing the function help files.

View the R script files
~~~~~~~~~~~~~~~~~~~~~~~

#. Select **Files** in the *Navigation pane*
#. Navigate to the directory where the GitHub repository is saved, and open the **R** directory
#. Open **start_mill.R** and **mill.R**. These scripts show the order in which the other main functions are called (in other words, the order of the steps (functions) in the processing pipeline).
#. Open any other **.R** files you would like to examine

Access the function help files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, select **Help** in the *Navigation pane*.

Then, enter the following line into the *Console*::

   ?function_name()

If that does not work, try entering this line::

   ?sawmill::function_name()

For example, if you wanted to view the help file for the **debark** function, you would enter::
   
   ?debark()