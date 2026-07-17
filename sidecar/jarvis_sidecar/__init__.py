"""JARVIS Code sidecar package."""

from __future__ import annotations

import os
import sys
from pathlib import Path


# Ensure hermes-agent (for nous-research OAuth token refresh) is importable.
# The hermes_cli package lives in the hermes-agent repo and provides
# resolve_nous_access_token() which the sidecar uses to refresh expired
# nous-research OAuth-sourced API keys transparently on 401.
_HERMES_AGENT_DIR = Path("/mnt/storage/Projects/hermes-agent")
if _HERMES_AGENT_DIR.is_dir():
    _path = str(_HERMES_AGENT_DIR)
    if _path not in sys.path:
        sys.path.insert(0, _path)
