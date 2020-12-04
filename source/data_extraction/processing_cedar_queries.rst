

Processing CEDAR Exports
========================

Overview
--------
This section provides instructions for processing CEDAR exports (queries, timber), for inclusion in the iAM.AMR models.

This processing is done using the **sawmill** R package. 
If you are not familiar with sawmill, please review the :ref:`section on sawmill <02_project/Sawmill:The sawmill R Package>`.

.. tip:: This section should be read concurrently with step 3 of the *Bootstrap* installation or step 4 of the *Standard* installation (see the *Installation and Use* section of the sawmill GitHub repository's *README.MD* file).

Preparing the Input File
------------------------

CEDAR timber should be in the form of an Excel file, where each row represents an individual factor.

.. tip:: If you are not sure which fields within CEDAR correspond to those specified in the following sections, please consult Charly Phillips or Brennan Chapman.

CEDAR v2 input
~~~~~~~~~~~~~~

The following table is an example of a properly formatted CEDAR v2 input timber file (header row and one example factor row are shown). 

.. csv-table:: CEDAR v2 Timber Example
   :file: CEDAR_v2_ex.csv
   :widths: 30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30
   :header-rows: 1

.. attention:: The left-to-right order and names of the fields in your input file must match that shown above *exactly*, otherwise sawmill will raise an error.

Each field has an expected data type, as dictated below. A description of each field is also provided.

.. csv-table:: CEDAR v2 Timber Specification
   :file: CEDAR_v2_spec.csv
   :widths: 30,10,50
   :header-rows: 1

.. attention:: The type of data contained within each of the fields in your input file should match those outlined above, as processing errors can occur otherwise. Please see :ref:`Warnings due to unexpected data types <03_activities/processing_cedar_queries:Warnings due to unexpected data types>` for more information.

CEDAR v1 input
~~~~~~~~~~~~~~

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

.. attention:: The type of data contained within each of the fields in your input file should match those outlined above, as processing errors can occur otherwise. Please see :ref:`Warnings due to unexpected data types <03_activities/processing_cedar_queries:Warnings due to unexpected data types>` for more information.

Using sawmill
-------------

Changing default values of sawmill arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip:: This sub-section is optional if you have chosen the *Bootstrap* installation.

Complete descriptions of these arguments and guides as to how they should be changed can be found in the *Sawmill Arguments* section of the sawmill GitHub repository's *README.md* file.

To change these arguments, open **mill.R**.
The default values are specified in this script in a single line of code, as shown in the following figure. 

.. figure:: /assets/figures/RStudio_default_arguments.jpg
   :align: center

   Default arguments in sawmill's **mill.R** script.

The argument values can be changed directly in this line of code. For example, if you wanted to change the argument **write_scrap** to *FALSE*, simply replace the *TRUE* after the *=* sign with *FALSE*.

.. attention:: You must click *Install and Restart* in the *Build* tab of RStudio for any changes to the code to take effect.

Running sawmill
~~~~~~~~~~~~~~~

Please see the instructions in the *Installation and Use* section of the GitHub repository's *README.md* file.

Prompts will appear in the *Console* as you follow the instructions from GitHub. 
Enter the information requested by the prompts and select the input timber file from its saved location on your computer.

Once sawmill is finished running, it will prompt you to save the processed output. Select an appropriate location on your computer to do so.

.. important:: Save the processed output with a *.csv* extension to prevent errors from occurring.

If **errors** or **warnings** appear, please see the following sub-sections.

Errors
~~~~~~

Errors will stop sawmill from continuing to run, at whichever point in the pipeline they are raised.

An error message will appear in the *Console*, indicating which function caused the error.
For example, if an error occurs due to an error in the **build_chairs** function, the message will look something like the following:

.. figure:: /assets/figures/Error_console.jpg
   :align: center

   Example error message.

Please note that only the lines beginning with "Error" constitute the actual error message. 
Although the "Processed function..." lines are also in red text, they should be present in the case of a normal output (i.e. one without errors or warnings).

.. important:: In the event of an error, please send the error message and input timber file that produced it to Charly Phillips or Brennan Chapman.

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

Coercing warnings appear when R is able to convert the affected cell(s) to the appropriate, expected data type(s).

Below is an example of a cell that is likely to produce a coercing warning. This value is in the **odds_ratio_up** column, so its data type should be numeric.
While the value is a number, it is formatted as text (flagged by Excel with a green half-triangle in the upper left corner of the cell).

.. figure:: /assets/figures/Coercing_warning_Excel.jpg
   :align: center

   Example of a cell that produces a coercing warning.

Warning messages for coercing warnings look something like that shown below.
The Excel cell shown above produced one of these warnings (the one affecting AE524 / R524C31).

.. figure:: /assets/figures/Coercing_warning_ex.jpg
   :align: center

   Coercing warning examples.

If only coercing warnings are present, you can safely choose to continue with processing when faced with the prompt.

Expecting warnings
^^^^^^^^^^^^^^^^^^

Expecting warnings appear when R is unable to convert the affected cell(s) to the appropriate, expected data type(s).

Below is an example of a cell that is likely to produce an expecting warning. This value is in the **rate_table_d** column, so its data type should be numeric.
However, a text string is present, and it cannot be converted to a numeric data type.

.. figure:: /assets/figures/Expecting_warning_Excel.jpg
   :align: center

   Example of a cell that produces an expecting warning.

Warning messages for expecting warnings look something like that shown below.
The Excel cell shown above produced this warning; it affects cell Z2 / R2C6.

.. figure:: /assets/figures/Expecting_warning_ex.jpg
   :align: center

   Expecting warning example.

The implications of expecting warnings vary depending on the columns in which they occur.

If the affected cell(s) are in any of the columns specified in the table below, you should stop the pipeline and fix the affected cells. 
These fields have a direct effect on the odds ratio calculation, so in the event of unexpected data types in any of these, sawmill will typically deem the factor unusable, excluding the row from further processing, removing it from the processed output, and writing it to the *scrap_pile* **without warning**.

.. note:: For more information about the *scrap_pile* please see **write_scrap**, under the *Sawmill Arguments* section of the GitHub repository's *README.md* file.

.. csv-table:: Columns Which Affect Calculations
   :file: Calculation_Fields.csv
   :widths: 30,30
   :header-rows: 1

If the affected cell(s) are in any of the other columns, however, sawmill will simply replace the cell with a value of **NA**. 
The factor will not be deleted, and the row will still appear in the processed output. 
In cases like this, it is up to the user whether or not to continue with processing when faced with the prompt.

.. attention:: Output fields may still be affected by unexpected data types in these other columns. For instance, the **url** and **html_link** output columns are affected by *ident_doi* (v2)/*docID* (v1), and sometimes *ident_pmid* (v2). Also, the **identifier** output column is affected by *ID_factor* (v2)/*ID* (v1) and *factor_title* (v2)/*title* (v1).

Other warnings
++++++++++++++

Every time you execute sawmill, you will likely see a message resembling the following in the *Console*, once the pipeline has finished and you have saved your processed output.

.. figure:: /assets/figures/standard_warning.jpg
   :align: center

   Generic warnings alert.

If you follow the prompt by entering the following into the *Console*::
   
   warnings()

You will see something closely resembling the following:

.. figure:: /assets/figures/fisher_warning.jpg
   :align: center

   Generic warning messages.

This type of warning can be ignored. It occurs when the significance value (p-value) for the odds ratio is calculated using the Fisher's exact test.
Since the values used in the Fisher's test must be rounded to the nearest integer, a warning is generated to notify the user that the rounding took place.

.. attention:: If the warning messages are of any other nature than those mentioned, please contact Charly Phillips or Brennan Chapman for assistance.

Interpreting the Output File
----------------------------

This section outlines the fields that will be present in the processed output (*.csv*) file. 

Output from CEDAR v2
~~~~~~~~~~~~~~~~~~~~

The following table is an example of processed timber from CEDAR v2.

While all fields present in the input timber are retained in the output, some will have new names. 
Sawmill renames some of the fields to improve uniformity between v1 and v2 outputs.

Please note that rows containing the results of a meta-analysis will look slightly different (for instance, some fields may have values of **NA**).

.. csv-table:: Output from CEDAR v2 Example
   :file: CEDAR_v2_output_ex.csv
   :widths: 30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30
   :header-rows: 1

A description of each output field is provided below. The fields which are added by sawmill and thus only appear in the processed output are also annotated with the function responsible for adding them to the output.

Please note that the **odds_ratio**, **se_log_or**, and **pval** fields are added by the *do_MA* function when the row displays the results of a meta-analysis.

.. csv-table:: Output from CEDAR v2 Specification
   :file: CEDAR_v2_output_spec.csv
   :widths: 30,10,50
   :header-rows: 1

Output from CEDAR v1
~~~~~~~~~~~~~~~~~~~~

The following table is an example of processed timber from CEDAR v1.

While all fields present in the input timber are retained in the output, some will have new names. 
Sawmill renames some of the fields to improve uniformity between v1 and v2 outputs.

Please note that rows containing the results of a meta-analysis will look slightly different (for instance, some fields may have values of **NA**).

.. csv-table:: Output from CEDAR v1 Example
   :file: CEDAR_v1_output_ex.csv
   :widths: 30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30
   :header-rows: 1

A description of each output field is provided below. The fields which are added by sawmill and thus only appear in the processed output are also annotated with the function responsible for adding them to the output.
Please note that the **odds_ratio**, **se_log_or**, and **pval** fields are added by the *do_MA* function when the row displays the results of a meta-analysis.

.. csv-table:: Output from CEDAR v1 Specification
   :file: CEDAR_v1_output_spec.csv
   :widths: 30,10,50
   :header-rows: 1

What to check for
~~~~~~~~~~~~~~~~~

CEDAR v2: insensible_rate_table field
+++++++++++++++++++++++++++++++++++++

Check your output *.csv* file for rows where **insensible_rate_table** = TRUE.
These rows likely have data entry errors in the rate table columns, as this result indicates that (% AMR+ exposed) **+** (% AMR- exposed) does not come to approximately 100, and/or that (% AMR+ referent) **+** (% AMR- referent) does not come to approximately 100.

The scrap_pile
++++++++++++++

If your output file is significantly shorter than your input file or seems to be missing a good deal of factors, you may want to check the *scrap_pile*.

To view the first few rows of the *scrap_pile*, enter the following into the *Console* after running sawmill::
   
   scrap_pile

You should expect to see entries here that are missing the fields necessary to calculate an odds ratio; these cannot be salvaged.

If you see unexpected entries, please save the *scrap_pile* as a *.csv* file by entering the following lines into the *Console*::
   
   install.packages("readr")
   library(readr)
   readr::write_csv(scrap_pile, file.choose())

Examining this entire *.csv* file should give you a clue as to why most of your factors are being discarded, and how to fix the issue.
If not, contact Charly Phillips or Brennan Chapman.