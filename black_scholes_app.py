import math
import streamlit as st


def norm_cdf(x: float) -> float:
    """Cumulative distribution function for the standard normal distribution."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def black_scholes_price(
    s: float, k: float, t: float, r: float, sigma: float, option_type: str = "call"
) -> float:
    """Calculate European option price using the Black-Scholes formula."""
    if t <= 0 or sigma <= 0:
        raise ValueError("Time to maturity and volatility must be positive")

    d1 = (math.log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)

    if option_type == "call":
        price = s * norm_cdf(d1) - k * math.exp(-r * t) * norm_cdf(d2)
    else:
        price = k * math.exp(-r * t) * norm_cdf(-d2) - s * norm_cdf(-d1)
    return price


st.title("Black-Scholes Option Pricer")

s = st.number_input("Underlying price", value=100.0)
k = st.number_input("Strike price", value=100.0)
t = st.number_input("Time to maturity (years)", value=1.0)
r = st.number_input("Risk-free rate", value=0.01)
sigma = st.number_input("Volatility", value=0.2)
option_type = st.selectbox("Option type", ["call", "put"])

if st.button("Calculate"):
    try:
        price = black_scholes_price(s, k, t, r, sigma, option_type)
        st.write(f"{option_type.capitalize()} option price: {price:.4f}")
    except ValueError as e:
        st.error(str(e))
