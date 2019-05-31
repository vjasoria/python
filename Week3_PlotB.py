from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

Y_t = zeros(len(y))

for i, item in enumerate(y):
	if item > 0.5:
		Y_t[i] = 0.5
	elif item < -0.5:
		Y_t[i] = -0.5
	else:
		Y_t[i] = item
		

figure(1)
clf()
plot(t,y, 'r--')
plot(t,Y_t)

title("Jasoria-Plot")
xlabel("Time(Sec.)")
ylabel("Y(t)")

show()
