from pytest_bdd import scenarios, given, when, then, parsers

from screenpy import Actor
from screenpy.actions import See

from screenpy_requests.actions import SendDELETERequest
from screenpy.resolutions import IsEqualTo, IsEmpty
from screenpy_requests.questions import (
    BodyOfTheLastResponse,
    StatusCodeOfTheLastResponse
)
from screenpy import AnActor
from screenpy_requests.abilities import MakeAPIRequests

# Actor
THE_MAIN_ACTOR = AnActor.named("Harold")

# Scenarios
scenarios('../../features/poke/delete.feature')

# Given Steps
@given(parsers.parse('final user is loged in app'))
def call_user():
    THE_MAIN_ACTOR.can(MakeAPIRequests())

# When Steps

@when(parsers.parse('send a request to delete pokemon with id "{id}"'))
def user_send_destroy(id):
    THE_MAIN_ACTOR.attempts_to(SendDELETERequest.to(
        f"https://reqres.in/{id}"))

# Then Steps

@then(parsers.parse('the response status code is "{code:d}"'))
def check_status_code(code):
    See.the(StatusCodeOfTheLastResponse(), IsEqualTo(code))

