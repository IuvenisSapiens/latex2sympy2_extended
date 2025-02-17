try:
    # Python 3.8+ standard library
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # For older Python versions, if needed, install importlib_metadata
    from importlib_metadata import version, PackageNotFoundError

try:
    antlr_version = version("antlr4-python3-runtime")
except PackageNotFoundError:
    antlr_version = ""

if antlr_version.startswith("4.13.2"):
    from latex2sympy2_extended.gen.antlr4_13_2 import PSParser, PSLexer
elif antlr_version.startswith("4.11"):
    from latex2sympy2_extended.gen.antlr4_11_0 import PSParser, PSLexer
elif antlr_version.startswith("4.9.3"):
    from latex2sympy2_extended.gen.antlr4_9_3 import PSParser, PSLexer
else:
    raise ImportError(
        f"Unsupported ANTLR version {antlr_version}, "
        "only 4.9.3, 4.11.0, and 4.13.2 runtime versions are supported."
    )