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
   * - mammos
     - Workflows in :doc:`examples/index`
     - –
     - .. image:: https://mybinder.org/badge_logo.svg
          :target: https://mybinder.org/v2/gh/mammos-project/mammos/main?urlpath=lab%2Ftree%2Fdocs%2Fsource%2Fexamples%2Fworkflows

Installation
------------

The MaMMoS software suite consists of a collection of packages for ... workflows. The metapackage ``mammos`` can be used to install a consistent set of sub-packages.


.. tab-set::

   .. tab-item:: pixi (recommended)

      Use `pixi <https://pixi.sh/latest/>`__ to also install Python and optionally packages from conda-forge.

      .. code:: shell

         pixi init
         pixi add python=3.13
         pixi add mammos --pypi

      To conveniently work with the notebook tutorials we install
      ``jupyterlab``. (``packaging`` needs to be pinned due to a limitation of
      pixi/PyPI.)

      .. code:: shell

         pixi add jupyterlab packaging<25

      Some examples also require `esys-escript
      <https://github.com/LutzGross/esys-escript.github.io>`__. On linux we can
      install it from conda-forge. On Mac or Windows refer to the esys-escript
      installation instructions.

      .. code:: shell

         pixi add esys-escript   # linux only

      Finally start a shell where the installed packages are available.

      .. code:: shell

         pixi shell

   .. tab-item:: pip
      :sync: pip_install

      When using ``pip`` we recommend creating a virtual environment to isolate the MaMMoS installation.

      .. code:: shell

         python3 -m venv .env
         . .env/bin/activate
         pip install mammos

      Some examples also require `esys-escript
      <https://github.com/LutzGross/esys-escript.github.io>`__, which must be
      installed separately. Please refer to the documentation of esys-escript
      for installation instructions.

   .. tab-item:: conda/mamba

      Use ``conda`` or ``mamba`` in combination with ``pip`` to get packages from
      conda-forge and PyPI. We recommend using `miniforge <https://github.com/conda-forge/miniforge>`__.

      To conveniently work with the notebook tutorials we install
      ``jupyterlab``. (``packaging`` needs to be pinned due to a dependency
      issue in ``mammos-entity``.)

      Some examples also require `esys-escript
      <https://github.com/LutzGross/esys-escript.github.io>`__. On linux we can
      install it from conda-forge. On Mac or Windows refer to the esys-escript
      installation instructions.

      .. code:: shell

         conda create -n mammos-environment python=3.13 pip jupyterlab packaging<25 esys-escript
         conda activate mammos-environment
         pip install mammos

Acknowledgement
---------------

This software has been supported by the European Union’s Horizon Europe research and innovation programme under grant agreement No 101135546 `MaMMoS <https://mammos-project.github.io/>`__.
