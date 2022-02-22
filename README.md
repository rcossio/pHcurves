Simple script to simulate titration curves of a weak acid and strong one
Equations were derived by hand so only usable in a single de-protonation acid.

Generate with: 

python calc.py > curves.dat

(You can change parameters inside)

A simple gnuplot command will show the plots

gnuplot> p "curves.dat" u 1:2 w lp, "curves.dat" u 1:3 w lp, 4.7

Cheers!
