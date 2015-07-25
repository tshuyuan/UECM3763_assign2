import pylab as p
import numpy as np


# To define parameters
alpha = 1  
theta = 0.064 
sigma = 0.27 
R_1 = 3
time = 1
n_path = 1000   
n = 1000     

# To generate Brownian motions
dt = time / n
t = p.linspace(0,time,n+1)[:-1]   
dB = p.randn(n_path,n+1) * p.sqrt(dt) ; dB[:,0] = 0
B = dB.cumsum(axis=1)

# To generate R using Euler Method
R = p.zeros_like(B)
R[:,0] = R_1
for col in range(n):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]

# To plot only 5 realisation of R
R_G = R[0:5:,:-1]
p.plot(t,R_G.transpose())
label = 'Time , $t$' ; p.xlabel(label)          
label = '$R_t$' ; p.ylabel(label)
p.title('5 runs of Mean reversal process for $R_t$ with $\\alpha$ = 1, $\\theta$ = 0.064, and $\sigma$ = 0.27\n')
p.show();

# To calculate of P[S(3)>39] and E[S(3)|S(3)>39]
R1 = p.array(R[:,-1])
E_R1 = np.mean(R1)
mask = R1 > 2
P_R1 = sum(mask)/n_path
print('E[R(1)] = ' + str(E_R1))
print('P[R(1)>2] = ' + str(P_R1))