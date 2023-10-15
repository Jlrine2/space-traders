# generated by datamodel-codegen:
#   filename:  api-docs/models/Cooldown.json
#   timestamp: 2023-10-15T19:00:16+00:00

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, conint, constr


class Cooldown(BaseModel):
    shipSymbol: constr(min_length=1) = Field(
        ..., description="The symbol of the ship that is on cooldown"
    )
    totalSeconds: conint(ge=0) = Field(
        ..., description="The total duration of the cooldown in seconds"
    )
    remainingSeconds: conint(ge=0) = Field(
        ..., description="The remaining duration of the cooldown in seconds"
    )
    expiration: Optional[datetime] = Field(
        None,
        description="The date and time when the cooldown expires in ISO 8601 format",
    )
