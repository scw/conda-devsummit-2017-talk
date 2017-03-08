Harnessing the Power of Python in ArcGIS using the Conda Distribution
=====================================================================

### Shaun Walbridge & Clinton Dow
### Esri DevSummit 2017

**[View the Slides](https://4326.us/esri/conda-2017/)**

**[Download Handout Version (PDF)](https://4326.us/esri/conda-2017/devsummit-2017-conda-arcgis-presentation-handout.pdf)**

**[Download High Quality Version (PDF, 4MB)](https://4326.us/esri/r/devsummit-2017-conda-arcgis-presentation-full.pdf)**

Description
-----------

Python has a rich ecosystem of packages you can use in your own code,
but installation used to be complex. Conda will be included with ArcGIS Pro 1.3,
and allows you to easily install libraries into your Python environment, and
distribute that code to others. Join us and learn to bend Python to your will.

Building
--------

 - From `slides/`, run `make` to rebuild the slide deck from the included slides.md file. Requires [Pandoc](http://johnmacfarlane.net/pandoc/).
  - Check links with `make check`, requires [LinkChecker](https://pypi.python.org/pypi/LinkChecker).
   - Generate handout version with `make pdf`. Requires XeTeX and pandoc.
    - Generate high-quality PDF with `make fullpdf`. Requires [decktape.js](https://github.com/astefanutti/decktape)
