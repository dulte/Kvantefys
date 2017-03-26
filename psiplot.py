import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,1000)

V_0 = 1
E = 0.66
k = np.sqrt(2*E)

psi1 = (k*(1j*V_0+k)*np.exp(1j*k*x) - 1j*k*V_0*np.exp(2*1j*k)*np.exp(-1j*k*x))/(2*1j*V_0*k + k**2 +V_0**2*np.exp(4*1j*k) - V_0**2)

E = 3.25
k = np.sqrt(2*E)

psi2 = (k*(1j*V_0+k)*np.exp(1j*k*x) - 1j*k*V_0*np.exp(2*1j*k)*np.exp(-1j*k*x))/(2*1j*V_0*k + k**2 +V_0**2*np.exp(4*1j*k) - V_0**2)

E = 8.22
k = np.sqrt(2*E)

psi3 = (k*(1j*V_0+k)*np.exp(1j*k*x) - 1j*k*V_0*np.exp(2*1j*k)*np.exp(-1j*k*x))/(2*1j*V_0*k + k**2 +V_0**2*np.exp(4*1j*k) - V_0**2)


plt.plot(x,np.conj(psi1)*psi1)
plt.plot(x,np.conj(psi2)*psi2)
plt.plot(x,np.conj(psi3)*psi3)
plt.title("$|\psi|^2$ i omraade II")
plt.xlabel("x")
plt.ylabel("$|\psi|^2$")
plt.legend(["E = 0.66","E=3.25","E=8.22"])
plt.show()
