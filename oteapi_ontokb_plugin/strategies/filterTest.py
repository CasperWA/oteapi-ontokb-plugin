"""Demo filter strategy."""
# pylint: disable=no-self-use,unused-argument
from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from typing import Any, Dict, Optional

    from oteapi.models.filterconfig import FilterConfig



@dataclass
class TestFilterStrategy:
    """Filter Strategy."""

    filter_config: "FilterConfig"

    def initialize(
        self, session: "Optional[Dict[str, Any]]" = None
    ) -> "Dict[str, Any]":
        """Initialize strategy.
        This method will be called through the `/initialize` endpoint of the OTE-API
        Services.
        Parameters:
            session: A session-specific dictionary context.
        Returns:
            Dictionary of key/value-pairs to be stored in the sessions-specific
            dictionary context.
        """
        print("[ONTOKB PLUGIN FILTER]: Initialize")
        return {}

    def get(self, session: "Optional[Dict[str, Any]]" = None) -> "Dict[str, Any]":
        """Execute the strategy.
        This method will be called through the strategy-specific endpoint of the
        OTE-API Services.
        Parameters:
            session: A session-specific dictionary context.
        Returns:
            Dictionary of key/value-pairs to be stored in the sessions-specific
            dictionary context.
        """
        print("[ONTOKB PLUGIN FILTER]: Getting data")
        return {"key": ""}