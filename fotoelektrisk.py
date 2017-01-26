import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

c = 299792458
e = 1.60217662e-19

lamb = np.array([2.536,3.132,3.65,4.047])*1e-7
V0 = np.array([1.95,0.98,0.5,.14])

nu = c/lamb
kmax = V0

slope, intercept, r_value, p_value, std_err = stats.linregress(nu,kmax)
print "%g x + %g" %(slope, intercept)

plt.title(r"$K_{max}$ mot $\nu$")
plt.xlabel(r"$\nu$")
plt.ylabel("$K_{max}$")
plt.plot(nu,kmax)
plt.show()
