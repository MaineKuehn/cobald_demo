=====================
Demo for using COBalD
=====================

Toy demo showing how the ``cobald`` daemon predicts resources required for unknown demand.
It implements a dummy pool which tracks your CPU usage, and exposes its utilisation compared to a faked demand.
This is visualised as a simple ASCII art on your terminal.

.. code:: bash

    [-----------------------------------^----------------------------v-----------------------------------]
    [------------------------------------^-----v---------------------------------------------------------]
    [------------------------------v-----^---------------------------------------------------------------]
    [-------------------------------------^------------v-------------------------------------------------]
    [----------------v--------------------^--------------------------------------------------------------]
    [-----------------v------------------^---------------------------------------------------------------]
    [-------------v----------------------^---------------------------------------------------------------]
                  | cpu usage            | target demand

Usage
-----

You can pull in the entire demo and its dependencies using ``git`` and ``pip``.
After installation, you can run it with one of the two example configuration files:

.. code:: bash

    git clone https://github.com/MaineKuehn/cobald_demo.git
    pip install --editable . --user
    python3 -m cobald.daemon demo_config.yaml

Looking around
--------------

If you just want to use ``cobald`` with existing components, check out the configuration files.
The ``demo_config.yaml`` uses a simple but limited format,
while the ``demo_config.py`` provides a complex but extensible approach.

If you want to write your own resource pool, check out the ``cobald_demo/cpu_pool.py`` implementation.
While it is a mockup, it shows how little is needed to hook into the ``cobald`` machinery.
