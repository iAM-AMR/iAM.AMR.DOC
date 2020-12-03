

==================
Models and Modules
==================


About Modules
~~~~~~~~~~~~~

Models get big fast. 

This is particularly true of Analytica models, wherein data and model process are coupled to their layouts (recall, Lumina refers to this concept as an *Influence Diagram*). Accordingly, the Analytica wiki includes a section explicitly addressing `working with large models <https://wiki.lumina.com/index.php?title=Working_with_Large_Models>`_. 

In brief, Analytica models can be broken down into smaller parts, called *modules*. These modules fit together like puzzle pieces -- each contains its own nodes and connections that together, form a whole. A given module can be shared among multiple models.

Within a model, modules are organized hierarchically, like folders on your desktop. You may have many modules in the root of your model, or choose to add modules within other modules. Or, if you prefer, you may just have one large model with no modules at all (but will be doing a lot of scrolling!). A module looks like a standard node, but you'll be able to identify them by their thick black borders.


Types of Modules
~~~~~~~~~~~~~~~~

Standard Modules
++++++++++++++++

Standard modules (or simply, *modules*) exist within the parent model file as a logical sub-dividion of your model. For example, you may add a user-interface at the root level of your model, and hide the actual model from view within a module (we do this in the iAM.AMR models). Or, you might put all nodes related to a particular antimicrobial class within a single class module.

.. hint:: 'Enter the model' on the front page of each model is actually a module! We use modules throughout the iAM.AMR models to better organize information and improve user experience.


Filed Modules
+++++++++++++

*Filed modules* exist within a seperate file (i.e. a seperate .ANA file), linked remotely to your parent model file. For example, you may have different filed modules for each animal species (that can be updated by a different subject-matter expert), that are all linked together in a single parent model. 

Filed modules offer several important advantages, including re-use across multiple models, and improved collaboration (as everyone can work on their own section). However, it is important to note that you must have all of the files present to run the parent model. 

Returning to our above example, if you have a parent model "agri-food production", linked to seperate chicken, cattle, and swine filed modules, you must have all four to run the complete model. And, they must be stored/distributed in the same relative location (see below).


Linking Modules in Analytica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a complete explanation of how to link filed modules to parent models in Analytica, see the `Analytica Wiki <https://wiki.lumina.com/index.php?title=Import_a_module_or_library>`_. For a practical example, see the iAM.AMR.HUB section.

Some Important Points
+++++++++++++++++++++

- Changes in a linked module (i.e. a filed module) are propegated in **both directions**. Do not make an edit within the module in your model that you do not want to propegate to all models linked to that module.  
- Generally, you do not want to *embed* a module, as that breaks the link to the original module file, and no updates or changes will be propegated in either direction.
- For existing links, you will have to re-link the modules if the files have been moved relative to one another. For example, when you download the files from GitHub, you will have to re-link the module when open. 


