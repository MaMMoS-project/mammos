=========
Changelog
=========

The format follows `Keep a Changelog <https://keepachangelog.com/>`__. Versions
follow `semantic versioning <https://semver.org/>`__, the metapackage version is
updated according to the largest bump of any of the dependent packages.

..
   ADD NEW ENTRIES BELOW THIS COMMENT.

0.12.1 -- 2026-03-10
====================

Changed
-------

``mammos-analysis``
  - Change in the signature of ``KuzminResult.plot`` function: it does not accept
    a ``matplotlib.axes.Axes`` object to plot the Kuzmin plots any more.
    (`PR82 <https://github.com/MaMMoS-project/mammos-analysis/pull/82>`__)
  - Store spontaneous magnetisation in kA/m in ``KuzminResult``.
    (`PR83 <https://github.com/MaMMoS-project/mammos-analysis/pull/83>`__)


0.12.0 -- 2026-03-06
====================

Added
-----

``mammos-dft``
  - Added material Y2Ti4Fe18 to database. (`PR56 <https://github.com/MaMMoS-project/mammos-dft/pull/56>`__)

``mammos-entity``
  - Now ``Entity`` instances have a ``description`` attribute, containing a
    string with user-defined information (empty by default). (`PR102
    <https://github.com/MaMMoS-project/mammos-entity/pull/102>`__)
  - ``EntityCollection`` instances have a ``description`` attribute, containing
    a string with user-defined information (empty by default). (`PR103
    <https://github.com/MaMMoS-project/mammos-entity/pull/103>`__)
  - Added i/o functionalities to preserve ``description`` attribute for
    ``Entity`` and ``EntityCollection`` instances. This results in an extra
    metadata line (in csv format v3) or key (in yaml format v2) for files.
    Furthermore, in csv format v3 ontology and unit information are no longer
    commented. (`PR105
    <https://github.com/MaMMoS-project/mammos-entity/pull/105>`__)
  - Added function ``mammos_entity.search_labels`` to search for matches in the
    ontology to a specific label. (`PR117
    <https://github.com/MaMMoS-project/mammos-entity/pull/117>`__)
  - New methods ``EntityCollection.metadata`` to extract metadata for all
    entities in a collection (as dictionary) and
    ``EntityCollection.from_dataframe`` to convert a ``pandas.DataFrame`` +
    metadata dictionary into an ``EntityCollection``. (`PR123
    <https://github.com/MaMMoS-project/mammos-entity/pull/123>`__)
  - Dictionary-like interface for ``EntityCollection``: support for element
    access with ``["name"]`` notation, iterating over entities in collection and
    member-checks with ``in``. (`PR130
    <https://github.com/MaMMoS-project/mammos-entity/pull/130>`__)
  - Added functions to create anisotropy constants ``mammos_entity.K1``,
    ``mammos_entity.K2``. (`PR141
    <https://github.com/MaMMoS-project/mammos-entity/pull/141>`__)
  - Support for reading and writing HDF5 files. (`PR147
    <https://github.com/MaMMoS-project/mammos-entity/pull/147>`__)
  - A new property ``Entity.ontology_iri`` that returns the IRI of the
    corresponding element in the ontology. (`PR161
    <https://github.com/MaMMoS-project/mammos-entity/pull/161>`__)
  - Mammos yaml v2: description is now a top-level key; non-entity elements in a
    collection no longer have keys with null values (ontology_label,
    ontology_iri, descripiton, [unit]) in the yaml representation. (`PR173
    <https://github.com/MaMMoS-project/mammos-entity/pull/173>`__)
  - Mammos yaml v2: support for nested entity collections. (`PR174
    <https://github.com/MaMMoS-project/mammos-entity/pull/174>`__)
  - Mammos yaml v2: empty entity collections can not be saved to yaml (empty
    nested collections are allowed). (`PR176
    <https://github.com/MaMMoS-project/mammos-entity/pull/176>`__)

Changed
-------

``mammos-entity``
  - Class ``EntityCollection`` can now be accessed with
    ``mammos_entity.EntityCollection``. Operations are moved into the
    ``mammos_entity.operations`` submodules and are no longer accessible from
    the ``mammos_entity`` namespace. (Internally, some private submodules were
    renamed: ``_base`` -> ``_entity``, ``_entities`` -> ``_factory``, and
    ``_onto`` -> ``_ontology``. The code for ``EntityCollection`` has been moved
    to ``mammos_entity._entity_collection``.) (`PR115
    <https://github.com/MaMMoS-project/mammos-entity/pull/115>`__)
  - The method ``to_dataframe`` of class ``EntityCollection`` now has default
    value ``include_units=False``. (`PR116
    <https://github.com/MaMMoS-project/mammos-entity/pull/116>`__)
  - Definition and methods of ``Entity`` now rely on a list of set
    equivalencies, called ``mammos_equivalencies``. For the moment, they only
    include equivalencies between different temperature units. (`PR118
    <https://github.com/MaMMoS-project/mammos-entity/pull/118>`__)
  - The API for writing and reading files has been changed in a backward
    incompatible way. Writing is now done via methods
    ``EntityCollection.to_csv``, ``EntityCollection.to_hdf5`` and
    ``EntityCollection.to_yaml``. Reading with the functions
    ``mammos_entity.from_csv``, ``mammos_entity.from_hdf5``, and
    ``mammos_entity.from_yaml``. The ``io`` submodule has been removed. (`PR154
    <https://github.com/MaMMoS-project/mammos-entity/pull/154>`__)
  - Saving an empty EntityCollection to csv is no longer allowed. (`PR160
    <https://github.com/MaMMoS-project/mammos-entity/pull/160>`__)
  - All elements in an EntityCollection must have names of type str. (`PR172
    <https://github.com/MaMMoS-project/mammos-entity/pull/172>`__)
  - Updated versions of shipped ontologies: Magnetic Materials domain Ontology
    (MagMO) to 0.0.4, EMMO to 1.0.3. (`PR177
    <https://github.com/MaMMoS-project/mammos-entity/pull/177>`__)

``mammos-spindynamics``
  - Changed unit for spontaneous magnetization entities from ``A/m`` to
    ``kA/m``. (`PR68
    <https://github.com/MaMMoS-project/mammos-spindynamics/pull/68>`__)

Removed
-------

``mammos-dft``
  - Material Nd2Fe14B has been removed from the database. (`PR49
    <https://github.com/MaMMoS-project/mammos-dft/pull/49>`__)

``mammos-mumag``
  - Removed material parameter ``K2``, unused in the micromagnetic simulation.
    (`PR114 <https://github.com/MaMMoS-project/mammos-mumag/pull/114>`__)

``mammos-spindynamics``
  - Material Nd2Fe14B has been removed from the database. (`PR14
    <https://github.com/MaMMoS-project/mammos-spindynamics/pull/14>`__)

Fixed
-----

``mammos-analysis``
  - Changed ``SpontaneousMagnetization`` to ``Magnetization`` where relevant.
    Changed ``Ms`` to ``M`` where relevant. (`PR69
    <https://github.com/MaMMoS-project/mammos-analysis/pull/69>`__)

``mammos-entity``
  - Conversion to dataframe failed for entity collections containing only scalar
    entities. (`PR157
    <https://github.com/MaMMoS-project/mammos-entity/pull/157>`__)
  - Conversion of nested entity collection to dataframe is now prohibited.
    Before, the elements of the inner collection were added as dataframe rows.
    (`PR158 <https://github.com/MaMMoS-project/mammos-entity/pull/158>`__)
  - Fixed unit definition logic after update to MagMO 0.0.4. If the user
    provides a unit, it is accepted if it is equivalent to any of the ontology
    defined units. (`PR169
    <https://github.com/MaMMoS-project/mammos-entity/pull/169>`__)
  - Creating entities with secondary labels will from now on produce entities
    with the ``prefLabel`` as their ``ontology_label``. (`PR170
    <https://github.com/MaMMoS-project/mammos-entity/pull/170>`__)

``mammos-mumag``
  - Changed ``SpontaneousMagnetization`` to ``Magnetization`` when relevant.
    (`PR121 <https://github.com/MaMMoS-project/mammos-mumag/pull/121>`__)
  - Fixed logic of downloading meshes from Zenodo: if HTTP return code is not
    200 (everything OK), fallback on Keeper and download mesh from there.
    (`PR103 <https://github.com/MaMMoS-project/mammos-mumag/pull/103>`__)
  - Fixed and better documented mesh initialization logic. First meshes are
    searched locally, interpreting the mesh name as its path. If they are not
    found, the mesh name is looked up in the Zenodo record. (`PR106
    <https://github.com/MaMMoS-project/mammos-mumag/pull/106>`__)
  - Fixed bug in code, where parameters ``size`` and ``scale`` were not actually
    read. (`PR113 <https://github.com/MaMMoS-project/mammos-mumag/pull/113>`__)
  - Fixed typo in documentation. (`PR128
    <https://github.com/MaMMoS-project/mammos-mumag/pull/128>`__)

Misc
----

``mammos-dft``
  - Added source in the database of all calculations. (`PR46 <https://github.com/MaMMoS-project/mammos-dft/pull/46>`__)

``mammos-entity``
  - Use of ``csv`` Python module for i/o in csv format. (`PR104
    <https://github.com/MaMMoS-project/mammos-entity/pull/104>`__)
  - IRI is not checked for consistency when reading a file anymore. (`PR187
    <https://github.com/MaMMoS-project/mammos-entity/pull/187>`__)
  - Changed selection process of ontology label in the initialization of an
    Entity. First, the given label is matched for ``prefLabel`` in the ontology.
    If no match is found, the given label is matched for all alternative labels.
    If any of the previous steps finds more than one match, an error is raised.
    If no matches are found after the previous steps, an error is raised.
    (`PR191 <https://github.com/MaMMoS-project/mammos-entity/pull/191>`__)
  - An internal helper function to convert an entity-like to the desired entity.
    (`PR201 <https://github.com/MaMMoS-project/mammos-entity/pull/201>`__)

``mammos-mumag``
  - Removed debugging messages generated in the conjugate gradient optimization
    during the hysteresis loop. (`PR118
    <https://github.com/MaMMoS-project/mammos-mumag/pull/118>`__)


0.11.2 -- 2025-12-22
====================

Added
-----

``mammos-analysis``
  - ``extract_BHmax``: calculate BHmax based on M, H and demagnization_coefficient. This replaces ``extract_maximum_energy_product()`` which has the same purpose but a different user interface. (`PR53 <https://github.com/MaMMoS-project/mammos-analysis/pull/53>`__)

Removed
-------

``mammos-anylis``
  - ``extract_maximum_energy_product()``. Use ``extract_BHmax`` instead. (`PR53 <https://github.com/MaMMoS-project/mammos-analysis/pull/53>`__)

Misc
----

``mammos``
  - Updated hard magnetic AI surrogate model notebook (`PR65 <https://github.com/MaMMoS-project/mammos/pull/65>`__), after upgrade of `mammos-analysis to version 0.4.0 <https://github.com/MaMMoS-project/mammos-analysis/tree/0.4.0>`__


0.11.1 -- 2025-12-18
====================

Added
-----

``mammos``
  - Added micromagnetic simulation data to hard magnet AI example (and scripts to compute the data)
    (`PR62 <https://github.com/MaMMoS-project/mammos/pull/62>`__, `PR63 <https://github.com/MaMMoS-project/mammos/pull/63>`__)

Fixed
-----

``mammos``
  - Set the available number of ``OMP_NUM_THREADS`` to 1 in the spindynamics notebook. (`PR58 <https://github.com/MaMMoS-project/mammos/pull/58>`__)
  - Fixed binder links to AI spindynamics notebooks. (`PR59 <https://github.com/MaMMoS-project/mammos/pull/59>`__)

``mammos-spindynamics``
  - Indexing of ``TemperatureSweepData`` sub-runs. (`PR54 <https://github.com/MaMMoS-project/mammos-spindynamics/pull/54>`__)



0.11.0 -- 2025-12-17
====================

Added
-----

``mammos``
  - New demonstrator notebook: performing spindynamics simulations with UppASD
    to get temperature-dependent intrinsic properties.
    (`PR55 <https://github.com/MaMMoS-project/mammos/pull/55>`__)
``mammos-analysis``
  - Initial guesses for the Kuz'min fit are now allowed.
    (`PR50 <https://github.com/MaMMoS-project/mammos-analysis/pull/50>`__)
``mammos-spindynamics``
  - Python interface for UppASD.
    (`PR42 <https://github.com/MaMMoS-project/mammos-spindynamics/pull/42>`__,
    `PR43 <https://github.com/MaMMoS-project/mammos-spindynamics/pull/43>`__)

Changed
-------

``mammos``
  - Hard magnet demonstrator notebooks now use ``Fe2.33Ta0.67Y`` as default
    material. (`PR49 <https://github.com/MaMMoS-project/mammos/pull/49>`__)
``mammos-analysis``
  - Improved heuristics for the initial guess for the Kuz'min fit to make the
    fitting more robust. (`PR50 <https://github.com/MaMMoS-project/mammos-analysis/pull/50>`__)
``mammos-dft``
  - The values of posfiletype and maptype were added to the databases.
    (`PR43 <https://github.com/MaMMoS-project/mammos-dft/pull/43>`__)

0.10.0 -- 2025-12-15
====================

Added
-----

``mammos-dft``
  - A new function :py:func:`mammos_dft.db.get_uppasd_properties` to get inputs required for UppASD from the database. (`PR41 <https://github.com/MaMMoS-project/mammos-dft/pull/41>`__)


0.9.1 -- 2025-12-12
===================

Fixed
-----

``mammos-entity``
  - Fixed logic to establish ontology-preferred units. (`PR98 <https://github.com/MaMMoS-project/mammos-entity/pull/98>`__)
``mammos-spindynamics``
  - Fixed header of ``M.csv`` for Fe3Y and Fe2.33Ta0.67Y. (`PR45 <https://github.com/MaMMoS-project/mammos-spindynamics/pull/45>`__)


0.9.0 -- 2025-12-11
===================

New package ``mammos-ai`` added.

Added
-----

``mammos-ai``
  - A new AI model which can predict extrinsic magnetic properties (Hc, Mr, BHmax) from the
    intrinsic micromagnetic parameters Ms, A and K has been added. (`PR5 <https://github.com/MaMMoS-project/mammos-ai/pull/5>`__, `PR6 <https://github.com/MaMMoS-project/mammos-ai/pull/6>`__)


0.8.2 -- 2025-12-10
===================

Misc
----

``mammos``
  - Refactored Demonstrator page with examples from the ``mammos`` metapackage. (`PR46 <https://github.com/MaMMoS-project/mammos/pull/46>`__)
``mammos-dft``
  - Materials Fe3Y and Fe2.33Ta0.67Y were added to the database. (`PR39 <https://github.com/MaMMoS-project/mammos-dft/pull/39>`__)
``mammos-spindynamics``
  - Materials Fe3Y and Fe2.33Ta0.67Y were added to the database. (`PR41 <https://github.com/MaMMoS-project/mammos-spindynamics/pull/41>`__)


0.8.1 -- 2025-12-03
===================

Misc
----

``mammos-mumag``
  - Fixed dependencies: added `matplotlib`, `pandas`, and `urllib3`. (`PR93 <https://github.com/MaMMoS-project/mammos-mumag/pull/93>`__)
``mammos-spindynamics``
  - Fixed dependencies: added `numpy`. (`PR38 <https://github.com/MaMMoS-project/mammos-spindynamics/pull/38>`__)


0.8.0 -- 2025-11-27
===================

Added
-----

``mammos-analysis``
  - Added `celsius=True` option in the `plot` methods for the :py:mod:`mammos_analysis.kuzmin` module to generate plots in degree Celsius. (`PR40 <https://github.com/MaMMoS-project/mammos-analysis/pull/40>`__)
``mammos-mumag``
  - Added `tesla=True` option in the `plot` method of :py:class:`mammos_mumag.hysteresis.Result` to generate the hysteresis loop in Tesla units. (`PR87 <https://github.com/MaMMoS-project/mammos-mumag/pull/87>`__)


Changed
-------

``mammos_entity``
  - Improved ``io`` notebook. Use cases for working with :py:class:`~mammos_entity.EntityCollection` objects are added. (`PR83 <https://github.com/MaMMoS-project/mammos-entity/pull/83>`__)


Misc
----

``mammos-entity``
  - Fix dependencies: remove upper limit for `emmontopy` and add `pandas>2`. (`PR93 <https://github.com/MaMMoS-project/mammos-entity/pull/93>`__)


0.7.0 -- 2025-11-05
===================

Added
-----

``mammos-mumag``
  - Two new notebooks :doc:`/examples/mammos-mumag/hysteresis` and
    :doc:`/examples/mammos-mumag/additional-functionality` documenting
    additional functionality of ``mammos-mumag``. (`PR42
    <https://github.com/MaMMoS-project/mammos-mumag/pull/42>`__)
  - Create cli command ``unv2fly`` to convert unv mesh to fly format. (`PR61 <https://github.com/MaMMoS-project/mammos-mumag/pull/61>`__)
  - Added notebook :doc:`/examples/mammos-mumag/using_tesla` for information on how to set up a workflow in Tesla. (`PR68 <https://github.com/MaMMoS-project/mammos-mumag/pull/68>`__)
  - Added possibility to install GPU support (both CUDA and ROCm) with ``pip`` via the extra dependencies. (`PR81 <https://github.com/MaMMoS-project/mammos-mumag/pull/81>`__)

Fixed
-----

``mammos-analysis``
  - The function :py:func:`mammos_analysis.kuzmin.kuzmin_properties` will not assume the magnetization input is in ``A/m``. If the input is in a unit not convertible to ``A/m`` (e.g., Tesla), an error is raised. (`PR31 <https://github.com/MaMMoS-project/mammos-analysis/pull/31>`__)
``mammos-mumag``
  - Fixed default ``outdir`` input in two functions in :py:mod:`mammos_mumag.simulation`. (`PR69 <https://github.com/MaMMoS-project/mammos-mumag/pull/69>`__)


Changed
-------

``mammos-mumag``
  - Now :py:func:`mammos_mumag.hysteresis.run` can be used to execute simulations with multigrain materials. (`PR46 <https://github.com/MaMMoS-project/mammos-mumag/pull/46>`__)
  - Implement automatic retries to download meshes if the requests fail. The requests will try three times in total, with a backoff factor of 0.1. (`PR70 <https://github.com/MaMMoS-project/mammos-mumag/pull/70>`__)
  - Documentation is updated. Parameters have been formatted to snake case when possible. The names ``h_start``, ``h_final``, ``h_step``,  ``n_h_steps``, ``m_step``, ``m_final``, and ``tol_h_mag_factor`` take the place of ``hstart``, ``hfinal``, ``hstep``, ``nhsteps``, ``mstep``, ``mfinal``, and ``tol_hmag_factor``. Whenever possible, reasonable entities have been defined. The unused variables ``iter_max``, ``tol_u``, and ``verbose`` have been removed. **Warning**: this PR causes failure in previously defined workflows if the variables  were defined by the user. (`PR71 <https://github.com/MaMMoS-project/mammos-mumag/pull/71>`__)

Misc
----

``mammos-mumag``
  - Added :doc:`examples/mammos-mumag/hysteresis` to document full functionality of :py:mod:`mammos_mumag` when running a hysteresis loop simulation. Additionally, show the functionality of the package irrelevant to an average user in :doc:`examples/mammos-mumag/additional-functionality`. (`PR42 <https://github.com/MaMMoS-project/mammos-mumag/pull/42>`__)

0.6.0 -- 2025-08-13
===================

Added
-----

``mammos-entity``
  - CSV files written with ``mammos_entity.io`` can now optionally contain
    a description. (`PR52
    <https://github.com/MaMMoS-project/mammos-entity/pull/52>`__)
  - Support for YAML as additional file format in ``mammos_entity.io``.
    (`PR59 <https://github.com/MaMMoS-project/mammos-entity/pull/59>`__, `PR69
    <https://github.com/MaMMoS-project/mammos-entity/pull/69>`__, `PR70
    <https://github.com/MaMMoS-project/mammos-entity/pull/70>`__)
  - Two new functions ``mammos_entity.io.entities_to_file`` and
    ``mammos_entity.io.entities_from_file`` to write and read entity
    files. The file type is inferred from the file extension. (`PR57
    <https://github.com/MaMMoS-project/mammos-entity/pull/57>`__)
  - A function :py:func:`mammos_entity.operations.concat_flat` to concatenate compatible
    entities, quantities and array-likes into a single entity. (`PR56
    <https://github.com/MaMMoS-project/mammos-entity/pull/56>`__)
``mammos-mumag``
  - Add function :py:func:`mammos_mumag.hysteresis.read_result` to read the
    result of a hysteresis loop from a folder (without running the hysteresis
    calculation again). (`PR48
    <https://github.com/MaMMoS-project/mammos-mumag/pull/48>`__)
  - Implement :py:class:`mammos_mumag.mesh.Mesh` class that can read and display
    information of local meshes, meshes on Zenodo and meshes given by the user.
    (`PR53 <https://github.com/MaMMoS-project/mammos-mumag/pull/53>`__)

Changed
-------

``mammos-analysis``
  - The Kuz'min formula to evaluate micromagnetic properties can now accept
    Curie Temperature Tc and spontaneous magnetisation at zero temperature Ms_0
    as optional inputs. If given, they are not optimised by fitting the
    magnetisation curve. (`PR12
    <https://github.com/MaMMoS-project/mammos-analysis/pull/12>`__)
  - The initial guess for the optimization of the Curie Temperature in Kuz'min
    formula is set to a much lower temperature (depending on the data). (`PR18
    <https://github.com/MaMMoS-project/mammos-analysis/pull/18>`__)
``mammos-entity``
  - When reading files with ``mammos_entity.io`` IRIs are now checked in
    addition to ontology labels and file reading fails if there is a mismatch
    between IRI and ontology label. (`PR68
    <https://github.com/MaMMoS-project/mammos-entity/pull/68>`__)
``mammos-mumag``
  - Changed the output of the hysteresis loop in compliance with
    ``mammos_entity.io`` v2. (`PR54
    <https://github.com/MaMMoS-project/mammos-mumag/pull/54>`__)

Deprecated
----------

``mammos-entity``
  - The functions ``mammos.entity.io.entities_to_csv`` and
    ``mammos_entity.io.entities_from_csv`` have been deprecated. Use
    ``mammos_entity.io.entities_to_file`` and
    ``mammos_entity.io.entities_from_file`` instead. (`PR58
    <https://github.com/MaMMoS-project/mammos-entity/pull/58>`__)

Fixed
-----

``mammos-entity``
  - On Windows, CSV files written with mammos-entity had blank lines between all
    data lines. (`PR66
    <https://github.com/MaMMoS-project/mammos-entity/pull/66>`__)
  - Writing CSV files with entities of different shapes 0 and 1, where elements
    with shape 0 were broadcasted is no longer supported as it is not round-trip
    safe. (`PR67 <https://github.com/MaMMoS-project/mammos-entity/pull/67>`__)
``mammos-dft``
  - Update attribute name of uniaxial anisotropy constant to `Ku_0` from `K1_0`
    for the returned `MicromagneticProperties` object during a database lookup.
    (`PR19 <https://github.com/MaMMoS-project/mammos-dft/pull/19>`__)
``mammos-mumag``
  - Fixed the default values of the
    :py:class:`~mammos_mumag.materials.MaterialDomain` class. (`PR41
    <https://github.com/MaMMoS-project/mammos-mumag/pull/41>`__)

0.5.0 -- 2025-07-11
===================

Added
-----

``mammos-entity``
  - A new submodule ``mammos_entity.io`` that provides two functions to
    write and read CSV files with additional ontology metadata. For more details
    refer to the new ``io`` documentation.
    (`PR29 <https://github.com/MaMMoS-project/mammos-entity/pull/29>`__, `PR46
    <https://github.com/MaMMoS-project/mammos-entity/pull/46>`__, `PR47
    <https://github.com/MaMMoS-project/mammos-entity/pull/47>`__ )

Fixed
-----

``mammos-entity``
  - Fix bug when defining unitless entities. (`PR37
    <https://github.com/MaMMoS-project/mammos-entity/pull/37>`__ and `PR45
    <https://github.com/MaMMoS-project/mammos-entity/pull/45>`__)

0.4.0 -- 2025-06-27
===================

Changed
-------

``mammos-entity``
  - The ``Entity`` class is no longer a subclass of ``mammos_units.Quantity``.
    As a consequence it does no longer support mathematical operations. Use the
    attribute ``.quantity`` (or the short-hand ``.q``) to access the underlying
    quantity and to perform (mathematical) operations. (`PR28
    <https://github.com/MaMMoS-project/mammos-entity/pull/28>`__)
  - The package now comes with a bundled ontology consisting of `EMMO
    <https://github.com/emmo-repo/EMMO>`__ (version 1.0.0-rc3) and `Magnetic
    Material <https://github.com/MaMMoS-project/MagneticMaterialsOntology>`__
    (version 0.0.3). Internet access is no longer required. (`PR33
    <https://github.com/MaMMoS-project/mammos-entity/pull/33>`__)
``mammos``
  - Use Fe16N2 instead of Nd2Fe14B in hard magnet workflow. (`PR17
    <https://github.com/MaMMoS-project/mammos/pull/17>`__)

0.3.0 -- 2025-06-11
===================

Added
-----

``mammos-entity``
  - New predefined entity ``mammos_entity.J``
  - New predefined entity ``mammos_entity.Js``
``mammos-mumag``
  - Optional argument ``plotter`` in ``plot_configuration`` to add a vector plot
    of a magnetization configuration to a :py:class:`pyvista.Plotter` provided
    by the caller.

Changed
-------

``mammos-entity``
  - Return a ``mammos_units.UnitConversionError`` (inherited from
    ``astropy.units``) when trying initialize an entity with incompatible units.

0.2.0 -- 2025-06-06
===================

Added
-----

``mammos``
  - Command-line script ``mammos-fetch-examples`` to download all example
    notebooks.
``mammos-entity``
  - Entity objects have ``ontology_label_with_iri`` attribute.

Changed
-------

``mammos-entity``
  - When trying to initialize an entity with a wrong unit the error message does
    now show the required unit defined in the ontology.

Fixed
-----

``mammos-entity``
  - ``Entity.to`` did not return a new entity in the requested units and instead
    used the default entity units.
  - ``Entity.axis_label``: unit inside parentheses instead of brackets.

0.1.0 -- 2025-06-05
===================

Added
-----

``mammos`` -- 0.1.0
  - Workflows for hard magnets and sensor shape optimization.
  - Ensures compatible software components are installed.
``mammos-analysis`` -- 0.1.0
  - Calculation of macroscopic properties (Mr, Hc, BHmax) from a hysteresis
    loop.
  - Fitting of the linear segment of a hysteresis loop.
  - Calculation of temperature-dependent micromagnetic properties from atomistic
    spin dynamics simulations using Kuz’min equations.
``mammos-dft`` -- 0.3.0
  - Database lookup functionality for a selection of pre-computed materials.
``mammos-entity`` -- 0.5.0
  - Provides entities: quantities with links to the MaMMoS ontology (based on
    EMMO) by combining ``mammos-units`` and `EMMOntoPy
    <https://github.com/emmo-repo/EMMOntoPy>`__.
  - Helper functions to simplify creation of commonly required magnetic entities.
``mammos-mumag`` -- 0.6.0
  - Finite-element hysteresis loop calculations.
  - Requires a separate installation of `esys-escript
    <https://github.com/LutzGross/esys-escript.github.io/>`__.
``mammos-spindynamics`` -- 0.2.0
  - Database lookup functionality for a selection of pre-computed materials.
``mammos-units`` -- 0.3.1
  - Extension of astropy.units that allows working with quantities (units with
    values) containing additional units relevant for magnetism.
