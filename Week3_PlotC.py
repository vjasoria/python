

from matplotlib.pyplot import *
from numpy import *
import copy

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

Y_t = copy.copy(y)
Y_t[Y_t>0.5] = 0.5
Y_t[Y_t<-0.5] = -0.5
		

figure(1)
clf()
plot(t,y, 'r--')
plot(t,Y_t)

title("Jasoria-Plot")
xlabel("Time(Sec.)")
ylabel("Y(t)")

show()
