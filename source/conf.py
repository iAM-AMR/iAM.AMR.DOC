# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'iAM.AMR'
copyright = '2022, iAM.AMR Team'
author = 'iAM.AMR Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel'
]

master_doc = 'index'


# -- Extension configuration -------------------------------------------------
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_js_files = [
    'https://p.trellocdn.com/embed.min.js'
]

# From an online source, no docs to explain the format.
# 
# In my conf.py I added this:
#
# address = '192.168.1.1'
# port = 'port 3333'
#
# rst_prolog = """
# .. |address| replace:: {0}
# .. |port| replace:: {1}
# """.format(
# address, 
# port
# )

rst_prolog = """
.. |pm| replace:: Brennan Chapman
.. |smod| replace:: story model
.. |anavcur| replace:: 6.1.0
.. |anavsup| replace:: 5.0.0
.. |br| raw:: html

    <br>

.. |hr| raw:: html

   <hr>
"""