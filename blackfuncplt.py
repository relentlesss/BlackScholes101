from scipy.stats import norm
from matplotlib import pyplot as plt
import numpy as np
from blackfunc import *

# plot call price vs. stock price
def call_s_des(s, k, t, r, d, v, c=1, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(s,s+c*(n),c)

    y = []
    for i in range(n):
        y.append(call_bs(s+c*i, k, t, r, d, v))

    plt.plot(x,y)
    plt.title('Call price vs. Stock price')
    plt.xlabel('stock price')
    plt.ylabel('call price')
    plt.show()

# plot call price vs. strike price
def call_k_des(s, k, t, r, d, v, c=0.03, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(k,k+c*(n),c)

    y = []
    for i in range(n):
        y.append(call_bs(s, k+c*i, t, r, d, v))

    plt.plot(x,y)
    plt.title('Call price vs. Strike price')
    plt.xlabel('strike price')
    plt.ylabel('call price')
    plt.show()

# plot call price vs. time to maturity
def call_t_des(s, k, t, r, d, v, c=0.5, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(t,t+c*(n),c)

    y = []
    for i in range(n):
        y.append(call_bs(s, k, t+c*i, r, d, v))

    plt.plot(x,y)
    plt.title('Call price vs. Time to maturity')
    plt.xlabel('time to maturity')
    plt.ylabel('call price')
    plt.show()

# plot call price vs. risk-free rate
def call_r_des(s, k, t, r, d, v, c=0.0002, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(r,r+c*(n),c)

    y = []
    for i in range(n):
        y.append(call_bs(s, k, t, r+c*i, d, v))

    plt.plot(x,y)
    plt.title('Call price vs. Risk-free rate')
    plt.xlabel('risk-free rate')
    plt.ylabel('call price')
    plt.show()

# plot call price vs. dividend yiel
def call_d_des(s, k, t, r, d, v, c=0.0001, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(d,d+c*(n),c)

    y = []
    for i in range(n):
        y.append(call_bs(s, k, t, r, d+c*i, v))

    plt.plot(x,y)
    plt.title('Call price vs. Dividend yield')
    plt.xlabel('dividend yiel')
    plt.ylabel('call price')
    plt.show()

# plot call price vs. volatility
def call_v_des(s, k, t, r, d, v, c=0.001, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(v,v+c*(n),c)

    y = []
    for i in range(n):
        y.append(call_bs(s, k, t, r, d, v+c*i))

    plt.plot(x,y)
    plt.title('Call price vs. Volatility')
    plt.xlabel('volatility')
    plt.ylabel('call price')
    plt.show()

# plot call price vs. all default parameters
def call_des(s, k, t, r, d, v):

    # initialize default parameters
    c = [1,0.03,0.5,0.0002,0.0001,0.001]
    n = 1000

    # compute x values
    x1 = np.arange(s,s+c[0]*(n),c[0])
    x2 = np.arange(k,k+c[1]*(n),c[1])
    x3 = np.arange(t,t+c[2]*(n),c[2])
    x4 = np.arange(r,r+c[3]*(n),c[3])
    x5 = np.arange(d,d+c[4]*(n),c[4])
    x6 = np.arange(v,v+c[5]*(n),c[5])

    # compute y values
    y1 = []
    for i in range(n):
        y1.append(call_bs(s+c[0]*i, k, t, r, d, v))
    y2 = []
    for i in range(n):
        y2.append(call_bs(s, k+c[1]*i, t, r, d, v))
    y3 = []
    for i in range(n):
        y3.append(call_bs(s, k, t+c[2]*i, r, d, v))
    y4 = []
    for i in range(n):
        y4.append(call_bs(s, k, t, r+c[3]*i, d, v))
    y5 = []
    for i in range(n):
        y5.append(call_bs(s, k, t, r, d+c[4]*i, v))
    y6 = []
    for i in range(n):
        y6.append(call_bs(s, k, t, r, d, v+c[5]*i))

    # Initialize the subplot function using number of rows and columns
    fig, axis = plt.subplots(2, 3)

    # For call price vs. stock price
    axis[0, 0].plot(x1, y1)
    axis[0, 0].set_title('Call p vs. Stock p')

    # For call price vs. strike price
    axis[0, 1].plot(x2, y2)
    axis[0, 1].set_title('Call p vs. Strike p')

    # For call price vs. time to maturity
    axis[0, 2].plot(x3, y3)
    axis[0, 2].set_title('Call p vs. Time to mat')

    # For call price vs. risk-free rate
    axis[1, 0].plot(x4, y4)
    axis[1, 0].set_title('Call p vs. R-f rate')

    # For call price vs. dividend yield
    axis[1, 1].plot(x5, y5)
    axis[1, 1].set_title('Call p vs. Div yield')

    # For call price vs. volatility
    axis[1, 2].plot(x6,y6)
    axis[1, 2].set_title('Call p vs. Volatility')

    # output clean fig
    fig.tight_layout()
    plt.show()

# plot put price vs. stock price
def put_s_des(s, k, t, r, d, v, c=1, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(s,s+c*(n),c)

    y = []
    for i in range(n):
        y.append(put_bs(s+c*i, k, t, r, d, v))

    plt.plot(x,y)
    plt.title('Put price vs. Stock price')
    plt.xlabel('stock price')
    plt.ylabel('put price')
    plt.show()

# plot put price vs. strike price
def put_k_des(s, k, t, r, d, v, c=0.03, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(k,k+c*(n),c)

    y = []
    for i in range(n):
        y.append(put_bs(s, k+c*i, t, r, d, v))

    plt.plot(x,y)
    plt.title('Put price vs. Strike price')
    plt.xlabel('strike price')
    plt.ylabel('put price')
    plt.show()

# plot put price vs. time to maturity
def put_t_des(s, k, t, r, d, v, c=0.5, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(t,t+c*(n),c)

    y = []
    for i in range(n):
        y.append(put_bs(s, k, t+c*i, r, d, v))

    plt.plot(x,y)
    plt.title('Put price vs. Time to maturity')
    plt.xlabel('time to maturity')
    plt.ylabel('put price')
    plt.show()

# plot put price vs. risk-free rate
def put_r_des(s, k, t, r, d, v, c=0.0002, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(r,r+c*(n),c)

    y = []
    for i in range(n):
        y.append(put_bs(s, k, t, r+c*i, d, v))

    plt.plot(x,y)
    plt.title('Put price vs. Risk-free rate')
    plt.xlabel('risk-free rate')
    plt.ylabel('put price')
    plt.show()

# plot put price vs. dividend yield
def put_d_des(s, k, t, r, d, v, c=0.0001, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(d,d+c*(n),c)

    y = []
    for i in range(n):
        y.append(put_bs(s, k, t, r, d+c*i, v))

    plt.plot(x,y)
    plt.title('Put price vs. Dividend yield')
    plt.xlabel('dividend yield')
    plt.ylabel('put price')
    plt.show()

# plot put price vs. volatility
def put_v_des(s, k, t, r, d, v, c=0.001, n=1000):

    # number of obs
    n = 1000

    # compute x and y data
    x = np.arange(v,v+c*(n),c)

    y = []
    for i in range(n):
        y.append(put_bs(s, k, t, r, d, v+c*i))

    plt.plot(x,y)
    plt.title('Put price vs. Volatility')
    plt.xlabel('volatility')
    plt.ylabel('put price')
    plt.show()

# plot put price vs. all default parameters
def put_des(s, k, t, r, d, v):

    # initialize default parameters
    c = [1,0.03,0.5,0.0002,0.0001,0.001]
    n = 1000

    # compute x values
    x1 = np.arange(s,s+c[0]*(n),c[0])
    x2 = np.arange(k,k+c[1]*(n),c[1])
    x3 = np.arange(t,t+c[2]*(n),c[2])
    x4 = np.arange(r,r+c[3]*(n),c[3])
    x5 = np.arange(d,d+c[4]*(n),c[4])
    x6 = np.arange(v,v+c[5]*(n),c[5])

    # compute y values
    y1 = []
    for i in range(n):
        y1.append(put_bs(s+c[0]*i, k, t, r, d, v))
    y2 = []
    for i in range(n):
        y2.append(put_bs(s, k+c[1]*i, t, r, d, v))
    y3 = []
    for i in range(n):
        y3.append(put_bs(s, k, t+c[2]*i, r, d, v))
    y4 = []
    for i in range(n):
        y4.append(put_bs(s, k, t, r+c[3]*i, d, v))
    y5 = []
    for i in range(n):
        y5.append(put_bs(s, k, t, r, d+c[4]*i, v))
    y6 = []
    for i in range(n):
        y6.append(put_bs(s, k, t, r, d, v+c[5]*i))

    # Initialize the subplot function using number of rows and columns
    fig, axis = plt.subplots(2, 3)

    # For put price vs. stock price
    axis[0, 0].plot(x1, y1, 'r')
    axis[0, 0].set_title('Put p vs. Stock p')

    # For put price vs. strike price
    axis[0, 1].plot(x2, y2, 'r')
    axis[0, 1].set_title('Put p vs. Strike p')

    # For put price vs. time to maturity
    axis[0, 2].plot(x3, y3, 'r')
    axis[0, 2].set_title('Put p vs. Time to mat')

    # For put price vs. risk-free rate
    axis[1, 0].plot(x4, y4, 'r')
    axis[1, 0].set_title('Put p vs. R-f rate')

    # For put price vs. dividend yield
    axis[1, 1].plot(x5, y5, 'r')
    axis[1, 1].set_title('Put p vs. Div yield')

    # For put price vs. volatility
    axis[1, 2].plot(x6, y6, 'r')
    axis[1, 2].set_title('Put p vs. Volatility')

    # output clean fig
    fig.tight_layout()
    plt.show()
