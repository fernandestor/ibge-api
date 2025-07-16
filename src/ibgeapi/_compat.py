try:
    from typing import override
except ImportError:  # pragma: no cover - fallback for Python<3.12
    def override(func):
        """Fallback noop decorator when typing.override is unavailable."""
        return func
