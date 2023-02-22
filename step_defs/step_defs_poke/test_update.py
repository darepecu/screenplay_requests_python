import json

from pytest_bdd import scenarios, given, when, then, parsers

from screenpy import Actor
from screenpy.actions import See, Debug

from screenpy_requests.actions import SendPUTRequest, AddHeader
from screenpy.resolutions import IsEqualTo, ContainsTheEntry
from screenpy_requests.questions import (
    BodyOfTheLastResponse,
    StatusCodeOfTheLastResponse
)
from screenpy import AnActor
from screenpy_requests.abilities import MakeAPIRequests

# Actor
THE_MAIN_ACTOR = AnActor.named("Kathe")

# Scenarios
scenarios('../../features/poke/update.feature')

# Given Steps
@given(parsers.parse('final user is loged in app'))
def call_user():
    THE_MAIN_ACTOR.can(MakeAPIRequests())

# When Steps

@when(parsers.parse('send a request to update "{id}" user to field "{field_poke}" with value "{new_value}"'))
def user_send_update(id, field_poke, new_value):
    payload = {
        field_poke: new_value
    }

    headers = {
        "Content-type": "application/JSON",
        "RQUID": "123412341234"
    }

    THE_MAIN_ACTOR.attempts_to(
        AddHeader(headers),
        SendPUTRequest.to(
            f"https://reqres.in/api/users/{id}").with_(data=json.dumps(payload))
    )

# Then Steps

@then(parsers.parse('the response status code is "{code:d}"'))
def check_status_code(code):
    THE_MAIN_ACTOR.should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(code)))

@then(parsers.parse('the response contains new information from pokemon "{field_poke}" with value "{new_value}"'))
def check_response_information(field_poke, new_value):
    THE_MAIN_ACTOR.should(
        See.the(
            BodyOfTheLastResponse(),
            ContainsTheEntry(name=new_value)
        )
    )
