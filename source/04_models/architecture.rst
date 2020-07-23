

==========================
iAM.AMR Model Architecture
==========================

Large Models in Analytica
-------------------------

About Modules
~~~~~~~~~~~~~

Models get big fast. 

This is particularly true of Analytica models, wherein data and model process are coupled to their layouts (recall, Lumina refers to this concept as an *Influence Diagram*). Accordingly, the Analytica wiki includes a section explicitly addressing `working with large models <https://wiki.lumina.com/index.php?title=Working_with_Large_Models>`_. 

In brief, Analytica models can be broken down into smaller parts, called *modules*. These modules fit together like puzzle pieces -- each contains its own nodes and connections that together, form a whole. 

Within a model, modules are organized hierarchically, like folders on your desktop. You may have many modules in the root of your model, or choose to add modules within other modules. Or, if you prefer, you may just have one large model with no modules at all (but will be doing a lot of scrolling!). A module looks like a standard node, but you'll be able to identify them by their thicker boarders.


Types of Modules
~~~~~~~~~~~~~~~~

Standard Modules
++++++++++++++++

Standard modules (or simply, *modules*) exist within the parent model file as a logical sub-dividion of your model. For example, you may add a user-interface at the root level of your model, and hide the actual model from view within a module (like we do in the iAM.AMR models). Or, you may put all nodes related to a particular antimicrobial class within a single class module.

.. hint:: 'Enter the model' on the front page of each model is actually a module! We use modules throughout the iAM.AMR models to better organize information and improve user experience.


Filed Modules
+++++++++++++

*Filed modules* exist within a seperate file (i.e. a seperate .ANA file), linked remotely to your parent model file. For example, you may have different filed modules for each animal species (that can be updated by a different subject-matter expert), that are all linked together in a single parent model. 

Filed modules offer several important advantages, including re-use across multiple models, and improved collaboration (as everyone can work on their own section). However, it is important to note that you must have all of the files present to run the parent model. 

Returning to our above example, if you have a parent model "agri-food production", linked to seperate chicken, cattle, and swine filed modules, you must have all four to run the complete model. And, they must be stored/distributed in the same relative location (see below).


Linking Modules in Analytica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a complete explanation of how to link filed modules to parent models in Analytica, see the `Analytica Wiki <https://wiki.lumina.com/index.php?title=Import_a_module_or_library>`_.

Some Important Points
+++++++++++++++++++++

- Changes in a linked module (i.e. a filed module) are propegated in **both directions**. Do not make an edit within the module in your model that you do not want to propegate to all models linked to that module.  
- Generally, you do not want to *embed* a module, as that breaks the link to the original module file, and no updates or changes will be propegated in either direction.
- For existing links, you will have to re-link the modules if the files have been moved relative to one another. For example, when you download the files from GitHub, you will have to re-link the module when open. 



Connecting iAM.AMR Models
-------------------------

We take full advantage of modules in Analytica, and use throughout the iAM.AMR models.

The Hub Module
~~~~~~~~~~~~~~

Recall that the iAM.AMR models are organized into *stories*, or collections of one or more drug-microbe-commodity combinations that together describe an important facet of resistance in the agri-food production system in Canada.

While the factors included in each model vary widely, there are several parameters common to all models, including: the baseline probability of resistance, the human population size, and rates of commodity consumption.

To ensure these parameters are implemented and updated uniformly across all models, they are included in a separate filed module -- iAM.AMR.HUB -- that runs alongside each of the iAM.AMR story models.

The Hub module is so named because of this hub-and-spoke design -- each 'spoke' model conencts back to the central Hub module, like spokes on a wheel.

HUB vs. HUB.GM
++++++++++++++

To ensure end-users do not accidently overwrite or change values in the Hub module(and subsequently propagate these changes to all story models), we maintain two different copies of the Hub module: the Gold Master [GM] (iAM.AMR.HUB.GM) and the production copy (iAM.AMR.HUB).

The Gold Master (a term borrowed from audio and software engineering) is  -- as the name suggests -- the master copy of the Hub module. The GM is where all development (additions, deletions, changes) occurs. The production module is a *protected and encrypted* copy of the mutable (editable) GM module. 

.. important:: The iAM.AMR.HUB module is the module to which the story models are linked. Do not link your story model to the iAM.AMR.HUB.GM module.

What does this mean in practice? To make changes to our Hub module, we first make the changes to the GM. Then, we save a protected copy, overwriting the existing production model. Because the name and location of the Hub module do not change, the story models automatically recognize the new production copy, and any changes are propagated when the story models are opened.

You can think of making changes to the Hub module like making changes to a manuscript. All changes are made in Microsoft Word, before creating a PDF to submit to the journal.


The Basic Hub Workflow
++++++++++++++++++++++

There are several steps to edit the Hub:

 #. Download/pull the latest version of the models from GitHub
 #. Edit the Gold Master Hub module [iAM.AMR.HUB.GM] and story models as required  
 #. Save the Gold Master Hub module  
 #. Save an additional copy of the Gold Master as a protected model, with the name 'iAM.AMR.HUB', overwriting the existing Hub module  
 #. Review the story models to ensure no bugs were introduced during editing  
 #. Upload/push the changes to the GitHub repository  


Save a Protected Model
^^^^^^^^^^^^^^^^^^^^^^

Creating a protected version of an Analytica model/module is simple, but **requires Analytica Enterprise**.

While in edit mode, navigate to `File > Save a Copy In...`. When prompted for a save location and file name, select *Save as a Browse-Only Model* in the lower left corner.

.. figure:: /assets/figures/hubModel_save.png
   :align: center

   The *Save a Copy In...* Dialogue

Selecting *Save as a Browse-Only Model* will automatically select *Lock and Encrypt the Copy*. Ensure you are saving a copy of the Gold Master without overwriting the Gold Master itself.

.. danger:: Analytica will let you shoot yourself in the foot. Do not overwrite the GM with a protected production copy.


Other Modules
~~~~~~~~~~~~~

Generally, any data which are applicable for multiple -- but not all -- story models are stored in a module, and are saved as *iAM.AMR.MOD_contents_here*.