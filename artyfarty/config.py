from dynaconf import Dynaconf, Validator
from pathlib import Path

validators = [
    # Validator("OUTPUT_DIR", must_exist=True, cast=Path),
    Validator("OUTPUT__PATH", must_exist=True, default="output", cast=Path),
    Validator("OUTPUT__FILENAME_PREFIX", must_exist=True, default="", cast=str),
    Validator("OUTPUT__FILENAME_TIMESTAMP", must_exist=True, default=False, cast=bool),
    Validator("REPLICATE_API_TOKEN", must_exist=True),
    Validator("INPUTS", must_exist=True),
]

settings = Dynaconf(
    envvar_prefix="ARTYFARTY",
    settings_files=["settings.toml", ".secrets.toml"],
    validators=validators,
)
