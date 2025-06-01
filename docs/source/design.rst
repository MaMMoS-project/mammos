======
Design
======

We use pseudocode below (i.e. not correct Python syntax) to illustrate the
motivation behind our design. This does not execute and is just used to explain
the approach from a high level perspective combined with a more concrete
example.

FAIR data requirements
----------------------

In the context of open science, it is essential that numerical values in data
are consistently associated both (i) units and (ii) ontology labels

We use the term `quantity` to refer to a value (such as a number) and associated units.

We understand 'entity' as a data point with units that has a label from an
ontology, such as the EMMO.

Units ensure that measurements are interpretable and comparable across datasets,
avoiding ambiguity about scale or dimension. Entities---through they 
ontology-based labels---provide precise semantic definitions for the quantities
being measured, ensuring clarity about what a number actually represents.

Together, units and entities make data more Findable, Accessible, Interoperable,
and Reusable by enabling machines and researchers alike to interpret and
integrate data correctly across disciplines and domains.

Strict approach
---------------

To make this more concrete: let's consider an example. we measure spontaneous magnetization in units of
Ampere per metre, and imagine that Ms = 10e5 A/m. If we wanted to be absolutely
clear what we talk about, we could refer to our entity as a triplet::

    (SpontaneousMagnetization, 10e5, A/m)

Or imagine a part of MaMMoS software returns to us a function ``f`` (perhaps from the Kuzmin equation) that
returns the exchange coupling constant as a function of temperature. Assuming it
is called ``f(T)`` and takes a temperature ``T``, and we want to evaluate it at a temperature of 100::

Option 1: just the number
~~~~~~~~~~~~~~~~~~~~~~~~~

    >>> f(100)

We should say what we mean with 100: if we talk about temperature, it could be
100 Kelvin or 100 degree Celsius for example. Using ``mammos_units``, we can be precise:

Option 2: number and units (=quantity)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    >>> import mammos_units as u
    >>> f(100*u.K)   # u.K represents the Unit Kelvin  

The function ``f`` can now check the units of the argument, and complain if
Kelvin is not what was expected.

We could also provide the ontology label for the temperature: this provides a
more precise semantic definition of the argument, and also avoids
misunderstandings (using kB*T one could express energy in units of temperature
T, but that's not what we mean here).

Option 3: number, units and ontology label (=entity)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To be as precise as possible, we need to use the ontology label. Using ``mammos_entity``, we can write

    >>> import mammos_entity as me
    >>> f(me.entity("ThermodynamicTemperature", 100, "K"))

or, as an equivalent abbreviation for this:

    >>> import mammos_entity as me
    >>> f(me.T(100, "K"))

With the ontology label, the function ``f`` can now check if that is the
expected entity and complain if this is not the case.

Practicality
------------

Option 3 is the best in terms of precision and clarity, and the best for
interoperability and re-usability of data and software. However, it does require
some additional effort to specify the units and the type of, in this example,
the temperature.

Once a scientist has used the function ``f`` a few times, they may feel very
confident that the input argument meant to be the thermodynamic temperature, and
that of course the function expects input in SI units (i.e. Kelvin). Given that
knowledge, the scientist may much prefer option 1.

We argue that a syntax like option 1 is useful to support as for some scientists
it would be a game changer (and stop them from using the MaMMoS software).

Design principles
-----------------

To balance the benefits of a complete specification (option 3) with the
convenience of being able to just use a number (option 1), we have developed the
following principles within the `mammos_*` packages:

Functions returning data:

- XXX, to be continued. Perhaps a notebook would be better here?
