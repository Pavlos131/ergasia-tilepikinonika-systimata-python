import numpy as np 
from scipy.special import erfinv
import matplotlib.pyplot as plt
def snr_db(M, Pe):
  
    #adistrofi tis q
    Q_inv = lambda y: np.sqrt(2) * erfinv(1 - 2 * y)

   
    SNR_b = ((M**2 - 1) / (6 * np.log2(M))) * (Q_inv(Pe * M * np.log2(M) / (2 * (M - 1))))**2

    # metattopi se db 
    SNR_db = 10 * np.log10(SNR_b)

    return SNR_db



#-4-2=-6
pb = 10**-6

m_values = np.arange(1, 11)
# 2^M
M_values = 2**m_values

SNR_values = [snr_db(M, pb) for M in M_values]
 
plt.figure(figsize=(10, 6))
plt.plot(M_values, SNR_values, marker='o')
plt.xlabel('2^M')
plt.ylabel('SNR')
plt.grid(True)
plt.xscale('log', basex=2)  
plt.xticks(M_values, labels=[f"2^{m}" for m in m_values])  
plt.show()

