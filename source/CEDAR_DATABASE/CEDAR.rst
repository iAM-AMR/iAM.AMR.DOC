

The CEDAR Database
==================

The *Collection of Epidemiologically Derived Associations with Resistance* or *CEDAR* database is the central repository of epidemiological data for the iAM.AMR project.

Introduction
------------

What is a database?
~~~~~~~~~~~~~~~~~~~
A **database** is a structured set of data, organized a way that makes it easy to search for, select, and retrieve specific subsets or combinations of information. There is no one defining characteristic that makes a *database* a *database*, but a database is often differentiated from a simpler application by its formal structure, and rigidly defined data-relationships.

.. tip:: We often use the term *database* to refer to the sum of the data, the data structure, and the software used to create, manipulate, and access the database. However, we can more accurately refer to the data and its structure as the database, and the software as the **database management system** or **DBMS**.

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

How do we store a database?
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generally, databases are separated into two parts: a **front-end** and a **back-end**.  The *front-end* consists of the user-interface, through which we enter, manipulate, and retrieve data. The *back-end* consists of the data itself, organized into tables and other data storage formats.

.. tip:: The *front-end* and *back-end* can be thought of as a web browser and website respectively; the distributed front-end is used to retrieve and display information from a centralized back-end.

This configuration allows multiple users to simultaneously access and work with the same, always up-to-date set of information. There is no explcit requirement for these parts to be seperate, however combining the files reduces multi-user capability.


Access CEDAR
------------

Locate CEDAR
~~~~~~~~~~~~
CEDAR consists of two files:

- the back-end file: *CEDAR_forest.accdb*
- the front-end file: *CEDAR.accdb*

You will need both to access CEDAR.

Locate the back-end file *CEDAR_forest.accdb*
+++++++++++++++++++++++++++++++++++++++++++++
If you are accessing CEDAR from the GoC network, locate *CEDAR_forest.accdb* in the CEDAR sub-folder of the iAM.AMR project. 

If you are accessing CEDAR from outside the GoC network, you will need a local of *CEDAR_forest.accdb*. 

Locate the front-end file *CEDAR.accdb*
+++++++++++++++++++++++++++++++++++++++
You can access the front-end file *CEDAR.accdb* from the `private CEDAR GitHub Repository <https://github.com/chapb/CEDAR>`_. You can request access to the repository by contacting `@chapb <https://github.com/chapb>`_. If you have been granted access, you can accept the invite `here <https://github.com/chapb/CEDAR/invitations>`_.


Open CEDAR
~~~~~~~~~~
Always access CEDAR by opening the front-end file *CEDAR.accdb*. When you open *CEDAR.accdb*, you will be presented with with a mostly blank screen:

.. figure:: /assets/figures/cedar_launch.png
   :align: center
   :alt: Image of CEDAR launch screen through Microsoft Access.

   The launch screen of *CEDAR.accdb*.

On the left-hand side, the database objects are organized by type (tables, queries, forms) in the Navigation Pane. 

What do I do if I get a security warning?
+++++++++++++++++++++++++++++++++++++++++

Upon opening *CEDAR.accdb*, you may see a security warning prompt like one of those shown below.
You may also see a security prompt if you are re-linking or using a new version of the *CEDAR.accdb* file.

.. figure:: /assets/figures/sec_warn_01.png
   :align: center
   :alt: Image of example security warning.

   Example security warning

.. figure:: /assets/figures/sec_warn_02.png
   :align: center
   :alt: Image of another example security warning.

   Another example security warning

In all cases, you can simply select *Enable Content* or *Accept/Trust* as necessary.

Re-link *CEDAR.accdb* and *CEDAR_forest.accdb*
++++++++++++++++++++++++++++++++++++++++++++++
The first time you open *CEDAR.accdb* (or an updated version of *CEDAR.accdb*), you must **re-link** the front-end and back-end databases. If you forget to re-link the databases, opening a database object like a query or form will result in an error message, similar to the one below:

.. figure:: /assets/figures/cedar_unlink_error.png
   :align: center
   :alt: Image of example error message if you forget to re-link the front-end and back-end of the database.

   An example of the error message recieved when opening a database object from an unlinked front-end.

To re-link the files:

#. Locate the *External Data* tab in the ribbon (the top, red menu bar), and select *Linked Table Manager*.
#. On the right-hand side of the *Linked Table Manager*, use *Select All* to select all tables.
#. On the right-hand side of the *Linked Table Manager*, select *Relink*, and navigate to *CEDAR_forest.accdb*.

In Access 365, an additional confirmation dialogue is presented:

.. figure:: /assets/figures/cedar_relink_name_confirm.png
   :align: center
   :alt: Image of Microsoft Access message asking if you would like to relink the selected tables with a different name.

   The name confirmation dialogue box is only displayed in the latest versions of Access.

Select **No**. If you select *Yes*, you will have to confirm each table name manually (by clicking accept through the subsequent dialogues).

.. tip:: Don't forget that you will need to re-link the database each time the front-end *CEDAR.accdb* is updated, or the files are moved.


Read CEDAR
----------
There are two primary ways to interact with CEDAR: to read reference-level information, and to read factor-level information. Both of these tasks are accomplished via forms, accessible via the Navigation Pane on the left-hand side of the window. 

To access reference-level information, use the *Add or Edit a Reference* form. To access factor-level information, use the *Add or Edit a Factor* form.

Navigating CEDAR
----------------

Most navigation in CEDAR is accomplished through the *Navigation Pane*, where you can select tables, queries, or forms, and the *Record Navigation Bar*, at the bottom of the screen:

.. figure:: /assets/figures/cedar_navigation.png
   :align: center
   :alt: Image showing CEDAR open to Add or Edit a Reference form with the Record Navigation Bar highlighted in red at the bottom of the screen.
   
   The Record Navigation Bar is highlighted in red at the bottom of the screen.

You can use the left and right arrows to navigate between records (generally between references), or the right arrow with yellow star to create a new record (generally a new reference). This bar also contains a search feature to quickly find records.