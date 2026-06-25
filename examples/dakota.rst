Sensor shape optimization with Dakota
=====================================

This example documents how an external optimizer such as Dakota can be used
together with the mammos framework. We consider the same optimization problem
as in the :doc:`sensor`: finding the optimal shape of a rhombohedral sensor to maximize the
linear section of the hysteresis loop. We will optimize the lengths of the two axes of
the rhombus, here called ``sx`` and ``sy``.

We assume the user has already installed a version of Dakota compatible with the
MaMMoS software suite, i.e. compiled with Python 3.11. The compilation must have
included all the necessary Python flags (for further information, see `here <https://snl-dakota.github.io/docs/6.24.0/users/usingdakota/advanced/advancedsimulationcodeinterfaces.html#python>`__).

A recipe for compiling Dakota on Linux can be found in https://github.com/MaMMoS-project/dakota-sensor-optimization.

To use Dakota's Python interface, first we need to define a Python function
accepting inputs and creating output in the format compatible with Dakota.
In particular, this function must accept a dictionary input where the item ``cv``
holds the continuous variables. The output is expected to be a dictionary with
the items ``fns`` (list of objective function values evaluated at the
continuous variables), ``fnGrads`` (the list of gradient values), and
``fnHessians`` (list of Hessian values), if needed. See :ref:`sensor-py` for
an example reproducing the optimization problem in :doc:`sensor`.

The function ``optimize`` interacts directly with the Dakota interface, while
the function ``objective`` defines the micromagnetic simulation. In
particular, it builds the geometry, defines the intrinsic properties and runs
a hysteresis loop. Then it analyses the loop and extracts the length of the
linear segment, returning it as the value of the objective function.


.. code-block:: python
   :caption: Content of ``sensor.py``
   :name: sensor-py

   import dakota.interfacing as di
   import discretisedfield as df
   import mammos_analysis as ma
   import mammos_entity as me
   import mammos_units as u
   import micromagneticmodel as mm
   import oommfc as mc


   def optimize(params):
       # extract rhombus axes from parameters dictionary passed by Dakota
       sx, sy = params["cv"]
       # evaluate objective function
       properties = compute_linear_segment_properties(sx, sy)
       # return the maximum field strength in the linear segment
       return {"fns": [properties.Hmax.value]}


   def compute_linear_segment_properties(sx, sy):
       """Compute linear segment for a rhombohedral sensor.

       Parameters ``sx`` and ``sy`` are the lengths of the two
       axes in metre.
       """
       # This function uses Ubermag to perform the micromagnetic
       # simulations and mammos_analysis to extract properties
       # of the linear segment of the hysteresis loop.
       # geometry and mesh
       L = 100e-9  # nm
       t = 5e-9  # nm
       region = df.Region(p1=(-L / 2, -L / 2, -t / 2), p2=(L / 2, L / 2, t / 2))
       mesh = df.Mesh(region=region, n=(40, 40, 1))

       # intrinsic properties
       A = me.A(6e-12, unit="J/m")
       Ms = me.Ms(832, "kA/m")

       # hysteresis loop settings and driver initialization
       hd = mc.HysteresisDriver()
       Hmin = (0, 0, 0)
       Hmax = ((0.1, 500, 0) * u.mT).to("A/m", equivalencies=u.magnetic_flux_field())
       n = 101

       # system
       system = mm.System(name="sensor")
       system.energy = mm.Exchange(A=A.value) + mm.Demag()

       # define diamond mask
       def in_diamond(position):
           x, y, _ = position
           if abs(x) / sx + abs(y) / sy <= 1:
               return Ms.q.to("A/m").value
           else:
               return 0

       # magnetization
       system.m = df.Field(mesh, nvdim=3, value=(1, 0, 0), norm=lambda p: in_diamond(p), valid="norm")

       # run hysteresis loop simulation
       hd.drive(system, Hsteps=[[Hmin, tuple(Hmax.value), n]], verbose=0)

       # read simulation results and extract properties of linear segment
       B_y = system.table.data["By_hysteresis"].values * u.Unit(system.table.units["By_hysteresis"])
       H_y = me.H(B_y.to("A/m", equivalencies=u.magnetic_flux_field()))
       M_y = system.table.data["my"].values * Ms.q
       margin = 0.05 * Ms.q.to("A/m")
       return ma.hysteresis.find_linear_segment(H_y, M_y, margin=margin, min_points=2)


A possible Dakota input file is shown in :ref:`sensor-in`.
We have used the `efficient global optimization method <https://snl-dakota.github.io/docs/6.24.0/users/usingdakota/theory/surrogatebasedglobaloptimization.html#efficient-global-optimization>`__
with 10 initial random samples and fixing the maximum number of iterations to 20.
In the ``variables`` section we define the number of continuous variables, the
initial points and the bounds. The ``interface`` section specifies the
Python function ``sensor.optimize`` (i.e. the function defined in
:ref:`sensor-py`) to be optimized. The last section, ``responses``, includes
information about the number of objective functions and whether we are calculating
the gradients and/or the Hessian. Extensive documentation about all keywords is
available in the `Dakota Keyword Reference <https://snl-dakota.github.io/docs/6.24.0/users/usingdakota/reference.html#>`__.


.. code-block::
   :caption: Content of ``sensor.in``
   :name: sensor-in

   method
     efficient_global
       initial_samples    10
       max_iterations     20

   variables
     continuous_design = 2
       cdv_initial_point  19e-9  39e-9
       cdv_lower_bounds    3e-9   3e-9
       cdv_upper_bounds    7e-8   7e-8
       cdv_descriptor       'sx'  'sy'

   interface
     analysis_driver = 'sensor.optimize'
       python

   responses
     objective_functions = 1
       sense = "maximization"
     no_gradients
     no_hessians


Dakota can then be called on the command line using :code:`dakota -i sensor.in -o sensor.out`.
This will produce the output file ``sensor.out`` and print extra information in the
terminal (and you might want to redirect stdout by adding ``> sensor.stdout`` at the
end of the previous command).

In particular, ``sensor.out`` contains the input file at the top of the file and the
optimization results at the end. This includes information such as which of the
stopping criteria were met, the ``Best objective function`` (the reached
maximum), the ``Best parameters`` (the maximizing couple), and the execution time.
For more information about the output, see the `Dakota Output documentation
<https://snl-dakota.github.io/docs/6.24.0/users/usingdakota/output.html>`__.

.. code-block::
   :caption: Selected output lines from Dakota
   :name: sensor-out

   Dakota version 6.24 released May 15 2026.
   Repository revision 1ab1c9924 (2026-05-11) built Jun  8 2026 15:35:45.
   Running serial Dakota executable in serial mode.
   Start time: Thu Jun 18 10:14:34 2026

   ...

   Stopping criteria not met: distConvergenceCntr (0) < distConvergenceLimit (1)
   Stopping criteria not met: eifConvergenceCntr (0) < eifConvergenceLimit (2)
   Stopping criteria met:     globalIterCount (20) >= maxIterations (20)
   <<<<< Function evaluation summary: 30 total (30 new, 0 duplicate)
   <<<<< Best parameters          =
                         6.9999978988e-08 sx
                         3.0000210121e-09 sy
   <<<<< Best objective function  =
                         3.9788735730e+05
   <<<<< Best evaluation ID: 11


   <<<<< Iterator efficient_global completed.
   <<<<< Environment execution completed.
   DAKOTA execution time in seconds:
     Total CPU        =    19.3955 [parent =    19.3955, child =      6e-06]
     Total wall clock =    87.6421


In :ref:`out-py` we include a Python script to load the optimization information from
the Dakota output into a mammos-yaml file.

.. code-block::
   :caption: Script to store Dakota output into a mammos-yaml file
   :name: out-py

   import mammos_entity as me

   with open("sensor.out") as f:
       lines = f.readlines()
   for i, line in enumerate(lines):
       if "<<<<< Best parameters" in line:
           sx = float(lines[i+1].strip().split()[0])
           sy = float(lines[i+2].strip().split()[0])
       if "<<<<< Best objective function" in line:
           linear_response = float(lines[i+1].strip())

   me.EntityCollection(
       description="Optimized rhomboydal sensor maximizing the linear section of the hysteresis loop.",
       sx=me.Entity("Length", sx, description="optimal sensor x-semiaxis"),
       sy=me.Entity("Length", sy, description="optimal sensor y-semiaxis"),
       linear_response=me.Entity("ExternalMagneticField", linear_response, description="maximum field strength in the linear segment"),
   ).to_yaml("sensor.yaml")


In :ref:`sensor-yaml` we can see the content of the generated file.

.. code-block:: yaml
   :caption: Content of ``sensor.yaml``
   :name: sensor-yaml

   # mammos yaml v2
   metadata: null
   description: Optimization result in order to maximize linear response of rhomboydal
     sensor.
   data:
     sx:
       ontology_label: Length
       description: optimal sensor x-semiaxis
       ontology_iri: https://w3id.org/emmo#EMMO_cd2cd0de_e0cc_4ef1_b27e_2e88db027bac
       unit: m
       value: 6.9999978988e-08
     sy:
       ontology_label: Length
       description: optimal sensor y-semiaxis
       ontology_iri: https://w3id.org/emmo#EMMO_cd2cd0de_e0cc_4ef1_b27e_2e88db027bac
       unit: m
       value: 3.0000210121e-09
     linear_response:
       ontology_label: ExternalMagneticField,
       description: maximum field strength in the linear segment,
       ontology_iri: https://w3id.org/emmo/domain/magnetic-materials#EMMO_da08f0d3-fe19-58bc-8fb6-ecc8992d5eb3
       unit: A / m
       value: 397887.3573


Note that each line in the ``Best parameters`` section in the Dakota
output also contains the name of the corresponding optimized variables,
so that in presence of multiple parameters, the variable extraction in
:ref:`out-py` could be generalized to


.. code-block::

   ...
   out = {}
   for i, line in enumerate(lines):
       if "<<<<< Best parameters" in line:
           n_params = 0
           while "<<<<< Best objective function" not in lines[i+n_params+1]:
               n_params += 1
               par = lines[i+n_params].strip().split()
               out[par[1]] = float(par[0])
           else:
               out["linear_response"] = float(lines[i+n_params+2].strip())

   me.EntityCollection(**out).to_yaml("sensor.yaml")
   ...
