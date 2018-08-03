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



.. code:: bash

    python3 -m pip install cobald_demo
    python3 -m cobald.daemon demo_config.yaml
