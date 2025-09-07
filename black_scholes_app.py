import streamlit as st
from black_scholes import black_scholes_price


def main() -> None:
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


if __name__ == "__main__":
    main()
