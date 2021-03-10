import matplotlib.pyplot as plt                 # Для створення та відображення графіків
from signalGenerator import generateRandomSignal
from fourie import dft_f, fft_f

n = 8                                           # Число гармонік в сигналі
W = 2000                                        # Гранична частота
N = 256                                         # Кількість дискретних відліків

randomSignal = generateRandomSignal(n, W, N)
time = range(N)

fig1, plot1 = plt.subplots()
plot1.plot(randomSignal)
plot1.set(xlabel='time', ylabel='randomSignal', title='Випадково згенерований сигнал')
fig1.savefig("randomSignal.png")

fig2, plot2 = plt.subplots()
plot2.plot(dft_f(randomSignal))
plot2.set_xlim(0, int(N/4))
plot2.set(xlabel='time', ylabel='randomSignal', title='Дискретне перетворення Фур`є')
fig2.savefig("dft.png")

fig3, plot3 = plt.subplots()
plot3.plot(fft_f(randomSignal))
plot3.set_xlim(0, int(N/4))
plot3.set(xlabel='time', ylabel='randomSignal', title='Швидке перетворення Фур`є')
fig3.savefig("fft.png")









