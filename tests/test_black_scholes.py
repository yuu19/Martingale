import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from black_scholes import black_scholes_price


def test_black_scholes_call_price():
    price = black_scholes_price(100, 100, 1, 0.01, 0.2, "call")
    assert price == pytest.approx(8.4333, rel=1e-4)


def test_black_scholes_put_price():
    price = black_scholes_price(100, 100, 1, 0.01, 0.2, "put")
    assert price == pytest.approx(7.4383, rel=1e-4)


def test_black_scholes_invalid_params():
    with pytest.raises(ValueError):
        black_scholes_price(100, 100, 0, 0.01, 0.2)
