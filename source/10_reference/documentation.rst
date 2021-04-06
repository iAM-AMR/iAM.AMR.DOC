

Documentation
=============

About this Documentation
------------------------
The iAM.AMR project's documentation is written in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ (reST), generated using `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_, and hosted by `Read the Docs <https://readthedocs.org/>`_.

reStructuredText
~~~~~~~~~~~~~~~~
reST, or `reStructuredText <http://docutils.sourceforge.net/rst.html>`_, is a lightweight `markup language <https://en.wikipedia.org/wiki/Markup_language>`_ originally created to document the programming language `Python <https://www.python.org/>`_.

A markup language, such as reST, is a system for creating and formatting complex documents from simple plain-text files. In a nutshell, markup languages define document properties (such as titles, chapters, paragraph breaks, **bolds** and *italics*) within the text itself, ensuring that no matter how the document is conveyed to the reader (e.g. as a website, as a PDF, or as an e-book), the content will always be structured in the same way.

.. note:: If you’ve ever used `LaTex <https://www.latex-project.org/>`_ or designed a website in `HTML <https://en.wikipedia.org/wiki/HTML>`_, you’ve already used a markup language!

This is in contrast to a ‘What-You-See-Is-What-You-Get’ or WYSIWYG system, such as Microsoft Word or Google Docs, where the content and structure of the document are specified separately and are interpreted in a way unique to the program itself. The drawbacks of such a system are evident if you’re a frequent user of Word and Google Docs (or Pages on a Mac) -- if you open a document from one of these programs using another, you’ll often see inexplicable formatting errors caused by differing interpretations of the structure of the document.

reST is relatively simple to learn. reST uses lines of symbols to designate headings, brackets to designate links, and tags to designate more complex document structures. To give you an idea of how simple reST is, the plain-text version of the above section is included below, and reference material for reST is provided in a subsequent section::

    iAM.AMR Documentation
    =====================

    About this Documentation
    ------------------------
    The iAM.AMR project's documentation is written in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ (reST), generated using `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_, and hosted by `Read the Docs <https://readthedocs.org/>`_.

    reStructuredText
    ~~~~~~~~~~~~~~~~
    reST, or `reStructuredText <http://docutils.sourceforge.net/rst.html>`_, is a lightweight `markup language <https://en.wikipedia.org/wiki/Markup_language>`_ originally created to document the programming language `Python <https://www.python.org/>`_.

    A markup language, such as reST, is a system for creating and formatting complex documents from simple plain-text files. In a nutshell, markup languages define document properties (such as titles, chapters, paragraph breaks, **bolds** and *italics*) within the text itself, ensuring that no matter how the document is conveyed to the reader (e.g. as a website, as a PDF, or as an e-book), the content will always be structured in the same way.

    .. note:: If you’ve ever used `LaTex <https://www.latex-project.org/>`_ or designed a website in `HTML <https://en.wikipedia.org/wiki/HTML>`_, you’ve already used a markup language!

    This is in contrast to a ‘What-You-See-Is-What-You-Get’ or WYSIWYG system, such as Microsoft Word or Google Docs, where the content and structure of the document are specified separately and are interpreted in a way unique to the program itself. The drawbacks of such a system are evident if you’re a frequent user of Word and Google Docs (or Pages on a Mac) -- if you open a document from one of these programs using another, you’ll often see inexplicable formatting errors caused by differing interpretations of the structure of the document.

    reST is relatively simple to learn. reST uses lines of symbols to designate headings, brackets to designate links, and tags to designate more complex document structures. To give you an idea of how simple reST is, the plain-text version of the above section is included below, and reference material for reST is provided in a subsequent section.

Sphinx and Read the Docs
~~~~~~~~~~~~~~~~~~~~~~~~
`Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ (likewise created to document the programming language Python), is the tool used to convert plain-text reST into the desired output format (e.g. website, PDF, or e-book). 

`Read the Docs <https://readthedocs.org/>`_ is a free hosting service supported by `unobtrusive and ethical ads <https://docs.readthedocs.io/en/latest/advertising/ethical-advertising.html>`_, which we use to host our documentation online. Read the Docs uses Sphinx to generate the web-pages, and provide PDF versions of the documentation for offline readers.

Version Control and GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~
The master-copies of the documentation (in reST format), are stored in a `GitHub <https://github.com/>`_ repository, under `version control <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>`_. When Read the Docs detects a change in these files, it automatically rebuilds and updates the website accordingly.

.. note:: Changes to the documentation require 2 – 10 minutes to propagate from GitHub to Read the Docs. 

.. tip:: If the documentation site does not reflect a recent change, ensure you ‘hard-refresh’ your browser using CTRL+F5 on Chrome or Firefox on Windows, or by following `the instructions here <https://en.wikipedia.org/wiki/Wikipedia:Bypass_your_cache>`_.


Editing this Documentation
--------------------------
Note that the use of `GitHub <https://github.com/>`_ is outside of the scope of this section. Please refer to the GitHub-specific documentation. 

Minor Edits
~~~~~~~~~~~
To make a minor edit or addition, follow the link in the upper-right corner of the target page to GitHub, where you can fork the document, make changes, and submit a pull request.

Major Edits
~~~~~~~~~~~
To make a major edit or addition, we recommend you clone the repository to your workstation and use an IDE such as `Visual Studio Code <https://code.visualstudio.com/>`_ -- coupled with a local version of Python and Sphinx -- to preview the changes before submitting a pull request.

Installing VSC, Python, and Sphinx
++++++++++++++++++++++++++++++++++
Detailed installation instructions to install VSC, Python, and Sphinx is outside the scope of this documentation. In brief:

#. Download and install `Visual Studio Code <https://code.visualstudio.com/>`_  
#. Download and install the latest version of `Python <https://www.python.org/>`_
#. Download and install the latest version of `Sphinx <http://www.sphinx-doc.org/en/master/usage/installation.html>`_ and `Read the Docs Sphinx Theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html>`_  

   - using PIP (via Python): ``pip install -U sphinx sphinx-autobuild sphinx_rtd_theme``  

#. Enable the Python and reStructuredText extensions in VSC  

.. tip:: If the preview window in VSC displays content without the theme (i.e. colours, formatting), ensure the explorer panel is open to the root directory (where build/ and source/ are) so VSC can locate conf.py that specifies the theme.


Documentation FAQs
------------------

How do I view online images at full-size?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To view images on the website at full-size, right-click on the image and select *open in new tab* or *open in new window*.


Conventions
-----------

Style Guide
~~~~~~~~~~~

The following should always be capitalized:

- Intelligent Array

The proper name of functions and objects should always be capitalized where refering to a generic function or object: 

- e.g. 'Choice function'; 'Table()'; 'Uniform function'

The names of specific objects should always be capitalized and italicized. The type of object is not capitalized or italicized:

- e.g. 'the *Interface* index'; 'the *Frequency* node'

Key Words
~~~~~~~~~
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" are to be interpreted as described in `RFC 2119 <https://www.ietf.org/rfc/rfc2119.txt>`_:

MUST
   This word, or the terms "REQUIRED" or "SHALL", mean that the definition is an absolute requirement of the specification.
MUST NOT   
   This phrase, or the phrase "SHALL NOT", mean that the definition is an absolute prohibition of the specification.
SHOULD
   This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course.
SHOULD NOT   
   This phrase, or the phrase "NOT RECOMMENDED" mean that there may exist valid reasons in particular circumstances when the particular behavior is acceptable or even useful, but the full implications should be understood and the case carefully weighed before implementing any behavior described with this label.
MAY
   This word, or the adjective "OPTIONAL", mean that an item is truly optional. An implementation which does not include a particular option MUST be prepared to interoperate with another implementation which does include the option, though perhaps with reduced functionality. In the same vein an implementation which does include a particular option MUST be prepared to interoperate with another implementation which does not include the option (except, of course, for the feature the option provides).

Common Acronyms
~~~~~~~~~~~~~~~
AAFC
   Agriculture and Agri-food Canada

AMR
   Antimicrobial Resistance

AMU
   Antimicrobial Use

CFIA
   Canadian Food Inspection Agency

CIPARS
   Canadian Integrated Program for Antimicrobial Resistance Surveillence

CSS
   Cascading Style Sheets

GRDI
   Genomics Research and Development Initiative

HC
   Health Canada

NSD
   National Service Desk

PHAC
   Public Health Agency of Canada

SSC
   Shared Services Canada

3GC
   Third-generation Cephalosporins

Model Names
~~~~~~~~~~~
The models are named **iAM.AMR.XZY** where **XYZ** represents a three character short-code identifying the model. The code should be relevant to the contents of the model.

* e.g. the iAM.AMR.CHI model focuses on chickens, while the iAM.AMR.3GC focuses on third-generation cephalosporins.


Factor Identifier
~~~~~~~~~~~~~~~~~
The factor identifier is automatically generated by the :ref:`sawmill R package <data_extraction/Sawmill:The sawmill R Package>`, in the format **A#####_Name_of_Factor** where:

* **A** is either 'R' for a standard factor, or 'M' for a meta-analysis
* **#####** is the factor or meta-analysis number

Where multiple factors inform a single node:

* and one or more of the factors is a meta-analysis, use the meta-analysis identifier with the lowest number
* and all of the factors are not meta-analyses, use the identifier with the lowest number
* and all of the factors are meta-analyses, use the identifier with the lowest number

In some instances, it may be appropriate to deviate from this schema – care should be taken to maintain consistency despite these deviations.

Study Groups
~~~~~~~~~~~~

Study groups should be named as follows:

**Referent**: The group which represents the default practice in Canadian industry, or the least interventionist.

**Comparator**: The group which represents the less common, or more interventionist group.

.. note:: If a study has more than two groups, all groups except the Referent should be titled Comparator 1, Comparator 2, etc. For example, a study examining the effect of AMU on AMR may have multiple comparator groups, each representing a slightly different dosage or treatment regime.

Node Colour
~~~~~~~~~~~
Colour is used to indicate the function and contents of each node. The use of colour in the model should conform to the general scheme:

Light Grey
   Non user-modifiable node that performs intermediate calculations, or which is otherwise exposed to the user via a separate user interface
Dark Grey
   A node containing a list of factors
Orange
   An objective node, containing intermediate or final results of calculations
Purple
   A user interface node
Blue
   A factor node, or a node which contains epidemiological data

Note, the following colour designations are liable to change, as the models are further standardized:

Pink
   A node in which the factor is informed by meta-analysis
Peach
   A node which contains information for multiple bacterial species
Gold
   A node which contains information for multiple bacterial species, informed by meta-analyses

