import scipy.io as sio
from scipy import signal
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

filename='33484K-LFS'  #выбрали, какой файл читать

m = sio.loadmat(filename + '.mat')#открыли файлик
print (spec) #посмотреть, что мы вообще такое открыли

skl_arr = m.get('sigKL')#считали сигнал
sign = np.array(list(map(lambda x: x[0], skl_arr))) #преобразовали двумерный массив сигналов, в котором каждое значение записано в нулевой элемент нового массива в одномерный массив

time = m.get('tbKL')[0]#считали время, весь сигнал содержится в нулевом элементе массива

timename='tbKL'
signame='sigKL'

fs=1/(time[1]-time[0])  # определяем частоту дискретизации
fs=round(fs)  # округляем частоту дискретизации

f, t,Sxx = signal.spectrogram(sign, fs)   #получаем исходную спектрограмму
plt.pcolormesh(t, f, np.log(Sxx))
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.axis([t.min(),t.max(), 0, 3e5])
plt.savefig(filename+'spectrogram')
plt.show()


# b, a = signal.ellip(4, 0.1,30, 0.0001)    # фильтруем сигнал
# scipy.signal.filtfilt(b, a, x, axis=-1, padtype='odd', padlen=None, method='pad', irlen=None)
# scipy.signal.ellip(N, rp, rs, Wn, btype='low', analog=False, output='ba')
fc = 3e5 #граничная частота
w = fc/(fs/2) 
w = fc/(fs/2) 
b, a = signal.butter(5, w, 'low') # строим фильтр для того, чтобы оставить частоты ниже заданной
output = signal.filtfilt(b, a, sign)# применяем фильтр для того, чтобы оставить частоты ниже заданной

plt.plot(time,output)
plt.plot(time,fgust, 'r-')
plt.plot([], [], ' ', label='RMS=%.2f' %(np.sqrt(np.mean((fgust-sign)**2))))
plt.axis([time.min(),time.max(), fgust.min()*1.5, fgust.max()])
plt.savefig(filename+'filtered')
plt.show()

f1, t1, Sxx1 = signal.spectrogram(fgust,fs)  # делаем спектрограмму отфильтрованного сигнала
plt.pcolormesh(t1, f1, np.log10 (Sxx1))
plt.ylabel('Frequency [kHz]')
plt.xlabel('Time [sec]')
plt.axis([t.min(),t.max(), 0, 3e5])
plt.savefig(filename+'filtered spectrogram')
plt.show()
 
