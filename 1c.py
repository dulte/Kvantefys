import numpy as np
import matplotlib.pyplot as plt

V_0 = 1.
E = 1.
q_0 = 1.

E = np.linspace(0,10,1000)


kappa = np.sqrt(2*E)/V_0
k = np.sqrt(2*E)

T1 = kappa**2/(1+kappa**2)

T2 = k**4/(4*k*V_0**3*np.sin(4*k*q_0) + 2*V_0**2*np.cos(4*k*q_0)*(k**2 - V_0**2) + k**4 + 2*k**2*V_0**2 + 2*V_0**4)


plt.plot(E,T1)
plt.plot(E,T2)
plt.title("Transmittert Fluks for $V_0 = q_0 = 1$")
plt.legend(["$\delta$-potensial", "Dobbelt $\delta$-potensial"], loc = 4)
plt.xlabel("$E$")
plt.ylabel("T")
plt.show()
