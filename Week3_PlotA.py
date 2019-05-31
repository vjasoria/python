from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

Y_t = zeros(len(y))

for i in range(len(y)):
	if y[i] > 0.5:
		Y_t[i] = 0.5
	elif y[i] < -0.5:
		Y_t[i] = -0.5
	else:
		Y_t[i] = y[i]
		

figure(1)
clf()
plot(t,y, 'r--')
plot(t,Y_t)

title("Jasoria-Plot")
xlabel("Time(Sec.)")
ylabel("Y(t)")

show()
