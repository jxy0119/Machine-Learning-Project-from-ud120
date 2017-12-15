#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    err =[]
    b_new=[]
    c_new=[]
    cleaned_data = []
    temp = ()
    ### your code goes here
    a = np.array(predictions).tolist()
    c = np.array(net_worths).tolist()
    b = np.array(ages).tolist()
    #d = c[0][0]-a[0][0]
    #d1 = c[1][0]-a[1][0]
    #d2 = c[2][0]-a[2][0]
    #print a
    #print b
    #print c[0]
    for i in range(0,90):
        b_new.append(b[i][0])
        c_new.append(c[i][0])
        e = c[i][0]-a[i][0]
        err.append(e)
    cleaned_data = zip(b_new, c_new, err)
    print cleaned_data
    m = cleaned_data[0][2]
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])

   # for j in range(0,90):
    #    for k in range(j+1,90):
     #       if cleaned_data[k-1][2] > cleaned_data[k][2]:
      #          temp = data[k]
       #         cleaned_data[k] = cleaned_data[k-1]
        #        cleaned_data[k-1]= temp


    del cleaned_data[0:9]
    return cleaned_data

