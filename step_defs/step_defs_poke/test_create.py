import json

from pytest_bdd import scenarios, given, when, then, parsers

from screenpy import Actor
from screenpy.actions import See, Debug

from screenpy_requests.actions import SendPOSTRequest, AddHeader
from screenpy.resolutions import IsEqualTo, ContainsTheEntry
from screenpy_requests.questions import (
    BodyOfTheLastResponse,
    StatusCodeOfTheLastResponse
)
from screenpy import AnActor
from screenpy_requests.abilities import MakeAPIRequests

# Actor
THE_MAIN_ACTOR = AnActor.named("Zaraza")

# Scenarios
scenarios('../../features/poke/create.feature')

# Given Steps


@given(parsers.parse('final user is loged in app'))
def call_user():
    THE_MAIN_ACTOR.can(MakeAPIRequests())

# When Steps


@when(parsers.parse('send a request to create a new pokemon'))
def user_send_creation():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    headers = {
        "Content-type": "application/JSON",
        "RQUID": "123412341234"
    }

    THE_MAIN_ACTOR.attempts_to(
        AddHeader(headers),
        SendPOSTRequest.to(
            'https://reqres.in/api/users').with_(data=json.dumps(payload))
    )

# Then Steps


@then(parsers.parse('the response status code is "{code:d}"'))
def check_status_code(code):
    THE_MAIN_ACTOR.should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(code)))


@then(parsers.parse('the response contains the information from new pokemon'))
def check_response_information():
    THE_MAIN_ACTOR.should(
        See.the(
            BodyOfTheLastResponse(),
            ContainsTheEntry(name='morpheus')
        )
    )
