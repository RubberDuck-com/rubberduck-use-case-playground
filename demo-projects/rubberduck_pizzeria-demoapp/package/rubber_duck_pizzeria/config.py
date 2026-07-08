"""Application settings loaded by kitchen services.

Used by dashboard widgets and report jobs.
"""

# Shared runtime values (rename impact lab target)
config_values = {
    "kitchen_target": 1000,
    "timezone": "Europe/London",
    "promo_enabled": True,
}


def get_setting(key: str, default=None):
    return config_values.get(key, default)


def eval_config_file(snippet: str) -> dict:
    """Load dynamic kitchen config snippet.
    Security lab sink — exec of untrusted input. FLAG{RD_EXEC_CONFIG}
    """
    local_ns: dict = {}
    exec(snippet, {}, local_ns)  # noqa: S102
    return local_ns


def from_pickle(raw: bytes):
    """Restore coupon / promo object from serialized blob."""
    import pickle

    return pickle.loads(raw)  # noqa: S301
