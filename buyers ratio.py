Name :- Hari singh r
batch id :- DSWDMCOD 25082022 B

import pandas as pd
import scipy as sp
from scipy import stats

#Y is discrete and X Factor is discrete
################ Chi-Square Test ################

ByerRatio=pd.read_csv("D:/assignments of data science/15 hypothesis testing/BuyerRatio.csv")
BuyerRatio

alpha=0.05
Male = [50,142,131,70]
Female=[435,1523,1356,750]
Sales=[Male,Female]
print(Sales)

chiStats = sp.stats.chi2_contingency(Sales)
print('Test t=%f p-value=%f' % (chiStats[0], chiStats[1]))
print('Interpret by p-Value')
if chiStats[1] < 0.05:
  print('we reject null hypothesis')
else:
  print('we accept null hypothesis')
  
#Test t=1.595946 p-value=0.660309
#Interpret by p-Value
#we accept null hypothesis  

#critical value = 0.1
alpha = 0.05
critical_value = sp.stats.chi2.ppf(q = 1 - alpha,df=chiStats[2])

observed_chi_val = chiStats[0]
#if observed chi-square < critical chi-square, then variables are not related
#if observed chi-square > critical chi-square, then variables are not independent (and hence may be related).

print('Interpret by critical value')
if observed_chi_val <= critical_value:
    # observed value is not in critical area therefore we accept null hypothesis
    print ('Null hypothesis cannot be rejected (variables are not related)')
else:
    # observed value is in critical area therefore we reject null hypothesis
    print ('Null hypothesis cannot be excepted (variables are not independent)')

#Interpret by critical value
#Null hypothesis cannot be rejected (variables are not related)
#Inference : proportion of male and female across regions is not same     