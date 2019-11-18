import numpy as np
for i in np.arange(0.0,1.0+1/12,1/12):
    print(i)

x=[np.log(i+1)/(1+i**2) for i in np.arange(0.0,1.0+1/12,1/12)]

#print(x)
y=[]
for i in range(1,len(x),2):
    z=x[i-1]+4*x[i]+x[i+1]
    y.append(z)
print(y)
print(sum(y)/36)


