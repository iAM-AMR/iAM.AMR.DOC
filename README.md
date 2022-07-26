

[![Documentation Status](https://readthedocs.org/projects/grdi-amr-iamamrdoc/badge/?version=latest)](https://docs.iam.amr.pub/en/latest/?badge=latest)  

# iAM.AMR Project Documentation

This repo contains the source code (i.e. the plain-text) of the [iAM.AMR Documentation site](https://docs.iam.amr.pub) hosted by [Read the Docs](https://readthedocs.org/).

For more details, see the [*Documentation* section](https://docs.iam.amr.pub/en/latest/reference/documentation.html) section of the documentation site.

## Citation

The recommended fields are:

Author(s): The iAM.AMR Team.  
Date: 2022  
Title: The iAM.AMR Project Documentation.  
URL: https://docs.iam.amr.pub  
DOI: (see below).  


### DOI

We use [Zenodo](https://zenodo.org/) to generate DOIs for our documentation.

Zenodo provides a static DOI for the project (a *concept* DOI), and a *version* DOI for each GitHub release ([more details](https://help.zenodo.org/#versioning)). 

#### Concept DOI

> You can use the Concept DOI representing all versions in citations when it is desirable to cite an evolving research artifact, without being specific about the version.

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.6823214.svg)](https://doi.org/10.5281/zenodo.6823214)  

#### Version DOI

> You should normally always use the DOI for the specific version of your record in citations. This is to ensure that other researchers can access the exact research artefact you used for reproducibility. By default, Zenodo uses the specific version to generate citations.

[![DOI](https://zenodo.org/badge/236518739.svg)](https://zenodo.org/badge/latestdoi/236518739)


## Development

### Build

- To check if a virtual environment exists: `python -m pipenv --venv`
- To create or activate a new virtual environment: `python -m pipenv shell`
- To build: `.\make.bat html`

### Empty Cache

If recent changes have been made to the documentation, they may not be reflected in browser, or may be incorrectly displayed due to cached elements (like the navigation side-bar).

We can clear the cache specifically for the documentation site.

#### Chrome / Edge

1. Open Chrome/Edge, and copy `chrome://settings/siteData` into the omnibox (the address bar).
2. Locate the documentation site, either in full `docs.iam.amr.pub`, or as the base domain `amr.pub`.
3. Use the garbage can icon to delete the cached data.

#### Firefox

1. Open Firefox, and copy `about:preferences#privacy` into the address bar.
2. Scroll down to *Cookies and Site Data* and click on the “Manage Data…” button.
3. Locate the documentation site by searching for the base domain `amr.pub`.
4. Use the *Remove Selected* button to delete the cached data.