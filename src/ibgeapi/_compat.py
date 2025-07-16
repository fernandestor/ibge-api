"""Compatibility helpers for optional typing features."""

try:  # Python 3.12+
    from typing import override
except ImportError:  # pragma: no cover - fallback for Python<3.12
    try:  # Try typing_extensions first
        from typing_extensions import override  # type: ignore
    except Exception:  # pragma: no cover - final fallback
        def override(func):  # type: ignore
            """Fallback noop decorator when typing.override is unavailable."""
            return func
