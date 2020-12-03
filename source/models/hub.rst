

===========
iAM.AMR.HUB
===========


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
