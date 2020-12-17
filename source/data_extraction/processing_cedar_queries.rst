

Processing CEDAR Exports
========================

Overview
--------
This section provides instructions for processing CEDAR exports (queries, timber), so that they can be used to populate the iAM.AMR models.

This processing is performed using the **sawmill** R package. 
If you are not familiar with sawmill, please review the :ref:`section on sawmill <data_extraction/Sawmill:The sawmill R Package>`, and install it as per the instructions on that page before continuing.

.. tip:: This section should be read concurrently with the last step of your chosen installation procedure (**Bootstrap** or **Standard**): please see the `Installation and Use <https://github.com/iAM-AMR/sawmill#installation-and-use>`_ section of the sawmill GitHub repository's *README* instruction file).

Raw Timber
----------

CEDAR timber should be in the form of an Excel (*.xlsx*) file, where each row represents an individual factor.

CEDAR v2 timber
~~~~~~~~~~~~~~~

The following table is an example of a properly formatted CEDAR v2 input timber file (header row and one example factor row are shown). 

.. csv-table:: CEDAR v2 Timber Example
   :file: CEDAR_v2_ex.csv
   :widths: 30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30
   :header-rows: 1

.. attention:: The left-to-right order and names of the fields in your input file must match that shown above *exactly*, otherwise sawmill will raise an error.

Each field has an expected data type, as dictated below. A description of each field is also provided.

.. csv-table:: CEDAR v2 Timber Specification
   :file: CEDAR_v2_spec.csv
   :widths: 30,10,50
   :header-rows: 1

.. attention:: The type of data contained within each of the fields in your input file should match those outlined above, as processing errors can occur otherwise. Please see :ref:`Warnings due to unexpected data types <data_extraction/processing_cedar_queries:Warnings due to unexpected data types>` for more information.

CEDAR v1 timber
~~~~~~~~~~~~~~~

The following table is an example of a properly formatted CEDAR v1 input timber file (header row and one example factor row are shown).

.. csv-table:: CEDAR v1 Timber Example
   :file: CEDAR_v1_ex.csv
   :widths: 30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30
   :header-rows: 1

.. attention:: The left-to-right order and names of the fields in your input file must match that shown above *exactly*, otherwise sawmill will raise an error.

Each field has an expected data type, as dictated below. A description of each field is also provided.

.. csv-table:: CEDAR v1 Timber Specification
   :file: CEDAR_v1_spec.csv
   :widths: 30,10,50
   :header-rows: 1

.. attention:: The type of data contained within each of the fields in your input file should match those outlined above, as processing errors can occur otherwise. Please see :ref:`Warnings due to unexpected data types <data_extraction/processing_cedar_queries:Warnings due to unexpected data types>` for more information.

Using sawmill
-------------

Changing default values of sawmill arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip:: This sub-section is optional if you have chosen the **Bootstrap** installation.

Complete descriptions of these arguments and guides as to how they should be changed can be found in the `Sawmill Arguments <https://github.com/iAM-AMR/sawmill#sawmill-arguments>`_ section of the sawmill GitHub repository's *README.md* file.

To change these arguments, open *start_mill.R* and *mill.R*.
The default values are specified in this script in a single line of code, as shown for *mill.R* in the following figure. 

.. figure:: /assets/figures/RStudio_default_arguments.jpg
   :align: center

   Default arguments in sawmill's *mill.R* script.

The argument values can be changed directly in this line of code. For example, if you wanted to change the argument **insensible_p_lo** to *98*, simply replace the *99* after the *=* sign with *98*.

.. attention:: You must click *Install and Restart* in the **Build** tab of RStudio for any changes to the code to take effect.

Running sawmill
~~~~~~~~~~~~~~~

Please see the instructions in the `Installation and Use <https://github.com/iAM-AMR/sawmill#installation-and-use>`_ section of the GitHub repository's *README.md* file.

Prompts will appear in the **Console** as you follow the instructions from GitHub. 
Enter the information requested by the prompts and select the input timber file from its saved location on your computer.

Once sawmill is finished running, it will prompt you to save one or more output files. 
For each one, you will be prompted to select the save location on your computer.

.. important:: Save all output files with *.csv* extensions to prevent errors from occurring.

If **errors** or **warnings** appear, please see the following sub-sections.

.. caution:: You will likely rerun sawmill many times, as deciding which factors to include in a model is an iterative process. You will need to enter the command `rm(list = ls())` into the **Console** before rerunning sawmill. This must be done once for every rerun. This way, variables saved during sawmill's previous run will not carry over to the new one.

Errors
~~~~~~

Errors will stop sawmill from continuing to run, at whichever point in the pipeline they are raised.

An error message will appear in the **Console**, indicating which function caused the error.
For example, if the error is raised in the *build_chairs* function, the message will look something like the following:

.. figure:: /assets/figures/Error_console.jpg
   :align: center

   Example error message.

Please note that only the lines beginning with "Error" constitute the actual error message. 
Although the "Processed function..." lines are also in red text, they should be present in the case of a normal output (i.e. one without errors or warnings).

.. important:: In the event of an error, please send the error message and input timber file that produced it to the maintainer of sawmill's GitHub repository.

Warnings
~~~~~~~~

Warnings alert the user to potential problems with the code or input data. 

Their presence can indicate that sawmill may run into an error at a later step in the processing pipeline, or simply that the current code or input data will produce an incorrect output **without further warning**. 
Others may mean nothing; sawmill may continue to execute flawlessly. 

Warnings do not stop the pipeline at the point they are raised, but they are still worth examining.

Warnings due to unexpected data types
+++++++++++++++++++++++++++++++++++++

If sawmill detects that one or more cells in the input timber file do not match the expected data types for their respective columns, a warning message will be generated for each mismatching cell.
The warning messages are informative; they specify the exact cell addresses within your input file that contain data of the unexpected type.

These particular warnings will also generate a prompt asking whether you would like to stop the pipeline and fix your input data, or continue with processing anyway. 

.. figure:: /assets/figures/Warning_prompt.jpg
   :align: center

   Warning prompt.

.. caution:: Electing to continue with processing when faced with this prompt can create unwanted/unexpected results, which **you may not receive further warning about**. 

The type of warning received (**Coercing** or **Expecting**) can help you decide whether or not you should continue.

Coercing warnings
^^^^^^^^^^^^^^^^^

Coercing warnings appear when R *is* able to convert the affected cell(s) to the appropriate, expected data type(s).

Below is an example of a cell that is likely to produce a coercing warning. This value is in the **odds_ratio_up** column, so its data type should be numeric.
While the value is a number, it is formatted as text (flagged by Excel in the upper left corner of the cell).

.. figure:: /assets/figures/Coercing_warning_Excel.jpg
   :align: center

   Example of a cell that produces a coercing warning.

Warning messages for coercing warnings appear in the **Console** and look something like that shown below.
The Excel cell shown above produced one of these warnings (the one affecting AE524 / R524C31).

.. figure:: /assets/figures/Coercing_warning_ex.jpg
   :align: center

   Coercing warning examples.

If only coercing warnings are present, you can safely choose to continue with processing when faced with the prompt.

Expecting warnings
^^^^^^^^^^^^^^^^^^

Expecting warnings appear when R is *not* able to convert the affected cell(s) to the appropriate, expected data type(s).

Below is an example of a cell that is likely to produce an expecting warning. This value is in the **prev_table_d** column, so its data type should be numeric.
However, a text string is present, and it cannot be converted to a numeric data type.

.. figure:: /assets/figures/Expecting_warning_Excel.jpg
   :align: center

   Example of a cell that produces an expecting warning.

Warning messages for expecting warnings appear in the **Console** and look something like that shown below.
The Excel cell shown above produced this warning; it affects cell Z2 / R2C26.

.. figure:: /assets/figures/Expecting_warning_ex.jpg
   :align: center

   Expecting warning example.

The implications of expecting warnings vary depending on the columns in which they occur.

If the affected cell(s) are in any of the columns specified in the table below, you should stop the pipeline and fix the affected cells. 
These fields have a direct effect on the odds ratio calculation, so in the event of unexpected data types in any of these, sawmill will 
typically deem the factor unusable, excluding the row from further processing and writing it to the :ref:`scrap pile <data_extraction/processing_cedar_queries:Scrap pile>` **without warning**.

.. csv-table:: Columns Which Affect Calculations
   :file: Calculation_Fields.csv
   :widths: 30,30
   :header-rows: 1

If the affected cell(s) are in any of the other columns, however, sawmill will simply replace the cell with a value of *NA*. 
The factor will not be deleted, and the row will still appear in the processed timber. 
In cases like this, it is up to the user whether or not to continue with processing when faced with the prompt.

.. attention:: Output fields may still be affected by unexpected data types in these other columns. For instance, the **url** and **html_link** output columns are affected by *ident_doi* (v2)/*docID* (v1), and sometimes *ident_pmid* (v2). Also, the **identifier** output column is affected by *ID_factor* (v2)/*ID* (v1) and *factor_title* (v2)/*title* (v1).

Other warnings
++++++++++++++

Every time you execute sawmill, you will likely see a message resembling the following in the **Console**, once the pipeline has finished and you have saved your processed timber.

.. figure:: /assets/figures/standard_warning.jpg
   :align: center

   Generic warnings alert.

If you follow the prompt by entering the following into the **Console**::
   
   warnings()

You will see something closely resembling the following:

.. figure:: /assets/figures/fisher_warning.jpg
   :align: center

   Generic warning messages.

This type of warning can be ignored. It occurs when the significance value (p-value) for the factor is calculated using the Fisher's exact test.
Since the values used in the Fisher's test must be rounded to the nearest integer, a warning is generated to notify the user that the rounding took place.

.. attention:: If the warning messages are of any other nature than those mentioned, please contact the maintainer of sawmill's GitHub repository for assistance.

Evaluating the Processed Timber (Planks) and Other Outputs
----------------------------------------------------------

This section outlines the fields that will be present in the processed timber *.csv* file. 
Each row now represents a plank of processed timber, or a factor usable for an iAM.AMR model.

An overview of additional output *.csv* files that may be produced is also provided.

The output .csv files
~~~~~~~~~~~~~~~~~~~~~

Processed timber
++++++++++++++++

A processed timber file is produced for each successful run of sawmill.

Two types of planks (rows) are present in the following order, from top to bottom:

#. *Error-free factors* for which an odds ratio and other outputs were successfully calculated
#. *Meta-analysis results* for each meta-analysis grouping (each unique meta-analysis ID)

.. note:: Rows containing the results of a meta-analysis will look slightly different (for instance, some fields may have values of *NA*).

Scrap pile
++++++++++

This file is only provided as an output if there is at least one erroneous factor in the raw timber.

The scrap pile contains all erroneous factors, or factors for which an odds ratio and other key outputs
were *not* successfully calculated.

Its fields are overall quite similar to those present in the raw timber, with two unique additions:

#. **exclude_sawmill**: Flagged as TRUE, indicating that the factor was excluded from calculations by sawmill due to errors/missing data
#. **exclude_sawmill_reason**: A more detailed description of why the factor was not usable

Full meta-analysis results
++++++++++++++++++++++++++

This file is only provided as an output if there is at least one meta-analysis grouping in the raw timber.

Each row represents the results from a single meta-analysis grouping, indicated by the value of **ID_meta** 
in the far-left column.

The main estimates produced by the meta-analysis calculation (odds ratio, standard error of the log(odds ratio), 
and p-value) are included in the processed timber. However, the full results
produced by *metafor* (the meta-analysis R package used by sawmill), contain many more fields describing other parameters of the calculation.

For a full description of these parameters, please see pg. 241 of the `metafor user guide <https://cran.r-project.org/web/packages/metafor/metafor.pdf>`_, which is the Value list for rma.uni.

CEDAR v2 planks
~~~~~~~~~~~~~~~

The following table is an example of processed timber from CEDAR v2.

While all fields present in the input timber are retained in the output, some will have new names. 
Sawmill renames some of the fields to improve uniformity between v1 and v2 outputs.

.. csv-table:: Output from CEDAR v2 Example
   :file: CEDAR_v2_output_ex.csv
   :widths: 30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30
   :header-rows: 1

A description of each output field is provided below. The fields which are added by sawmill and thus only appear in the processed timber are also annotated with the function responsible for adding them.

.. tip:: The **odds_ratio**, **se_log_or**, and **pval** fields are added by the *do_MA* function in cases where the row contains the results of a meta-analysis.

.. tip:: The **logOR** field is only added if there is at least one meta-analysis grouping (one unique meta-analysis ID) in the raw timber.

.. csv-table:: Output from CEDAR v2 Specification
   :file: CEDAR_v2_output_spec.csv
   :widths: 30,10,50
   :header-rows: 1

CEDAR v1 planks
~~~~~~~~~~~~~~~

The following table is an example of processed timber from CEDAR v1.

While all fields present in the input timber are retained in the output, some will have new names. 
Sawmill renames some of the fields to improve uniformity between v1 and v2 outputs.

Please note that rows containing the results of a meta-analysis will look slightly different (for instance, some fields may have values of *NA*).

.. csv-table:: Output from CEDAR v1 Example
   :file: CEDAR_v1_output_ex.csv
   :widths: 30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30
   :header-rows: 1

A description of each output field is provided below. The fields which are added by sawmill and thus only appear in the processed timber are also annotated with the function responsible for adding them.

.. csv-table:: Output from CEDAR v1 Specification
   :file: CEDAR_v1_output_spec.csv
   :widths: 30,10,50
   :header-rows: 1

Adding meta-analysis groupings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upon examining the processed timber, you may wish to group certain factors together for meta-analysis in the raw timber and rerun sawmill.

.. attention:: Meta-analysis is currently only supported for timber from CEDAR v2.

To add a meta-analysis grouping, make the following changes to the optional meta-analysis fields in the original, raw timber file:

#. **ID_meta**: assign the same meta-analysis ID to all factors you wish to include in the grouping
#. **meta_amr**: specify the antimicrobial or class of antimicrobials to which resistance is assayed
#. **meta_type**: describe the type and level of granularity of the meta-analysis grouping

.. tip:: The actual meta-analysis ID assigned to a particular grouping is irrelevant, as long as it is consistent across all factors in the grouping.

The table below provides example values for each meta-analysis field, as they might appear for a factor in the raw timber.

.. csv-table:: Meta-analysis Example
   :file: Meta-analysis_example.csv
   :widths: 50,50,50
   :header-rows: 1

All three meta-analysis fields (**ID_meta**, **meta_amr**, and **meta_type**) can simply be left blank for factors that should not be involved in meta-analysis calculations.

Checking the validation fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are present in the processed timber file.

Low cell count factors
++++++++++++++++++++++

When one or more of the four values in the 2x2 contingency table is equal to zero, sawmill sets the **low_cell_count** field to True.
To avoid divide by zero errors, sawmill increments all four values by 0.5.

Null comparison factors
+++++++++++++++++++++++

When the # AMR+ observations in both the exposed and referent groups are equal to zero, sawmill sets the **null_comparison** field to True.
To avoid divide by zero errors, sawmill increments all four values by 0.5.

Any null comparison factors also have the **low_cell_count** field set to True.

CEDAR v2: factors with an insensible_prev_table
+++++++++++++++++++++++++++++++++++++++++++++++

Check your output *.csv* file for rows where the **insensible_prev_table** field is set to True.
These rows likely have data entry errors in the prevalence table columns, as this result indicates that (% AMR+ exposed) **+** (% AMR- exposed) does not come to approximately 100, and/or that (% AMR+ referent) **+** (% AMR- referent) does not come to approximately 100.