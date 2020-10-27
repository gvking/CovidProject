import numpy as np
x = np.load('/Users/vikrampasupathy/Desktop/CS1/part1a.npz')
#for k in x.iterkeys():
    ##print k
beta = 0.5
N = x['N']
#print(x['N'])
print(x['Svc_0_pmf'])
#print(x['Lc'])
#print(x['Ic_0'])
#print(x['gamma'])
gamma = x['gamma']
IArray = [x[Ic_0]]
LArray = [[0,0,0,0]]
SVC = x['Svc_0_pmf']
derivativeSVCdTArray = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
for days in range(0,120):
    #simulation for the day ^
    for c in range(0,3):
        #looping through the vulnerability groups  
        for v in range(0,3):
            # looping through the comorbidity groups
            derivativeOfSVCdT = -1*beta*SVC[v][c] * np.sum(IArray[days])
            derivativeOfSVCdT = derivativeOfSVCdT/ N
            derivativeSVCdTArray[c][v] = derivativeOfSVCdT
        
        dIcit = -1*np.sum(derivativeSVCdTArray[c]) - gamma * IArray[days][c]
        dRdt = gamma* np.sum(IArray[days])
            



# def becomesInfected(result, gamma, Ic):

# def recoveryRate(Itotal, gamma):

# def loadDensity(LcPrev, IcArray):


