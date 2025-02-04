# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0]

### Added
- Support for `E` notation and `E` symbol in expressions
- Support for number subscripts in expressions
- Support for chained inequalities (e.g. `a < b < c`)
- Support for multiple boxed elements in normalization
- Support for "and"/"or" text conversion to semicolons in set notation
- Helper function `convert_elements_to_set_or_tuple()` to handle set/tuple conversion
- Added `is_expr_of_only_symbols` to public API
- Added docstring for `interpret_contains_as_eq` in ConversionConfig

### Changed
- Made `ConversionConfig` frozen dataclass
- Changed default behavior of `interpret_simple_eq_as_assignment` to `False`
- Updated set membership handling to use `Eq()` instead of direct assignment
- Made `NormalizationConfig` fields have default values
- Improved handling of boxed content in normalization
- Refactored set element parsing to be more consistent
- Updated handling of matrix operations with tuples
- Simplified grammar rules for `semicolon_elements` and `comma_elements` to be more linear

### Fixed
- Fixed handling of empty text in normalization
- Fixed handling of matrix transpose operations
- Added proper exception handling for timeouts
- Fixed handling of "and"/"or" text in set notation
- Fixed handling of E notation and E symbol
- Fixed handling of number subscripts

### Tests
- Added tests for boxed normalization
- Added tests for set operations with and/or
- Added tests for E notation and symbols
- Added more comprehensive set relation tests
- Disabled some linalg placeholder tests temporarily 