"""Example for a create transaction request to record a new transaction in AvaTax."""
import os
from client import AvataxClient


def create_client():
    """
    Construct a new AvaTaxClient.

    The client defaults to the environment unless you specify "sandbox"

    'test app': The name of the application
    'ver 0.0': Version number of the application
    'test machine': Name of the machine on which this code is executing
    'sandbox': Logs you into the sandbox environment instead of production.

    Add credentials to configure client to use the specified security settings:
        username/password or
        accountId/LicenseKey or
        bearer token

    Your Avatax credentials should be set as environment variables prior to executing the request.

    Return example_client.
    """
    example_client = AvataxClient('test app',
                                  'ver 0.0',
                                  'test machine',
                                  'sandbox')
    example_client.add_credentials(
        os.environ.get('USERNAME', ''),
        os.environ.get('PASSWORD', ''))
    return example_client


def example_create_transaction():
    """
    Assign example_client to the AvataxClient instance returned from create_client().

    The tax document dictionary is used as a transaction model in the
    create transaction request.

    'addresses': Addresses for all lines in the document
    'commit': Set to false so the document will not be committed automatically
    'companyCode': Specifies the account's default company creating the transaction
    'currenyCode': The three-character ISO 4217 currency code for the transaction
    'customerCode': The client application customer reference code
    'date': The date on the invoice
    'description': Description for the transaction
    'lines': List of line items that will appear on the transaction (as a list of dictionary objects)
    'purchaseOrderNo': Purchase Order Number for the document
    'type': Specifies permanent transaction document that will be recorded

    Call the create_transaction method on the example_client, passing in the arugments None and tax_document, and return that response.
    """
    example_client = create_client()
    tax_document = {
        'addresses':
            {'SingleLocation':
                {'city': 'Irvine',
                 'country': 'US',
                 'line1': '123 Main Street',
                 'postalCode': '92615',
                 'region': 'CA'
                 }},
        'commit': False,
        'companyCode': 'DEFAULT',
        'currencyCode': 'USD',
        'customerCode': 'ABC',
        'date': '2017-04-12',
        'description': 'Yarn',
        'lines': [{'amount': 100,
                  'description': 'Yarn',
                   'itemCode': 'Y0001',
                   'number': '1',
                   'quantity': 1,
                   'taxCode': 'PS081282'}],
        'purchaseOrderNo': '2017-04-12-001',
        'type': 'SalesInvoice'}
    return example_client.create_transaction(None, tax_document)
