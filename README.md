# Muon-Properties

--Program that calculates the invariant mass and four vector of muons--

The text file contains data from simulated particle collisions. The collisions contain two muons. What we'd like to know is whether the muons appear to have come from the decay of a heavy particle or not. To do that, we try to calculate the "invariant mass" of the hypothetical particle that it may have decayed from. If we see many events with the same invariant mass, then we think that a particle at that mass might exist.

Here's the math:

For a muon, we measure \
"pt", Transverse momentum = sqrt (px^2 + py^2) \
"phi",   angle in the x-y plane \
"eta", pseudorapidity, which is another form of the angle from the z-axis \
see:   http://en.wikipedia.org/wiki/Pseudorapidity \
"mass", the mass of the muon. 

If you know these 4 quantities, you can use trigonometry to calculate the x,y,z components of the momentum, as well as the total energy:

E = sqrt ( mass^2 + momentum^2)

Together, the momentum+energy are a 4-vector or "Lorentz vector"
see:  http://en.wikipedia.org/wiki/Four-momentum

To calculate the invariant mass of the hypothetical particle from the components, use:

see: http://en.wikipedia.org/wiki/Invariant_mass

The program should be able to read in the attached file and for each event: \
i) calculate the 4-vector for each muon \
ii) calculate the invariant mass of the hypothetical particle \
iii) writes that mass to another file

The input file and the details should be of this format below:

Format: event event is 4 lines: \
Line 1: a unique identifier for each event \
Line 2: ignore for now \
Line 3: Data for muon 1, pt,eta, phi and mass.   ignore the "dptinv" for now \
Line 3: Data for muon 2, pt,eta, phi and mass.   ignore the "dptinv" for now
