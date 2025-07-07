"""Minimal entrypoint to verify logging.

- パッケージ import 時に src.__init__ が configure_logging() を呼び出す
- main() 内で色付きログ + ファイル出力が行われることを確認する
"""

from __future__ import annotations

import logging

import src  # noqa: F401  （← configure_logging が発動）

LOGGER = logging.getLogger(__name__)


def main() -> None:
    LOGGER.debug("This is a DEBUG message (file only)")
    LOGGER.info("This is an INFO message (console + file)")
    LOGGER.warning("This is a WARNING message (console + file)")


if __name__ == "__main__":
    main()
