import numpy as np

#Weak Acid (Acetic acid)
Ka=1.8e-5
V1=1.0 #L
c1=0.1 #M
n1=c1/V1 #mol
c2=1.0#M (NaOH) 

#Strong Acid (HCl)
V1Cl=1.0#L
c1Cl=0.1
nCl0=c1Cl/V1Cl
Kw=1e-14

x=0.0
for i in range(800):
    # Next equations asume 
    # AcH + OH- --> Ac- + H2O
    # AcH <--> Ac- + H+
    # But no consideration on Kw
    n2=x #mols for calculation
    V2=n2/c2  #volume for plot
    nH= (1/2.0)*(-(n2+Ka)+np.sqrt( (n2+Ka)**2-4.0*Ka*(n2-n1) ))
    pH=-np.log10(nH/(V1+V2))
    
    # Next equation considers
    # H+ + OH- <--> H2O
    nHCl = nCl0-(1/2)* (nCl0+n2)+np.sqrt( (nCl0+n2)**2-4*(nCl0*n2-Kw)  )
    pHCl=-np.log10(nHCl/(V1Cl+V2))

    # I make dots approach the total H+ content in weak acid (as H+ or AcH)
    x=x+(n1-x)*0.02

    print(V2,pH,pHCl)


