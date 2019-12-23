import os.path
import numpy as np
import scipy.io as sio
from scipy import signal
import matplotlib.pyplot as plt


##slice_filename = 'spectr50ms.mat'
##sign = sio.loadmat(slice_filename).get('data')[0]
##
filename='33484K-LFS'  #выбрали, какой файл читать

m = sio.loadmat(filename + '.mat')#открыли файлик

skl_arr = m.get('sigKL')#считали сигнал
sign = np.array(list(map(lambda x: x[0], skl_arr))) #преобразовали двумерный массив сигналов, в котором каждое значение записано в нулевой элемент нового массива в одномерный массив

fn=2e6
#plt.plot(sign)
a=fn*5/1000
print(a)
otklonenie=[]
srznach=[]
for i in range(0,int(len(sign)/a)):
    #print(i)
    b=sign[int(a*i):int(a*(i+1))]
    print(np.std(b))
    otklonenie.append(np.std(b))
#    np.append(otklonenie,[np.std(b)])
#    print(otklonenie)
    srznach.append(np.mean(b))
#    np.append(srznach,[np.std(b)])

print(otklonenie)
print(srznach)
otklonenie=np.array(otklonenie)
srznach=np.array(srznach)
plt.subplot(211)
plt.plot(otklonenie)
plt.subplot(212)
plt.plot(srznach)

plt.show()   
