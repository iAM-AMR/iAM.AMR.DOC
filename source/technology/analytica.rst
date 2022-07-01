

=========
Analytica
=========

About Analytica 
---------------
According to `Lumina Decision Systems (Lumina) <https://lumina.com/>`_:

     "Analytica is a visual software environment for building, exploring, and sharing quantitative decision models. If you find yourself struggling with complex spreadsheets, you will find Analytica a revelation."

Analytica builds on spreadsheets by introducing *Influence Diagrams* (the "visual" element referenced above) and *Intelligent Arrays*. Intelligent arrays simplify coding, and make it considerably easier to dynamically expand the scope of the model (e.g., to include a different animal or microbe) and perform scenario analyses. 


Editions and Versions
---------------------
Analytica is available in three editions: `Analytica Free <https://lumina.com/products/free101/>`_, Analytica Professional, and Analytica Enterprise (`compare the editions <https://lumina.com/products/compare-analytica-editions/>`_). 

.. tip:: `Analytica Free <https://lumina.com/products/free101/>`_ allows you to create and edit models with up to 101 nodes.

Analytica regularly releases updated versions. As of July 01, 2022: the current version of Analytica is |anavcur|, 


iAM.AMR Minimum Requirements
----------------------------
To **open and run** the iAM.AMR models, you will need Analytica |anavsup| Free (or greater). To **create, edit, and run** the iAM.AMR models, you will need Analytica |anavsup| Professional (or greater).

Why?

- the iAM.AMR models generally have more than 101 nodes.
- we avoid the use of features supported only in the Enterprise edition (e.g., large arrarys). 
- we use encryption in the Hub module (v4.2+).
- we use *local* (replacing *var*) for local variables (v5.0+).

.. tip:: Analytica v5.0 also introduced `multi-threaded computation <http://wiki.analytica.com/Multithreaded_evaluation>`_.


Install Analytica
-----------------
All editions of Analytica are installed using `the same installer <https://lumina.com/support-2/analytica-downloads/>`_. If the installation fails (e.g., due to lack of administrative rights), you can install Analytica using the :doc:`"extract-and-run" procedure </technology/software>`.


Learn and Troubleshoot Analytica
--------------------------------
There are two first-party resources for learning and troubleshooting: the `Analytica User Guide <https://wiki.analytica.com/index.php?title=Analytica_User_Guide>`_, and the `Analytica Wiki <https://wiki.analytica.com/index.php?title=Analytica_Wiki>`_. Both are accessible from the help menu within Analytica. 

There are also resources specific to the iAM.AMR project, including recordings of past meetings, in the `iAM.AMR Team Repo <https://goto.iam.amr.pub/repo-team>`_ (*login required*).

.. tip:: `If you don't read manuals (or need to get started quickly) <https://wiki.analytica.com/index.php?title=If_you_don%E2%80%99t_read_manuals>`_.


Tips and tricks
---------------

Text size
~~~~~~~~~
To increase text size, navigate to the *Edit* > *Preferences* dialog, and ensure "Large text in attributes & tables" is selected.

To further increase text size, press F12 to open the `Typescript <https://wiki.analytica.com/index.php?title=Typescript>`_ window. Then, type the command: **AttributeFontSize:15**, where 15 is desired font size. For reference, the "Large text" size is 13pt.


Search Shortcuts
~~~~~~~~~~~~~~~~
You can use *search shortcuts* to trigger a custom search from your browser's address bar (e.g., only returning results from the Analytica wiki). 

To use a search shortcut, type the shortcut's name (i.e., keyword) and the search terms into the address bar (e.g., if the shortcut is "ANA" use: ``ANA search terms``). 

.. tip:: These instructions are for Firefox, but similar instructions apply for Google Chrome.

Shortcut to Search using Wiki
+++++++++++++++++++++++++++++
To create a shortcut that uses the Analytica Wiki search box, navigate to the `Analytica Wiki <https://wiki.analytica.com/index.php?title=Analytica_Wiki>`_, right-click in the search bar, and select "*Add keyword for this search*".  

Shortcut to Search using Google
+++++++++++++++++++++++++++++++
To create a shortcut that uses Google to search the Analytica Wiki, right-click in the bookmarks bar, and select *Create a bookmark*. Then, set the location to ``https://www.google.com/search?q=site%3Aanalytica.com+%s``.

