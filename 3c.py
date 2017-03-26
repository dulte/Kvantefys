import numpy as np

psi = 1.0/np.sqrt(5) * np.array([2,1])
d0 = 1.0/(np.sqrt(4-2*np.sqrt(2)))*np.array([-1+np.sqrt(2),1]) #d+
d1 = 1.0/(np.sqrt(4+2*np.sqrt(2)))*np.array([-1-np.sqrt(2),1]) #d-

h0 = np.array([1,0])
h1 = np.array([0,1])

psiToD0 = np.dot(d0,psi)**2
psiToD1 = np.dot(d1,psi)**2

D0ToE0 = np.dot(h0,d0)**2
D0ToE1 = np.dot(h1,d0)**2

D1ToE0 = np.dot(h0,d1)**2
D1ToE1 = np.dot(h1,d1)**2

E0ToD0 = np.dot(d0,h0)**2
E0ToD1 = np.dot(d1,h0)**2

E1ToD0 = np.dot(d0,h1)**2
E1ToD1 = np.dot(d1,h1)**2

P_D0 = psiToD0*(D0ToE0*E0ToD0 + D0ToE1*E1ToD0)
P_D1 = psiToD1*(D1ToE0*E0ToD1 + D1ToE1*E1ToD1)

print P_D0
print E0ToD0, D0ToE0
