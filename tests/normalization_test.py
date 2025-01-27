from build.lib.latex2sympy2_extended.math_normalization import NormalizationConfig
from latex2sympy2_extended.math_normalization import normalize_latex


def test_units_normalization():
    config = NormalizationConfig(
        basic_latex=False,
        units=True,
        malformed_operators=False,
        nits=False,
        boxed=False,
        equations=False
    )

    # Test basic unit removal
    assert normalize_latex("865 \\mbox{ inches}^2", config) == "865"
    assert normalize_latex("\\mbox{hello}", config) == "\\mbox{hello}"
