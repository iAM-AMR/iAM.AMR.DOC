

Software and services
=====================
The IAM.AMR project relies heavily on free and open-source software. The authors would like to thank the developers that made these projects possible, and recognize the companies which provide paid or closed-source software and services at a discount for academic users.

For more information on free and/or open-source projects, see the `Open Source Initiative <https://opensource.org/>`_ and the `Free Software Foundation <https://www.fsf.org/>`_.

List of software and services
-----------------------------
`Analytica <http://www.lumina.com/>`_
   "Analytica is a visual software package developed by Lumina Decision Systems for creating, analyzing and communicating quantitative decision models."

`Git <https://git-scm.com/>`_
   "Git is a distributed version-control system for tracking changes in source code during software development."

`GitHub <https://github.com/>`_
   "GitHub Inc. is a web-based hosting service for version control using Git."

`Kumu <https://kumu.io/>`_
   "Kumu is a powerful data visualizatiuon platform that helps you organize complex information into interactive relationship maps."

`Let's Encrypt <https://letsencrypt.org/>`_
   "Let's Encrypt is a free, automated, and open certificate authority."

`Mendeley <https://www.mendeley.com/>`_
   "Mendeley is a desktop and web program produced by Elsevier for managing and sharing research papers, discovering research data and collaborating online."

`R <https://www.r-project.org/>`_
   "R is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing. The R language is widely used among statisticians and data miners for developing statistical software and data analysis."

`RStudio <https://www.rstudio.com/>`_
   "RStudio is a free and open-source integrated development environment for R, a programming language for statistical computing and graphics."

`Read the Docs <https://readthedocs.org/>`_
   "Read the Docs is a software documentation hosting platform."

`Sphinx <http://www.sphinx-doc.org/en/master/>`_
   "Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license."

Management of shared software and services
------------------------------------------
Collaborative software and online services are usually managed by one or more persons.

GitHub
~~~~~~
* The IAM.AMR models are housed in a private repository owned by Brennan Chapman (chapb). Availability of a private repository with more than three collaborators is made possible by GitHub’s academic offerings. 
* The documentation is housed in a public repository owned by Brennan Chapman (chapb).

Kumu
~~~~
* The AMR Org Chart is managed by Brennan Chapman (chapmanb). Availability of private projects is made possible by Kumu's academic offerings.

Read the Docs
~~~~~~~~~~~~~
* The documentation is hosted by Read the Docs and is managed by Brennan Chapman (chapb).

Domain Name
~~~~~~~~~~~
* The grdi-amr.com domain is managed -- and has been graciously donated by -- Brennan Chapman.

.. _extract and run:

Install software using "extract-and-run"
----------------------------------------
Sometimes, installation of software may fail (e.g., due to lack of administrative rights). As an alternative to using the installer, many programs can be run "portably" via "extract-and-run".

"Extract-and-run" involves the use of an unarchiver (e.g., 7-Zip) to extract the program files from the installer to a location of your choice. The program is not installed in the traditional sense (it won;t appear in your start menu), but a shortcut can be created on your desktop directly to the program's .exe.

The following instructions use the ``C:/myprograms`` directory, but you can use any local writiable directory (e.g., ``C:/Users/My Username/My Desktop``). 

.. warning:: The Government of Canada's *Acceptable Use Policy* states that the installation of unapproved software on a government device is prohibited. Proceed at your own risk.



Mendeley
~~~~~~~~
1. Download the latest version of `Mendeley here <https://www.mendeley.com/download-desktop/>`_.
2. Right-click on the installer and select '7-Zip > Extract to "Mendeley-Desktop-###-win32"'. This will create a new folder in your current directory.
3. Navigate to the root of your C:/ drive, and if it doesn't already exist, create a new folder called 'myprograms'.
4. Move the folder you created in step 2 into the myprograms folder.
5. Navigate to the folder (within C:/myprograms/), and locate the 'MendeleyDesktop.exe' executable. Right-click on MendeleyDesktop.exe and select 'Send to > Desktop' to create a shortcut.
6. Launch Mendeley from your newly created shortcut.

R and R Studio
~~~~~~~~~~~~~~

Install R
+++++++++
1. Download the latest version of R from the University of Toronto `here <https://utstat.toronto.edu/cran/bin/windows/base/release.html>`_.
2. Navigate to the root of your C:/ drive, and if it doesn't already exist, create a new folder called 'myprograms'.
3. Run the installer and select your preferred language.
4. When prompted, click ‘Next’ to acknowledge the warning about administrator privileges, and ‘Next’ to accept the licensing agreement.
5. Now, select a destination location by using ‘Browse’. Navigate to and select the ‘myprograms’ folder, in the root of your C:/ directory. The installer will automatically append a folder name to this path, according to the R version number. Click 'Next'.
6. Click 'Next' on all subsequent screens to accept the default installation options, and complete the installation.

Install RStudio
+++++++++++++++
1. Download the latest zipped version of RStudio from the `downloads page <https://www.rstudio.com/products/rstudio/download/>`_.

.. tip:: Ensure you download the Windows Vista/7/8/10 zip file, not the .exe installer. These are located under the **Zip/Tarball** heading.

2. Right-click on the zip file and select 'Extract All'. This will create a new folder in your current directory.
3. Navigate to the root of your C:/ drive, and if it doesn't already exist, create a new folder called 'myprograms'.
4. Move the folder you created in step 2 into the myprograms folder.
5. Navigate to the folder (within C:/myprograms/), and locate the 'rstudio.exe' exexutable within the 'bin' folder. Right-click 'rstudio.exe', and select 'Send to > Desktop' to create a shortcut.
6. Launch RStudio from your newly created shortcut.

Select a R Installation (optional)
++++++++++++++++++++++++++++++++++
Where multiple versions of R are available, or where the installation has not successfully been added to the registry, it may be necessary to select the appropriate (usually the latest) version of R. 

.. figure:: /assets/figures/rstudiolocate.png
   :align: center
   :alt: Image showing selection options of R versions to choose from.
   
   The RStudio R installation selection window.

If you are prompted during RStudio’s installation, choose the most appropriate version of R from the ‘Choose a specific version of R’ dropdown. If there are none listed, use ‘Browse…’ to navigate to the ‘bin’ sub-directory of your installation, and select ‘R.exe’.

If you have multiple versions of R installed and you would like to choose a different version after RStudio has been installed, you can make the selection from Tools > Global Options. 


.. Other Software commented out
.. ~~~~~~~~~~~~~~
.. For software such as :ref:`Analytica <technology/analytica:Analytica>` and :ref:`GitHub Desktop <technology/git:Git et al.>`, refer to their respective main pages (coming soon!).


Zotero
------

Fix Zotero plugin missing from Microsoft Word ribbon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Zotero ribbon will not appear by default on GoC PCs, because of the `software\policies\microsoft\office\14.0\common\toolbars\word\noextensibilitycustomizationfromdocument` GPO. To replace the toolbar manually, follow the steps in Word below:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/WUxZXAJ0dZU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



1. Left click on the File tab.  
2. Left click on Options.  
3. Left click on "Customize Ribbon"  
4. Right click on "References"  
5. Left click on "Add New Group"  
6. Right click on "New Group (Custom)"  
7. Left click on "Rename", and rename the group "Zotero"  
8. Left click on "Choose commands from:"  
9. Left click on "Macros"  
10. Left click on "Project.Zotero.ZoteroAddNote" (the first item in the list)  
11. Double left click on "Add" button repeatedly, until all Zotero macros are in the new Zotero group  
12. Left click on "OK (Button)"  
13. 