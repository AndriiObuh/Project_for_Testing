import  pytest
from contextlib import nullcontext as does_not_raise
from app.calc import Calc

class TestCalc:

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (4, 0, ZeroDivisionError, pytest.raises((ZeroDivisionError))),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calc().divide(x, y) == res

    @pytest.mark.parametrize("x, y, res, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            (5, "-1", 4, pytest.raises(TypeError))
        ]
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calc().add(x, y) == res