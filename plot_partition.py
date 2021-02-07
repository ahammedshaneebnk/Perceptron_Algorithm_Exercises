# solution to exercise 1

import numpy as np
import matplotlib.pyplot as plt

# weights and bias
w1, w2, w0 = 1, 1, 2
x1_start = -6
x1_end = 6
x1_count = 100
x1 = np.linspace(x1_start, x1_end, x1_count)
x2 = -(w0/w2) - (w1*x1/w2)

# line plot
plt.plot(x1, x2, color='b', linewidth=3)
plt.grid(True, color='k')
x_axis_min = -6
x_axis_max = 6
y_axis_min = -6
y_axis_max = 6
plt.axis([x_axis_min, x_axis_max, y_axis_min, y_axis_max])
plt.axhline(0, color='k')
plt.axvline(0, color='k')
plt.fill_between(x1, x2, y_axis_max, color='r', alpha=0.5)
plt.xlabel('<--x1-->')
plt.ylabel('<--x2-->')
plt.legend(['x1 + x2 + 2 = 0'])
plt.gca().set_aspect('equal')

plt.show()
