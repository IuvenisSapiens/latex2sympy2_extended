from sympy import (
    Symbol, FiniteSet, Interval, S, Union, Intersection,
    Complement, Contains, Not, Add, Mul, Pow, UnevaluatedExpr
)
import sympy
from tests.context import assert_equal, _Add, _Mul, _Pow

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
a = Symbol('a')
b = Symbol('b')

def test_literal_sets():
    # Test built-in sets
    assert_equal("\\mathbb{N}", S.Naturals)
    assert_equal("\\mathbb{Z}", S.Integers)
    assert_equal("\\mathbb{Q}", S.Rationals)
    assert_equal("\\mathbb{R}", S.Reals)
    assert_equal("\\mathbb{C}", S.Complexes)
    # Test empty set
    assert_equal("\\emptyset", S.EmptySet)
    assert_equal("\\{\\}", S.EmptySet)
    assert_equal("∅", S.EmptySet)

def test_finite_sets():
    # Test basic finite sets
    assert_equal("{1,2,3}", FiniteSet(1, 2, 3))
    assert_equal("{x,y,z}", FiniteSet(x, y, z))
    # Test sets with expressions
    assert_equal("{x+y, 2x, y^2}", FiniteSet(_Add(x, y), _Mul(2, x), _Pow(y, 2)))
    # Test sets with plus-minus notation
    assert_equal("{x \\pm y}", FiniteSet(_Add(x, y), _Add(x, _Mul(-1, y))))
    assert_equal("{2 \\pm 1}", FiniteSet(3, 1))
    assert_equal("1,2,3,4", FiniteSet(1, 2, 3, 4))

def test_intervals():
    # Test closed intervals
    assert_equal("[a,b]", Interval(a, b))
    assert_equal("[1,2]", Interval(1, 2))
    # # Test open intervals
    assert_equal("(a,b)", Interval(a, b, left_open=True, right_open=True))
    assert_equal("(1,2)", Interval(1, 2, left_open=True, right_open=True))
    # # Test half-open intervals
    assert_equal("[a,b)", Interval(a, b, right_open=True))
    assert_equal("(a,b]", Interval(a, b, left_open=True))

def test_set_operations():
    # Test union
    assert_equal("{1,2} \\cup {2,3}", Union(FiniteSet(1, 2), FiniteSet(2, 3), evaluate=False))
    assert_equal("{1,2} ∪ {2,3}", Union(FiniteSet(1, 2), FiniteSet(2, 3), evaluate=False))
    # Test intersection
    assert_equal("{1,2} \\cap {2,3}", Intersection(FiniteSet(1, 2), FiniteSet(2, 3), evaluate=False))
    assert_equal("{1,2} ∩ {2,3}", Intersection(FiniteSet(1, 2), FiniteSet(2, 3), evaluate=False))
    # Test set difference
    assert_equal("{1,2} \\setminus {2}", Complement(FiniteSet(1, 2), FiniteSet(2), evaluate=False))
    assert_equal("{1,2} ∖ {2}", Complement(FiniteSet(1, 2), FiniteSet(2), evaluate=False))

def test_set_relations():
    # Test element membership
    assert_equal("x \\in {1,2,3}", FiniteSet(1, 2, 3))
    assert_equal("x \\notin {1,2,3}", sympy.S.Complexes - FiniteSet(1, 2, 3))
    # # Test subset relations
    assert_equal("{1} \\subseteq {1,2}", FiniteSet(1).is_subset(FiniteSet(1, 2)))
    assert_equal("{1,2} \\supseteq {1}", FiniteSet(1).is_subset(FiniteSet(1, 2)))

def test_complex_set_operations():
    # Test nested set operations
    assert_equal("({1,2} \\cup {3,4}) \\cap {2,3}", 
                Intersection(Union(FiniteSet(1, 2), FiniteSet(3, 4), evaluate=False), 
                           FiniteSet(2, 3), evaluate=False))
    # Test multiple operations
    assert_equal("{1,2} \\cup {3,4} \\cup {5,6}", 
                Union(Union(FiniteSet(1, 2), FiniteSet(3, 4), evaluate=False), FiniteSet(5, 6), evaluate=False))
    assert_equal("{1,2} \\cap {2,3} \\cap {2,4}", 
                Intersection(Intersection(FiniteSet(1, 2), FiniteSet(2, 3), evaluate=False), FiniteSet(2, 4), evaluate=False))
    # Test mixed operations
    assert_equal("({1,2} \\cup {3,4}) \\setminus {2,3}", 
                Complement(Union(FiniteSet(1, 2), FiniteSet(3, 4), evaluate=False), 
                         FiniteSet(2, 3), evaluate=False))

def test_interval_operations():
    # Test interval operations
    assert_equal("[0,1] \\cup [2,3]", Union(Interval(0, 1), Interval(2, 3), evaluate=False))
    assert_equal("[0,2] \\cap (1,3)", Intersection(Interval(0, 2), 
                                                  Interval(1, 3, left_open=True, right_open=True), 
                                                  evaluate=False))
    assert_equal("(0,1)", Interval(0, 1, left_open=True, right_open=True))
    assert_equal("[0,2] \\setminus (0,1)", Complement(Interval(0, 2), 
                                                     Interval(0, 1, left_open=True, right_open=True), 
                                                     evaluate=False))

def test_mixed_set_types():
    # Test operations between different set types
    assert_equal("{1,2} \\cup [0,3]", Union(FiniteSet(1, 2), Interval(0, 3), evaluate=False))
    assert_equal("(0,1) \\cap {0.5}", Intersection(Interval(0, 1, left_open=True, right_open=True), 
                                                  FiniteSet(0.5), evaluate=False))
    assert_equal("[0,1] \\setminus {0.5}", Complement(Interval(0, 1), FiniteSet(0.5), evaluate=False)) 