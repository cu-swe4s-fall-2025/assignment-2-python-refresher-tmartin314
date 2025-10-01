import math
import random
import statistics
import pytest

from my_utils import mean, median, std, get_column

# ---------- Helper ----------
def random_int_list(n=100, lo=-10_000, hi=10_000):
    random.seed(12345)
    return [random.randint(lo,hi) for _ in range(n)]

# ---------- mean ----------
def test_mean_matches_statistics_mean_on_random_list():
    data = random_int_list(200)
    assert math.isclose(mean(data), statistics.mean(data), rel_tol=1e-12, abs_tol=1e-12)

def test_mean_handles_negatives_and_zero():
    data = [0, -5, 5, -10, 10]
    assert mean(data) == 0

def test_mean_empty_returns_none():
    assert mean([]) is None

def test_mean_raises_on_non_numeric():
    with pytest.raises(TypeError):
        mean([1, "2", 3])

def test_mean_does_not_mutate_input():
    data = [1, 2, 3, 4]
    copy = data[:]
    _ = mean(data)
    assert data == copy

# ---------- median ----------
@pytest.mark.parametrize("data, expected", [
    ([1], 1),
    ([1, 3, 2], 2),
    ([1, 2, 3, 4], (2 + 3) / 2),
    ([-5, 0, 5], 0),
])
def test_median_simple_cases(data, expected):
    assert median(data) == expected

def test_median_matches_statistics_median_on_random_list():
    data = random_int_list(199)  # odd length
    assert median(data) == statistics.median(data)
    data = random_int_list(200)  # even length
    assert median(data) == statistics.median(data)

def test_median_empty_returns_none():
    assert median([]) is None

def test_median_does_not_mutate_input():
    data = [5, 1, 9, 3]
    copy = data[:]
    _ = median(data)
    assert data == copy

# ---------- standard_deviation (population) ----------
def test_std_matches_statistics_pstdev_on_random_list():
    data = random_int_list(300)
    assert math.isclose(
        std(data),
        statistics.pstdev(data),
        rel_tol=1e-12,
        abs_tol=1e-12
    )

def test_std_zero_for_constant_list():
    assert std([7, 7, 7, 7]) == 0.0

def test_std_empty_returns_none():
    assert std([]) is None

def test_std_raises_on_non_numeric():
    with pytest.raises(TypeError):
        std([1, 2, "x"])

def test_std_does_not_mutate_input():
    data = [2, 4, 6]
    copy = data[:]
    _ = std(data)
    assert data == copy

