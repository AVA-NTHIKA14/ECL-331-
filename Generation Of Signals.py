#Genaration of unit impulse signal
import numpy as np
import matplotlib.pyplot as plt
N=7
x=np.arange(-N,N+1)
y=np.zeros(len(x))
y[x==0]=1
plt.stem(x,y)
plt.xlabel("n")
plt.ylabel("det(n)")
plt.title("unit impulse signal")

#Generation of unit step signal
import numpy as np
import matplotlib.pyplot as plt
N=7
x=np.arange(-N,N+1)
y=np.zeros(len(x))
y[x>=0]=1
plt.stem(x,y)
plt.xlabel("n")
plt.ylabel("u(n)")
plt.title("unit step signal")

#Generation of Unit ramp
import numpy as np
import matplotlib.pyplot as plt
N=7
x=np.arange(-N,N+1)
y=np.zeros(len(x))
y[x>=0]=x[x>=0]
plt.stem(x,y)
plt.stem(x,y)
plt.xlabel("n")
plt.ylabel("r(n)")
plt.title("Unit ramp signal")

#Generation of Bipolar Signal
import numpy as np
import matplotlib.pyplot as plt
N = 7
x = np.arange(-8,8)
y = np.zeros(len(x))
y[x <=5] = 1
y[x < 0] = -1
y[x<-6]=0
plt.stem(x, y)
plt.xlabel("n")
plt.ylabel("Bipolar Signal")
plt.title("Bipolar Signal using Conditional Indexing")
plt.show()
