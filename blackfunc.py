from scipy.stats import norm
from matplotlib import pyplot as plt
import numpy as np

# Implement Black-Scholes to price a call.
def call_bs(s, k, t, r, d, v):

    # Compute parameters
    d1 = (np.log(s/k) + (r - d + v**2/2) * t) / (v * np.sqrt(t))
    d2 = d1 - v * np.sqrt(t)

    # Plug parameters in Normal cdf.
    nd1 = norm.cdf(d1)
    nd2 = norm.cdf(d2)

    # Compute call price
    call_price = np.exp(-d * t) * s * nd1 - np.exp(-r * t) * k * nd2

    return call_price


# Implement Black-Scholes to price a put using put-call parity.
def put_bs(s, k, t, r, d, v):

    # Compute parameters
    d1 = (np.log(s/k) + (r - d + v**2/2) * t) / (v * np.sqrt(t))
    d2 = d1 - v * np.sqrt(t)

    # Plug parameters in Normal cdf.
    nd1 = norm.cdf(-d1)
    nd2 = norm.cdf(-d2)

    # Compute put price
    put_price = np.exp(-r * t) * k * nd2 - np.exp(-d * t) * s * nd1

    return put_price
