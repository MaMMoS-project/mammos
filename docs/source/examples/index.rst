Examples
========

End-to-end workflows are shown in the following set of tutorials. Some require additional software, see `Requirements` at the top of the individual workflows.

Demonstrator workflows
----------------------

.. toctree::
   :caption: Demonstrator
   :maxdepth: 1
   :hidden:

   workflows/hard-magnet-tutorial
   workflows/hard-magnet-material-exploration
   workflows/sensor

* `Hard magnet tutorial <workflows/hard-magnet-tutorial>`__ |binder-1|
* `Hard magnet material exploration <workflows/hard-magnet-material-exploration>`__ |binder-2|
* `Sensor shape optimization workflow <workflows/sensor>`__  |binder-3|

.. |binder-1| image:: /_static/badge-launch-binder2.svg
   :target: https://notebooks.mpcdf.mpg.de/binder/v2/gl/mammos-project%2Fmammos/latest?urlpath=lab%2Ftree%2Fexamples%2Fhard-magnet-tutorial.ipynb

.. |binder-2| image:: /_static/badge-launch-binder2.svg
   :target: https://notebooks.mpcdf.mpg.de/binder/v2/gl/mammos-project%2Fmammos/latest?urlpath=lab%2Ftree%2Fexamples%2Fhard-magnet-material-exploration.ipynb

.. |binder-3| image:: /_static/badge-launch-binder2.svg
   :target: https://notebooks.mpcdf.mpg.de/binder/v2/gl/mammos-project%2Fmammos/latest?urlpath=lab%2Ftree%2Fexamples%2Fsensor.ipynb



Tutorials for the individual packages
-------------------------------------

Further examples for the individual packages are available in these tutorials:

.. toctree::
   :caption: Packages
   :maxdepth: 2

   mammos-analysis/index
   mammos-dft/index
   mammos-entity/index
   mammos-mumag/index
   mammos-spindynamics/index
   mammos-units/index

.. _download-all-examples:

Downloading all examples
------------------------

To conveniently download all example notebooks use the ``mammos-fetch-examples``
script, which is installed as part of the ``mammos`` package. All notebooks are
written to a new `examples` directory with a subdirectory per package. The
command fails if a directory or file with the name `example` exists in the
current working directory.

Upon completion a list of downloaded examples is displayed:

.. code:: shell

   $ mammos-fetch-examples
   Downloading examples...
   The following examples have been downloaded:
   examples/mammos/hard-magnet-material-exploration.ipynb
   examples/mammos/hard-magnet-tutorial.ipynb
   examples/mammos/sensor.ipynb
   examples/mammos-analysis/quickstart.ipynb
   examples/mammos-dft/quickstart.ipynb
   examples/mammos-entity/quickstart.ipynb
   examples/mammos-entity/io.ipynb
   examples/mammos-mumag/quickstart.ipynb
   examples/mammos-spindynamics/quickstart.ipynb
   examples/mammos-units/example.ipynb
   examples/mammos-units/quickstart.ipynb
