import numpy as np
def fshoot (x):
    k0, c0 = x
    k1 = A*k0**(alfa)-c0+(1-delta)*k0
    c1 = c0*(beta*(1+(1-tau)*(alfa*A*k1**(alfa-1))-delta))**(1/sigma)
    return [k1,c1]
alfa, delta, sigma, beta, A, tau= 0.4, 0.08, 2, 0.98, 1, 0.1
kss = ((1/beta-1+delta)/(alfa*A))**(1/(alfa-1))
css = A*kss**alfa-delta*kss
kss1 = ((1/beta-1+delta)/((1-tau)*alfa*A))**(1/(alfa-1))
css1 = A*kss1**(alfa)-delta*kss1
k0=kss
c0 = css + 0.1
epsil, cmax, cmin = 0.00001, A*(kss)**(alfa), css
k = []
k.append(k0)
   
while abs(k[-1]-kss1)>epsil:
    k, c = ([] for i in range(2))   
    k.append(kss)
    c.append(c0)
    d = (k[-1], c[-1])
    new = fshoot(d)
    k.append(new[0])
    c.append(new[1])
    
    
    while c[-1]<c[-2] and k[-1]<k[-2]:
        d = [k[-1], c[-1]]
        new = fshoot(d)
        k.append(new[0])
        c.append(new[1])
    if c[-1]>c[-2]:
        cmax= c0
        c0 = (cmin+cmax)/2
    if k[-1]>k[-2]:
        cmin = c0
        c0 = (cmin+cmax)/2
print(k)
print(c)
def utilidad(u):
     return ((u**(1-sigma)-1)/(1-sigma))
uss0 = utilidad(css)
ut0 = uss0/(1-beta)
uss1 = utilidad(css1)
ut1 = uss1/(1-beta)
ut1 = ut0 - 1
gamma = 0.001
while ut1 < ut0:
    util1 = 0
    for i in range(len(c)):
        util1 =util1 + (beta**i)*utilidad(c[i]*(1+gamma))
    ut1= util1 + beta**len(c)*utilidad(css1*(1+gamma))/(1-beta)
    gamma = gamma +0.00001
print(gamma)
