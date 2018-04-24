#!/usr/bin/python3
import numpy as np
import os

'''Move the data to respective folders
then run the below file uncomment as appropriate
'''

path = 'j4kdemo/Phone'
#path = 'j4kdemo/Reading'
#path = 'j4kdemo/Drinking'
files = os.listdir(path)


avg_n = 273
data = 0
for file in files:
    print(path + '/' + str(file))
    f = open(path + '/' + file, 'r')
    st = f.read()
    l = st.split(',')
    l.pop()
    n  = int(len(l)/60)
    k = np.array(l, dtype=float)
    k = k.reshape((n,20,3))
    print(k.shape)
    if n < avg_n:
        diff = avg_n - n
        for i in range(diff):
            k = np.vstack((np.array([k[0]]),k))
    else:
        diff = n - avg_n
        k = k[diff:]
        
    if type(data) == int:
        data = np.array([k])
    else:
        #print(data.shape,k.shape)
        data = np.vstack((data,[k]))
    


data.shape


np.save('phone_np',data)
#np.save('reading_np',data)
#np.save('drinking_np',data)

