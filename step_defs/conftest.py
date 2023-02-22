from typing import Generator

import pytest

from screenpy import AnActor
from screenpy.pacing import the_narrator
from screenpy_requests.abilities import MakeAPIRequests

from screenpy.pacing import the_narrator
from screenpy.narration.adapters.stdout_adapter import StdOutAdapter

the_narrator.attach_adapter(StdOutAdapter())

@pytest.fixture
def FinalUser() -> Generator:
    """Generate our final user, Cameron."""
    the_actor = AnActor.named("Cameron").who_can(MakeAPIRequests())
    yield the_actor
    the_actor.exit_stage_left()