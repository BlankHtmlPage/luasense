# LuaSense

A Python library providing intelligent autocompletion for Lua scripting language keywords and built-in functions.

## Features

- Fast, case-sensitive autocompletion for Lua keywords and functions
- Input validation with meaningful error messages
- Zero external dependencies
- Fully typed for better IDE support

## Installation

```bash
pip install luasense
```

## Usage

```python
import luasense

# Get autocomplete suggestions
try:
    suggestions = luasense.autocomplete("pri")
    print(suggestions)  # ['print', 'private']
except luasense.TooShortRequestError:
    print("Input too short - minimum 2 characters required")
```

## API

autocomplete(query: str) -> List[str]

Returns a list of Lua keywords and built-in functions that start with the given query.

· query: String to autocomplete (minimum 2 characters)
· Returns: List of matching Lua identifiers
· Raises: TooShortRequestError if query length < 2

## License

Apache-2.0
