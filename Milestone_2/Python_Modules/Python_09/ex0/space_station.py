#!/usr/bin/env


from pydantic import BaseModel, Field
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool = True
    notes: str


if __name__ == "__main__":
    ...