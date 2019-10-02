=====================
Demo for using COBalD
=====================

Toy demo showing how the ``cobald`` daemon predicts resources required for unknown demand.
It implements a dummy pool which tracks your CPU usage, and exposes its utilisation compared to a faked demand.
This is visualised as a simple ASCII art on your terminal:

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
Install it in a ``venv`` to isolate the demo:

.. code:: bash

    python3 -m venv /tmp/cobalddemo/venv/ --clear
    cd /tmp/cobalddemo/
    git clone https://github.com/MaineKuehn/cobald_demo.git
    source venv/bin/activate
    python3 -m pip install --editable cobald_demo

After installation, you can run the demo with one of the two example configuration files:

.. code:: bash

    python3 -m cobald.daemon cobald_demo/demo_config.yaml
    python3 -m cobald.daemon cobald_demo/demo_config.py

Looking around
--------------

If you just want to use ``cobald`` with existing components, check out the configuration files.
The ``demo_config.yaml`` uses a simple but limited format,
while the ``demo_config.py`` provides a complex but extensible approach.

If you want to write your own resource pool, check out the ``cobald_demo/cpu_pool.py`` implementation.
While it is a mockup, it shows how little is needed to hook into the ``cobald`` machinery.
