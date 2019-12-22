import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plot

# делаю на основе примера, но честно пытаюсь понять
# Возьмем массив частот по аналогии с примером, но случайным образом
# на всякий случай: np.random.randint(минимум, максимум, количество элементов)
print ('Я немного глючная прога и сейчас я сгенерирую вам спектр')
print ('Введите минимальное значение диапазона частот (и не путайте меня, пусть оно будет неотрицательно)')
min_freq=int(input())
print ('Введите максимальное значение диапазона частот (оно должно быть больше минимального)')
max_freq=int(input())
print ('Введите количество частот, которые будут в спектре')
number_of_freq=int(input())
frequencies = np.random.randint(min_freq, max_freq, number_of_freq)
print (frequencies)

# Sampling Frequency
# частота дискретизации должна быть больше частоты сигнала, чтобы было адекватно, поэтому пусть так
samplingFrequency   = max_freq * 3
 
# здесь создаются массивы, в которые будет записан сигнал, тут менять нечего, пусть живет как в примере
# Create two ndarrays
s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For signal

# Start Value of the sample
start   = 1
# Stop Value of the sample
stop    = samplingFrequency+1

#для всех частот в массиве частот
for frequency in frequencies:
# напоминалка для себя: numpy.arange(начало, конец, шаг, тип данных)
    sub1 = np.arange(start, stop, 1)
    # генерация синусоидального сигнала с шумом и с заданной частотой
    # Signal - Sine wave with varying frequency + Noise
    # Шум сделан с помощью numpy.random.randn(d0, d1, ..., dn), 
    # которая здает массив указанной формы (если аргумент один, 
    # как тут, то линейный массив заданной длинны)
    # и заполняет его случайными числами с плавающей точкой, 
    # которые выбраны из одномерного нормальногораспределения со средним значением равным 0
    # и дисперсией равной 1
    sub2 = np.sin(2*np.pi*sub1*frequency*1/samplingFrequency)+np.random.randn(len(sub1))
# добавляем в спектр то, что сгенерировали только что

    s1      = np.append(s1, sub1)
    s2      = np.append(s2, sub2)
# шоб я ещё понимала, чем являются эти старт и стоп... 
# тут изменение их значений, вроде, надо, чтобы
# на следующем шаге в s1 и s2 удобнее было добавлять нужные значения
    start   = stop+1
    stop    = start+samplingFrequency

print ('Секундочку, сейчас я это построю...')
# а тут всё это строится
# Plot the signal
# зачем я крашу график, на котором рисую сигнал? потому что могу! 
# Потому что нашла эту фичу, пока гуглила, как работает subplot
# Кстати, если вам интересно, как называются разные цвета на графиках, то информация об этом есть 
# тут https://undoshutdown.blogspot.com/2018/06/matplotlib-python.html

plot.subplot(211, facecolor='ivory')
plot.plot(s1,s2)
plot.xlabel('Номер измерения')
plot.ylabel('Амплитуда')

# Plot the spectrogram
plot.subplot(212)
# а вот сейчас я не понимать, почему они много разных переменных приравняли к одной штуковине, но оно же работает...
powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(s2, Fs=samplingFrequency)

plot.xlabel('Время')
plot.ylabel('Частота')

 
plot.show()   
