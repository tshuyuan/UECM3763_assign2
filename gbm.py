import pylab as p
import numpy as np

# Define parameters
mu = 0.1
sigma = 0.26
S0 = 39
n_path = 1000
n = n_partitions = 1000
period = 3

# Find theoritical expectation and variance
T_E = S0 * p.exp(mu*period)
T_Var = (S0**2)*(np.exp(2*mu*period))*(np.exp(sigma*sigma*period)-1)
print(' ')
print('dS(t) = 0.1dt + 0.26dB(t); S(0) = 39')
print('The theoritical expectation and variance:')
print('E(S(3) = ' + str(T_E))
print('Var(S(3)) = ' + str(T_Var))

# Create Brownian paths
t = p.linspace(0,period,n+1);
dB = p.randn(n_path,n+1)/p.sqrt(n/period);dB[:,0]=0;
B = dB.cumsum(axis=1);

# Find stock prices
nu = mu-sigma*sigma/2.0
St = p.zeros_like(B);St[:,0]=S0
St[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:])

# Plot 5 realizations of the GBM
S = St[0:5]
label = 'Time , $t$' ; p.xlabel(label)
label = 'Stock prices, $S$' ; p.ylabel(label)
p.title('5 runs of GBM for Stock prices with $\mu$ = 0.1 and $\sigma$ = 0.26\n')
p.plot(t,S.transpose());
p.show();

# Calculate the E(S(3)) and Var(S(3))
ST_3 = np.array(St[:,-1])
E_ST_3 = np.mean(ST_3)
Var_ST_3 = np.var(ST_3)
print('E(S3) = ' + str(E_ST_3))
print('Var(S3) = ' + str(Var_ST_3))

# Find P[S(3)>39] and E[S(3)|S(3)>39]
count = ST_3 > 39
P_S3_39 = (sum(count)/len(ST_3))
C_E = ST_3 > 39 
S3_39 = ST_3 * C_E               
E_S3_39 = sum(S3_39) / sum(C_E)
print('P(S3>39) = '+str(P_S3_39))
print('E(S3|S3>39) = ' + str(E_S3_39))