

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
Always access CEDAR by opening the front-end file *CEDAR.accdb*.

Upon opening *CEDAR.accdb*, you will be presented with with a mostly blank screen:

.. figure:: /assets/figures/cedar_launch.png
   :align: center

   The launch screen of *CEDAR.accdb*.



