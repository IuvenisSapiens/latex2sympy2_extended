from latex2sympy2_extended.math_normalization import NormalizationConfig, normalize_latex


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

def test_boxed_normalization():
    config = NormalizationConfig(
        basic_latex=False,
        units=False,
        malformed_operators=False,
        nits=False,
        boxed=True,
        equations=False
    )

    assert normalize_latex("\\boxed{\\left( 3, \\frac{\\pi}{2} \\right)}.", config) == "\\left( 3, \\frac{\\pi}{2} \\right)"
