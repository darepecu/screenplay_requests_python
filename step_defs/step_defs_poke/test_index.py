from pytest_bdd import scenarios, given, when, then, parsers

from screenpy import Actor
from screenpy.actions import See

from screenpy_requests.actions import SendAPIRequest, SendGETRequest
from screenpy.resolutions import IsEqualTo, ContainsTheEntry
from screenpy_requests.questions import (
    BodyOfTheLastResponse,
    StatusCodeOfTheLastResponse
)
from screenpy import AnActor
from screenpy_requests.abilities import MakeAPIRequests

# Actor 
THE_MAIN_ACTOR = AnActor.named("Alzate")

# Scenarios
scenarios('../../features/poke/index.feature')

# Given Steps
@given(parsers.parse('final user is loged in app'))
def call_user():
    THE_MAIN_ACTOR.can(MakeAPIRequests())

# When Steps

@when(parsers.parse('send a request to show all pokemons'))
def user_send_index():
    THE_MAIN_ACTOR.attempts_to ( SendGETRequest.to('https://pokeapi.co/api/v2/pokemon') )

# Then Steps

@then(parsers.parse('the response status code is "{code:d}"'))
def check_status_code(code):
    THE_MAIN_ACTOR.should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(code)))

@then(parsers.parse('the response contains results all pokemons'))
def check_response_information():
    THE_MAIN_ACTOR.should(
        See.the(
            BodyOfTheLastResponse(),
            ContainsTheEntry(count=1279)
        )
    )
