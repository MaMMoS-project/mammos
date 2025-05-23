.. MaMMoS documentation master file, created by
   sphinx-quickstart on Wed May 21 08:47:01 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MaMMoS documentation
====================

.. toctree::
   :maxdepth: 1
   :hidden:

   Home <self>
   examples/index
   api
   changelog

About
-----

MaMMoS provides software suite for magnetic multiscale modeling. It consists of several software components. The following table provides a short overview and contains links to example and API reference for the individual packages. The binder badges allow running the examples for the individual packages interactively in the cloud.

.. list-table::
   :header-rows: 1

   * - Package
     - Examples
     - API
     - Interactive examples
   * - mammos-analysis
     - :doc:`examples/mammos-analysis/index`
     - :doc:`_autosummary/mammos_analysis`
     - .. image:: https://mybinder.org/badge_logo.svg
          :target: https://mybinder.org/v2/gh/mammos-project/mammos-analysis/main?urlpath=lab%2Ftree%2Fexamples
   * - mammos-dft
     - :doc:`examples/mammos-dft/index`
     - :doc:`_autosummary/mammos_dft`
     - .. image:: https://mybinder.org/badge_logo.svg
          :target: https://mybinder.org/v2/gh/mammos-project/mammos-dft/main?urlpath=lab%2Ftree%2Fexamples
   * - mammos-entity
     - :doc:`examples/mammos-entity/index`
     - :doc:`_autosummary/mammos_entity`
     - .. image:: https://mybinder.org/badge_logo.svg
          :target: https://mybinder.org/v2/gh/mammos-project/mammos-entity/main?urlpath=lab%2Ftree%2Fexamples
   * - mammos-mumag
     - :doc:`examples/mammos-mumag/index`
     - :doc:`_autosummary/mammos_mumag`
     - .. image:: https://mybinder.org/badge_logo.svg
          :target: https://mybinder.org/v2/gh/mammos-project/mammos-mumag/main?urlpath=lab%2Ftree%2Fexamples
   * - mammos-spindynamics
     - :doc:`examples/mammos-spindynamics/index`
     - :doc:`_autosummary/mammos_spindynamics`
     - .. image:: https://mybinder.org/badge_logo.svg
          :target: https://mybinder.org/v2/gh/mammos-project/mammos-spindynamics/main?urlpath=lab%2Ftree%2Fexamples
   * - mammos-units
     - :doc:`examples/mammos-units/index`
     - :doc:`_autosummary/mammos_units`
     - .. image:: https://mybinder.org/badge_logo.svg
          :target: https://mybinder.org/v2/gh/mammos-project/mammos-units/main?urlpath=lab%2Ftree%2Fexamples


Installation
------------

The MaMMoS software suite consists of a collection of packages for ... workflows. The metapackage ``mammos`` can be used to install a consistent set of sub-packages.


.. tab-set::

   .. tab-item:: pip
      :sync: pip_install

      We recommend to create a virtual environment to isolate the MaMMoS installation.

      .. code:: shell

         python3 -m venv .env
         . .env/bin/activate
         pip install mammos

   .. tab-item:: pixi

      Use pixi to also install packages Python and optionally packages from conda-forge.

      .. code:: shell

         pixi init
         pixi add python=3.13
         pixi add mammos --pypi
         pixi shell

..
  .. tab-item:: conda

      Not yet supported


Acknowledgement
---------------

This software has been supported by the European Union’s Horizon Europe research and innovation programme under grant agreement No 101135546 `MaMMoS <https://mammos-project.github.io/>`__.
