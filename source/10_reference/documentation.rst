

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

How to Add a Page
~~~~~~~~~~~~~~~~~

This is how to add a page!

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


.. Conventions
.. -----------


reStructuredText
================

Guides
------

- `reST Full Specification <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_  
- `reST Quick Reference <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_
- `Sphinx's reST Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
- `reST Cheatsheet <https://docutils.sourceforge.io/docs/user/rst/cheatsheet.html>`_  


Document Layout
---------------

General
~~~~~~~
There shall be two blank lines at the **start** of each document. 

There shall be three blank lines at the **end** of each document.

Font
~~~~
*Italic* text is specified by surrounding text with one asterisk. **Bold** text is specified by surrounding text with two asterisks::

   *this text is italic*

   **this text is bold**

Headings
~~~~~~~~
There should be one blank line between sections of the same level (e.g. H1 -- H1) and between a section and a sub-section (e.g. H1 -- H2). There should be two blank lines between a sub-section and a greater section (e.g. H2 -- H1). There should be no blank line between a heading and the section's contents, where contents exist::

   Section
   =======
   contents

   Sub-section
   -----------
   contents


   Next Section
   ============
   
   Sub-section
   -----------
   contents

The following symbols should be used for headings::

   H1 ===
   H2 ---
   H3 ~~~
   H4 +++
   H5 ^^^

Only H1 and H2 level headings should use Title Case. Sub-headings should use Sentence case.

Heading Labels
++++++++++++++
To link to a duplicated heading (i.e. two sections in the same document have the same heading), you will need to specify a heading label. Heading labels should be used where the heading is a common word, phrase, or where the heading is known to be repeated later in the document. 

Heading labels are placed above the heading, with a blank line seperating the heading label and heading. Where heading labels are used, two blank lines should come before it, regardless of the heading level.
::

   .. _this_is_a_heading_label:

   This is the Heading
   -------------------

If there is a duplicated heading, you will recieve a build warning regardless of your specified label (as autosectionlabel creates its own labels automatically). The duplicated label will be ambiguous (testing seems to show it will default to the last entry), and therefore not suitable for linking.

We use a slightly different format for links to a manually labeled section (we drop the path); see the links section below for more details.


Links
-----

Internal links
~~~~~~~~~~~~~~
::

   :ref:`text <folder/docname:heading>`

Internal links to manual labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::
   
   :ref:`text <label_text>`

External links
~~~~~~~~~~~~~~
::

   `text <URL>`_

Internal links to downloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

   :download:`text <path/file.ext>`

Admonitions
-----------
Admonitions are specially marked topics or notes which appear inline with other content. They can be styled with custom CSS.

Standard
~~~~~~~~
::

   Example: 

   .. attention:: This is an attention admonition.

.. attention:: This is an attention admonition.
.. caution:: This is a caution admonition.
.. danger:: This is a danger admonition.
.. error:: This is an error admonition.
.. hint:: This is a hint admonition.
.. important:: This is an important admonition.
.. note:: This is a note admonition.
.. tip:: This is a tip admonition.
.. warning:: This is a warning admonition.

Custom
~~~~~~
::

   Example:

   .. admonition:: This is a Custom Admonition

      And this is its content.


.. admonition:: This is a Custom Admonition
   
   And this is its content.


References
----------
::

   The quick brown fox jumped over the lazy [#chapman]_ dog.

   .. [#chapman] Chapman, B. et al. (2019) The laziness of the common dog. Journal. Issue. DOI.


The quick brown fox jumped over the lazy [#chapman]_ dog.

.. [#chapman] Chapman, B. et al. (2019) The laziness of the common dog. Journal. Issue. DOI.


Images
------
::

   .. image:: images/image_name.png
      :height: 100px
      :width: 200 px
      :scale: 50 %
      :alt: alternate text
      :align: right

The same fields are applicable for figures.

Figures
-------
::

   .. figure:: /images/figure_name.png
      :align: center

      This is the descriptive text for the figure.


Text Substitutions
------------------

To setup a text substitution, add a block to your ``conf.py``::

  rst_prolog = """
  .. |placeholder| replace:: Definition
  .. |other| replace:: other definition
  """

Both ``rst_prolog`` and ``rst_epilogue`` should enable substitution. The following solution has also been proposed, but is untested::

  address = '192.168.1.1'
  port = 'port 3333'

  rst_prolog = """
  .. |address| replace:: {0}
  .. |port| replace:: {1}
  """.format(
  address, 
  port
  )

Then, simply add ``|placeholder|`` to your document to access the substitution.


