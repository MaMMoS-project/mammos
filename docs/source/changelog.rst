=========
Changelog
=========

The format follows `Keep a Changelog <https://keepachangelog.com/>`__. Versions
follow `semantic versioning <https://semver.org/>`__, the metapackage version is
updated according to the largest bump of any of the dependent packages.

0.1.0 - Unreleased
==================

Added
-----

``mammos``
  - Workflows for hard magnets and sensor shape optimization.
  - Ensures compatible software components are installed.
``mammos-analysis`` -- v0.x.y
  - Calculation of macroscopic properties (Mr, Hc, BHmax) from a hysteresis
    loop.
  - Fitting of the linear segment of a hysteresis loop.
  - Calculation of temperature-dependent micromagnetic properties from atomistic
    spin dynamics simulations using Kuz’min equations.
``mammos-dft`` -- v0.x.y
  - Database lookup functionality for a selection of pre-computed materials.
``mammos-entity`` -- v0.x.y
  - Provides entities: quantities with links to the MaMMoS ontology (based on
    EMMO) by combining ``mammos-units`` and
    [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy).
  - Helper functions to simplify creation of commonly required magnetic entities.
``mammos-mumag`` -- v0.x.y
  - Finite-element hysteresis loop calculations.
  - Requires a separate installation of
    [esys-escript](https://github.com/LutzGross/esys-escript.github.io/).
``mammos-spindynamics`` -- v0.x.y
  - Database lookup functionality for a selection of pre-computed materials.
``mammos-units`` -- v0.x.y
  - Extension of astropy.units that allows working with quantities (units with
    values) containing additional units relevant for magnetism.
