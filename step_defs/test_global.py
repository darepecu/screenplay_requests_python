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
THE_MAIN_ACTOR = AnActor.named("Harold")

# Scenarios

scenarios('../features/global.feature')

# Given Steps


@given('final user want to login in the aplicacion')
def call_user():
    THE_MAIN_ACTOR.can(MakeAPIRequests())

# When Steps


@when(parsers.parse('the user send credentials'))
def user_send_credentials():

    payload = {
        "name": "Developer",
        "email": "Developer5@gmail.com",
        "password": 123456
    }

    headers = {
        "Content-type": "application/JSON",
        "RQUID": "123412341234"
    }

    THE_MAIN_ACTOR.attempts_to(
        AddHeader(headers),
        SendPOSTRequest.to(
            'http://restapi.adequateshop.com/api/authaccount/login').with_(data=json.dumps(payload))
    )

# Then Steps


@then(parsers.parse('the response status code is "{code:d}"'))
def check_status_code():
    THE_MAIN_ACTOR.should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)))


@then(parsers.parse('the response contains authentication token'))
def check_response_information():
    THE_MAIN_ACTOR.should(
        See.the(
            BodyOfTheLastResponse(),
            ContainsTheEntry(message='success')
        )
    )
