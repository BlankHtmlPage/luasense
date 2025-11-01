"""
LuaSense - Intelligent autocompletion for Lua scripting language.

This module provides case-sensitive autocompletion for Lua keywords,
built-in functions, and language constructs.
"""

from typing import List, Final

# Lua keywords and built-in functions database
_LUA_KEYWORDS: Final[list[str]] = [
    # Keywords (Lua 5.x)
    "and", "break", "do", "else", "elseif", "end", "false", "for", "function",
    "goto", "if", "in", "local", "nil", "not", "or", "repeat", "return", "then",
    "true", "until", "while",

    # Standard globals
    "_G", "_VERSION",
    "assert", "collectgarbage", "dofile", "error", "getmetatable", "ipairs",
    "load", "loadfile", "loadstring", "next", "pairs", "pcall", "print",
    "rawequal", "rawget", "rawlen", "rawset", "require", "select",
    "setmetatable", "tonumber", "tostring", "type", "xpcall",

    # coroutine library
    "coroutine.create", "coroutine.resume", "coroutine.running",
    "coroutine.status", "coroutine.wrap", "coroutine.yield",

    # package library
    "package.config", "package.cpath", "package.path", "package.loaded",
    "package.loaders", "package.searchers", "package.searchpath", "package.preload",
    "package.loadlib",

    # string library
    "string.byte", "string.char", "string.dump", "string.find", "string.format",
    "string.gmatch", "string.gsub", "string.len", "string.lower", "string.match",
    "string.rep", "string.reverse", "string.sub", "string.upper",

    # table library
    "table.concat", "table.insert", "table.move", "table.pack", "table.remove",
    "table.sort", "table.unpack", "table.maxn",  # table.maxn present in some versions/compat libs

    # math library
    "math.abs", "math.acos", "math.asin", "math.atan", "math.atan2", "math.ceil",
    "math.cos", "math.cosh", "math.deg", "math.exp", "math.floor", "math.fmod",
    "math.frexp", "math.huge", "math.ldexp", "math.log", "math.log10", "math.max",
    "math.min", "math.modf", "math.pi", "math.pow", "math.rad", "math.random",
    "math.randomseed", "math.sin", "math.sinh", "math.sqrt", "math.tan", "math.tanh",

    # io library
    "io.close", "io.flush", "io.input", "io.lines", "io.open", "io.output",
    "io.popen", "io.read", "io.tmpfile", "io.type", "io.write",

    # os library
    "os.clock", "os.date", "os.difftime", "os.execute", "os.exit", "os.getenv",
    "os.remove", "os.rename", "os.time", "os.tmpname",

    # debug library
    "debug.debug", "debug.gethook", "debug.getinfo", "debug.getlocal",
    "debug.getmetatable", "debug.getregistry", "debug.getupvalue",
    "debug.sethook", "debug.setlocal", "debug.setupvalue", "debug.traceback",

    # utf8 library
    "utf8.char", "utf8.charpattern", "utf8.codepoint", "utf8.codes",
    "utf8.len", "utf8.offset", "utf8.nfcnormalize", "utf8.normalize", "utf8.next",

    # additional/compat globals sometimes present
    "unpack", "module", "package.loaders", "loadlib", "bit32", "bit32.band",
    "bit32.bnot", "bit32.bor", "bit32.bxor", "bit32.lshift", "bit32.rshift",
    "bit32.arshift", "bit32.extract", "bit32.replace", "bit32.test",

    # common Lua-ecosystem helpers and deprecated/compat names
    "pairsByKeys", "table.foreach", "table.foreachi",  # may appear in compatibility modules
]


class TooShortRequestError(ValueError):
    """Exception raised when autocomplete query is too short."""
    
    def __init__(self, query: str, min_length: int = 2) -> None:
        self.query = query
        self.min_length = min_length
        super().__init__(
            f"Autocomplete query '{query}' is too short. "
            f"Minimum length required: {min_length}"
        )


def autocomplete(query: str) -> List[str]:
    """
    Get autocomplete suggestions for Lua keywords and built-in functions.
    
    Args:
        query: The string to autocomplete (minimum 2 characters)
        
    Returns:
        List of Lua keywords and functions that start with the query
        
    Raises:
        TooShortRequestError: If query length is less than 2 characters
    """
    if len(query) < 2:
        raise TooShortRequestError(query)
    
    # Case-sensitive prefix matching using list comprehension for O(n) performance
    matches = [keyword for keyword in _LUA_KEYWORDS if keyword.startswith(query)]
    
    # Sort by length then alphabetically for better UX
    matches.sort(key=lambda x: (len(x), x))
    
    return matches


# Module-level exports
__all__ = ["autocomplete", "TooShortRequestError", "__version__"]
__version__ = "0.1.0"
