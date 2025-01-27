import pytest
from latex2sympy2_extended.latex2sympy2 import latex2sympy
from tests.context import assert_equal, get_simple_examples


@pytest.mark.parametrize('input, output, symbolically', [
    ('\\text{a}', 'a', True),
    ('\\text{(b)}', 'b', True),
    ('\\textit{c}', '\\text{c}', True),
    ('\\textbf{E}', 'E', True),
    ('\\textbf{e}', 'e', True),
    ('\\textbf{i}', 'i', True),
    ('\\mbox{hello}', '\\text{hello}', True),
])
def test_symbol(input, output, symbolically):
    input_parsed = latex2sympy(input)
    output_parsed = latex2sympy(output)
    assert input_parsed == output_parsed
