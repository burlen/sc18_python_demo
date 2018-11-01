SC18 Tutorial Demos
===================

Tightly couled / in situ
------------------------
These are stand alone, they run the simulation tighlty coupled to a back end.
The back end is selected vi an XML file passed into the bridge during start up.
Hence the major difference between these is that XML file.

1. `oscillator_catalyst.sh` -- renders data using Catalyst
2. `oscillator_libsim.sh` -- renders data using Libsim
3. `oscillator_posthoc_paraview.sh` -- writes VTK files in ParaView PVD format.
4. `oscillator_posthoc_visit.sh` -- writes VTK files in VisIt .visit format.
5. `oscillator_python.sh` -- processes data using Python

Loosely coupled / in transit
----------------------------
These require two mpiexec commands. The first runs the simulation configured to
send data through ADIOS. The second job runs the end point configured to
receive data from the simulation and push it to one of the back ends. The back
end is selected via an XML file passed into the end point during start up.
Hence the major diffence between these is that XML file. We used the same
XML file in the end-point as in the tightly coupled demos.

### Simulation
1. `oscillator_adios.sh` -- sends data through an ADIOS writer

### End point
1. `adios_endpoint_catalyst.sh` -- renders incoming data using Catalyst
2. `adios_endpoint_libsim.sh` -- renders incoming data using Libsim
3. `adios_endpoint_python.sh` -- processes incoming data using Python

Other
-----
clean.sh -- a script to remove output files

