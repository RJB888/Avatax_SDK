"""Example of resolve address to retrieve geolocation information for a specified address."""
import os
from client import AvaTaxClient


def create_client():
    """
    Construct a new AvaTaxClient in a Sandbox Environment.

    'test app': The name of the application
    'ver 0.0': Version number of the application
    'test machine': Name of the machine on which this code is executing
    'sandbox': Logs you into the sandbox environment instead of production.

    Add credentials to configure client to use the specified security settings:
        username/password or
        accountId/LicenseKey or
        bearer token

    Your credentials should be set as environment variables prior to
    executing the request.

    Return example_client.
    """
    example_client = AvaTaxClient('test app',
                                  'ver 0.0',
                                  'test machine',
                                  'sandbox')
    example_client.add_credentials(
        os.environ.get('USERNAME', ''),
        os.environ.get('PASSWORD', ''))
    return example_client


def example_resolve_address():
    """
    Assign example_client to the AvaTaxClient instance returned from.

    create_client().

    The address dictionary is used as a parameter in the resolve address
    request.
    This will be the address you have the geolocation information for.

    Call the resolve address on the example client, passing the address
    dictionary as an argument.
    """
    example_client = create_client()
    address = {
        'line1': '410 Terry Ave. North',
        'city': 'Seattle',
        'region': 'WA',
        'postal_code': '98109',
    }
    return example_client.resolve_address(address)
