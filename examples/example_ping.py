"""Example of ping method to test connectivity and version of the service."""
import os
from client import AvaTaxClient


def create_client():
    """Construct a new AvaTaxClient in a Sandbox Environment.

    'test app': The name of the application
    'ver 0.0': Version number of the application
    'test machine': Name of the machine on which this code is executing
    'sandbox': To connect to the sandbox environment instead of production

    """
    example_client = AvaTaxClient('test app',
                                  'ver 0.0',
                                  'test machine',
                                  'sandbox')
    example_client.add_credentials(
        os.environ.get('USERNAME', ''),
        os.environ.get('PASSWORD', ''))
    return example_client


def example_ping():
    """
    Assign example_client to the AvaTaxClient instance returned from.

    create_client().

    Call ping on the example_client and return the response.
    """
    example_client = create_client()
    return example_client.ping()
