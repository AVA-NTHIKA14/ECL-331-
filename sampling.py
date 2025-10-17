import numpy as np
import matplotlib.pyplot as plt
def get_DFT_matrix(N):
    w=np.exp(-1j*2*np.pi/N)
    n=k=np.arange(0,N)
    mat=np.outer(n,k)
    W=np.power(w,mat)
    return W

A=1
f=1000
phi=0
N=8
Fs=N*f
Ts=1/Fs
n=np.arange(N)
t=n*Ts
x=A*np.sin(2*np.pi*f*t+phi)
plt.subplots(2,1)
plt.subplot(2,1,1)
plt.stem(n,x)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title('Discrete samples of sine signal')

W=get_DFT_matrix(N)
X=np.matmul(W,x)
plt.subplot(2,1,2)
plt.stem(n,np.abs(X))
plt.xlabel("k")
plt.ylabel("Magnitude")
plt.title("Magnitude plot of DFT of sine signal")
plt.subplots_adjust(hspace=0.95)
