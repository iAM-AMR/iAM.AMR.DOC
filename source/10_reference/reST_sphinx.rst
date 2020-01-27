

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To be done.


Documentation FAQs
------------------

How do I view online images at full-size?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To view images on the website at full-size, right-click on the image and select *open in new tab* or *open in new window*.


