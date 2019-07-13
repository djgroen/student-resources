
*************************************************************
Advanced use of the Flee code.
*************************************************************

Written by Derek Groen (Derek.Groen@brunel.ac.uk), with help from Hamid Arabnejad, Diana Suleimenova and Gebremariam Assres.

In this 30-minute tutorial, you will learn how to run the parallel version of Flee and how to run a coupled simulation. The content of this tutorial is derived from two conference papers, which are
- ...
- ...

In this tutorial we will cover the following aspects:

- How to run the parallel Flee code using MPI.
- How to run a coupled simulation, with a microscale and macroscale migration model.
- How to run a coupled simulation, with Flee and a conflict evolution model

Because this tutorial is so brief, we will focus primarily on just running basic versions of each type, so that you get a rough idea how these things would work on your local machine.

------------
Requirements
------------

To do this tutorial, you need a working Python3 installation, a working MPI installation, and the MPI4Py library. The numpy, pandas and matplotlib Python3 libraries are also recommended. 

You also need to have Flee installed (http://www.github.com/djgroen/flee-release), as well as Flare (http://www.github.com/djgroen/flare-release).

==============================
Parallel Flee
==============================

The simplest way to run the parallel code is to run it with the `test_par.py` testing script. To run a parallel version of Flee, please:
1. Make sure you've navigated the the Flee installation directory in the terminal.
2. Type `mpirun -np 2 python3 test_par.py 5` to run Flee across 2 cores.
3. To measure the execution time of your run, type `time mpirun -np 2 python3 test_par.py 5` to run Flee across 2 cores.

-----------------
Simple exercises
-----------------

You can change `-np 2` to other values, such as `-np 1` to run on 1 core, or `-np 4` to run on 4 cores.

1. Use the aforementioned time command (see step 3 above) to time 10 runs of Flee using 2 cores. What's the highest time you get? And the lowest?
2. Use the aforementioned time command (see step 3 above) to a run of Flee using 1, 2 and 4 cores. Which core count gives you the lowest execution time?
3. (advanced) Open the test_par.py script. Are you able to change the number of agents in the simulation  by editing this script? If so, how does changing that number affect your performance and scalability?

==============================
Coupled micro-macro
==============================

To run a basic micro-macro coupled model, you can use the test script `mscalecity.py`. Because you are running two models, you'll need to open two terminals for this part.
1. In the first terminal, go to your Flee installation directory, and type `python3 mscalecity.py 0`. This will start a microscale model of a small town.
2. In the second terminal, go to your Flee installation directory, and type `python3 mscalecity.py 1`. This will start a macroscale model of a hypothetical country.

Once you have typed the second command, you should see output being written to the screen for both simulations. You can write output to a CSV file, by appending `> out.csv` to the command described in step 2.

==============================
Coupled Flare-Flee
==============================

