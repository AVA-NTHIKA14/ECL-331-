#1
import numpy as np
#import matplotlib.pyplot as plt
def get_DFT_matrix(N):
    k=n=np.arange(0,N)
    mat=np.outer(n,k)
    w=np.exp(-1j*2*np.pi/N)
    W=np.power(w,mat)
    W=np.round(W,decimals=0)
    return W
N=4
W=get_DFT_matrix(N)
x=np.ones(N)
X=np.matmul(W,x)

print(X)
#R=np.real(W)
#Imag=np.imag(W)
#plt.matshow(R)
#plt.title('Real part of DFT')
#plt.matshow(Imag)
#plt.title('Imaginary Part Of DFT')

#2
import numpy as np
def get_DFT_matrix(N):
    w=np.exp(-1j*2*np.pi/N)
    n=k=np.arange(0,N)
    mat=np.outer(n,k)
    W=np.power(w,mat)
    W=np.round(W,decimals=0)
    return W
N=16
W=get_DFT_matrix(N)
x=np.zeros(N)
X=np.matmul(W,x)
print(X)


#3
import numpy as np
import matplotlib.pyplot as plt
def get_DFT_matrix(N):
    w=np.exp(-1j*2*np.pi/N)
    n=k=np.arange(0,N)
    mat=np.outer(n,k)
    W=np.power(w,mat)
    return W
N=16
W=get_DFT_matrix(N)
R=np.real(W)
plt.matshow(R)
plt.title('REAL')
I=np.imag(W)
plt.matshow(I)
plt.title('IMAG')

#4
import numpy as np
def get_DFT_matrix(N):
    w=np.exp(-1j*2*np.pi/N)
    n=k=np.arange(0,N)
    mat=np.outer(n,k)
    W=np.power(w,mat)
    W=np.round(W,decimals=0)
    return W
N=4
W=get_DFT_matrix(N)
print(W)
x=[1,2,3,4]
X=np.matmul(W,x)
print(X)
  
