

============================
Getting Started in Analytica
============================

What is Analytica?
------------------
`Analytica <https://lumina.com/>`_ (by Lumina Decision Systems [hereby ‘Lumina’]) is a popular decision modelling tool for creating probabilistic risk assessment models. While Analytica is similar in many ways to a spreadsheet-based modelling tool, it adds two key differentiating features: a flexible and informative user interface, and an ‘intelligent array’ system. 

The former makes large, complex models easier to understand for end-users and modellers; the latter allows modellers to dynamically resize the model as new information becomes available. Both of these features are desirable for a large-scale model.


Analytica Editions and Versions
-------------------------------
Analytica is available in several *editions*, and is currently (as of Dec 2020) on *version* 5.4.x.


Editions
~~~~~~~~
Analytica is available in three editions: Analytica Professional, Analytica Enterprise, and Analytica Free 101. The latter is -- as the name implies -- free! `Lumina <https://lumina.com/products/analytica-editions/>`_ provides a description of the various `editions <https://lumina.com/products/analytica-editions/>`_, and provides a useful `comparison of Analytica editions <https://lumina.com/products/compare-analytica-editions/>`_.

**Analytica Professional** is the standard, fully featured edition of Analytica, which allows users to build models of any size, and address arrays with a maximum length of 32,000 elements.

**Analytica Enterprise** offers all the functionality of Analytica Professional, while increasing the maximum array length to 100 million elements, adding encryption, and adding the ability to use a performance profiler to identify computationally expensive model elements.

**Analytica Free 101** offers the same functionality as Analytica Professional, but limits users to the creation and modification of smaller models, containing no more than 101 nodes. Users can still open and evaluate larger models, but cannot make changes to variables or the underlying model structure. 

.. tip:: You can open and run the iAM.AMR models with Analytica Free 101, but you will not be able to edit them.

All editions can be installed using the same installer, available from `Lumina's download page <http://www.lumina.com/support/downloads/>`_.

We provide more details on *editions* in the iAM.AMR Tech Tutorial - see the `iAM.AMR Team Repo <https://goto.iam.amr.pub/repo-team>`_ for more details (*login required*).


Editions and the iAM.AMR project
++++++++++++++++++++++++++++++++
In short, we avoid using features from the Enterprise edition (not available in Professional) to reduce software cost. The only Enterprise feature relevant to the iAM.AMR models are the large arrays - we have worked around this issue with some clever coding.

We recommend Professional, unless users are involved in framework development. 


Versions
~~~~~~~~
Analytica is currently on version 5.4.x. For GoC employees, Shared Services has packaged version 5.1.x.


Versions and the iAM.AMR project
++++++++++++++++++++++++++++++++
We identify three important milestones; 4.2, 4.6, and 5.0. 

The changes introduced in versions 4.2 (encryption) and 4.6 (OLE links) are no longer relevant to the iAM.AMR models. Versions 5.0+ enable `multi-threaded computation <http://wiki.analytica.com/Multithreaded_evaluation>`_, and may speed up model evaluation.

We recommend using version 4.7+.


Install Analytica
--------------------
Analytica is packaged for GoC computers, however (as always) Shared Services is several versions behind. We can side-load Analytica using the same "extract-and-run" procedure described here.


Learn Analytica
---------------
Lumina has provided a number of great first-party resources for getting started with Analytica, including the Analytica User Guide, and a series of Analytica tutorials. These, in addition to the `Analytica Wiki <https://wiki.analytica.com/index.php?title=Analytica_Wiki>`_, are accessible from the help menu within Analytica. For a general introduction to Analytica, we recommend you get started by reading the `User Guide <https://wiki.analytica.com/index.php?title=Analytica_User_Guide>`_, which is available as a PDF in Analytica’s help menu, or on the Wiki.

.. tip:: If you’re not a fan of manuals, Lumina has distilled the User Guide into a few key chapters listed `here <https://wiki.analytica.com/index.php?title=If_you_don%E2%80%99t_read_manuals>`_.

There are additional training resources in the `iAM.AMR Team Repo <https://goto.iam.amr.pub/repo-team>`_ (*login required*).
