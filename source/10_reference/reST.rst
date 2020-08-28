

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

