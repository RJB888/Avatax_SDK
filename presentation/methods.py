"""."""


def ping():
    """."""
    url = 'https://sandbox-rest.avatax.com/api/v2/utilities/ping'
    verb = 'GET'
    response = {
      "version": "17.12.0-147",
      "authenticated": True,
      "authenticationType": "AccountIdLicenseKey",
      "authenticatedUserName": "anonymous@2000188004",
      "authenticatedUserId": 247126,
      "authenticatedAccountId": 2000188004
    }
    return url, verb, response


def create():
    """."""
    url = 'https://sandbox-rest.avatax.com/api/v2/transactions/create'
    verb = 'POST'
    request = {
      "lines": [
        {
          "number": "1",
          "quantity": 1,
          "amount": 100,
          "taxCode": "PS081282",
          "itemCode": "Y0001",
          "description": "Yarn"
        }
      ],
      "type": "SalesInvoice",
      "companyCode": "DEFAULT",
      "date": "2017-12-14",
      "customerCode": "ABC",
      "purchaseOrderNo": "2017-12-14-001",
      "addresses": {
        "singleLocation": {
          "line1": "2000 Main Street",
          "city": "Irvine",
          "region": "CA",
          "country": "US",
          "postalCode": "92614"
        }
      },
      "commit": False,
      "currencyCode": "USD",
      "description": "Yarn"
    }
    response = {
      "id": 382539246,
      "code": "51ebf143-ffbf-4c22-babb-d06811ff741b",
      "companyId": 474615,
      "date": "2017-12-14",
      "paymentDate": "1900-01-01",
      "status": "Committed",
      "type": "SalesInvoice",
      "batchCode": "",
      "currencyCode": "USD",
      "customerUsageType": "",
      "entityUseCode": "",
      "customerVendorCode": "ABC",
      "exemptNo": "",
      "reconciled": False,
      "purchaseOrderNo": "2017-12-14-001",
      "referenceCode": "",
      "salespersonCode": "",
      "taxOverrideType": "None",
      "taxOverrideAmount": 0,
      "taxOverrideReason": "",
      "totalAmount": 100,
      "totalExempt": 100,
      "totalDiscount": 0,
      "totalTax": 0,
      "totalTaxable": 0,
      "totalTaxCalculated": 0,
      "adjustmentReason": "NotAdjusted",
      "adjustmentDescription": "",
      "locked": False,
      "region": "CA",
      "country": "US",
      "version": 1,
      "softwareVersion": "17.11.2.11",
      "originAddressId": 940553652,
      "destinationAddressId": 940553652,
      "exchangeRateEffectiveDate": "2017-12-14",
      "exchangeRate": 1,
      "isSellerImporterOfRecord": False,
      "description": "Yarn",
      "businessIdentificationNo": "",
      "modifiedDate": "2017-12-21T17:17:56.16",
      "modifiedUserId": 247126,
      "taxDate": "2017-12-14T00:00:00",
      "lines": [
        {
          "id": 1335069561,
          "transactionId": 382539246,
          "lineNumber": "1",
          "boundaryOverrideId": 0,
          "customerUsageType": "",
          "entityUseCode": "",
          "description": "Yarn",
          "destinationAddressId": 940553652,
          "originAddressId": 940553652,
          "discountAmount": 0,
          "exemptAmount": 100,
          "exemptCertId": 0,
          "exemptNo": "",
          "isItemTaxable": True,
          "isSSTP": False,
          "itemCode": "Y0001",
          "lineAmount": 100,
          "quantity": 1,
          "ref1": "",
          "ref2": "",
          "reportingDate": "2017-12-14",
          "revAccount": "",
          "sourcing": "Origin",
          "tax": 0,
          "taxableAmount": 0,
          "taxCalculated": 0,
          "taxCode": "PS081282",
          "taxCodeId": 38007,
          "taxDate": "2017-12-14",
          "taxEngine": "",
          "taxOverrideType": "None",
          "businessIdentificationNo": "",
          "taxOverrideAmount": 0,
          "taxOverrideReason": "",
          "taxIncluded": False,
          "details": [
            {
              "id": 2491481707,
              "transactionLineId": 1335069561,
              "transactionId": 382539246,
              "addressId": 940553652,
              "country": "US",
              "region": "CA",
              "stateFIPS": "06",
              "exemptAmount": 0,
              "exemptReasonId": 6,
              "inState": True,
              "jurisCode": "06",
              "jurisName": "CALIFORNIA",
              "jurisdictionId": 5000531,
              "signatureCode": "AGAM",
              "stateAssignedNo": "",
              "jurisType": "STA",
              "nonTaxableAmount": 100,
              "nonTaxableRuleId": 0,
              "nonTaxableType": "NexusRule",
              "rate": 0,
              "rateRuleId": 0,
              "rateSourceId": 0,
              "serCode": " ",
              "sourcing": "Origin",
              "tax": 0,
              "taxableAmount": 0,
              "taxType": "Sales",
              "taxName": "CA STATE TAX",
              "taxAuthorityTypeId": 45,
              "taxRegionId": 2127863,
              "taxCalculated": 0,
              "taxOverride": 0,
              "rateType": "General",
              "rateTypeCode": "G",
              "taxableUnits": 0,
              "nonTaxableUnits": 100,
              "exemptUnits": 0,
              "unitOfBasis": "PerCurrencyUnit"
            }
          ],
          "lineLocationTypes": [
            {
              "documentLineLocationTypeId": 1232205831,
              "documentLineId": 1335069561,
              "documentAddressId": 940553652,
              "locationTypeCode": "PointOfOrderOrigin"
            },
            {
              "documentLineLocationTypeId": 1232205830,
              "documentLineId": 1335069561,
              "documentAddressId": 940553652,
              "locationTypeCode": "PointOfOrderAcceptance"
            },
            {
              "documentLineLocationTypeId": 1232205829,
              "documentLineId": 1335069561,
              "documentAddressId": 940553652,
              "locationTypeCode": "ShipTo"
            },
            {
              "documentLineLocationTypeId": 1232205828,
              "documentLineId": 1335069561,
              "documentAddressId": 940553652,
              "locationTypeCode": "ShipFrom"
            }
          ],
          "parameters": {}
        }
      ],
      "addresses": [
        {
          "id": 940553652,
          "transactionId": 382539246,
          "boundaryLevel": "Address",
          "line1": "2000 Main St",
          "line2": "",
          "line3": "",
          "city": "Irvine",
          "region": "CA",
          "postalCode": "92614-7202",
          "country": "US",
          "taxRegionId": 2127863,
          "latitude": "33.684689",
          "longitude": "-117.851495"
        }
      ],
      "locationTypes": [
        {
          "documentLocationTypeId": 98223671,
          "documentId": 382539246,
          "documentAddressId": 940553652,
          "locationTypeCode": "PointOfOrderOrigin"
        },
        {
          "documentLocationTypeId": 98223670,
          "documentId": 382539246,
          "documentAddressId": 940553652,
          "locationTypeCode": "PointOfOrderAcceptance"
        },
        {
          "documentLocationTypeId": 98223669,
          "documentId": 382539246,
          "documentAddressId": 940553652,
          "locationTypeCode": "ShipTo"
        },
        {
          "documentLocationTypeId": 98223668,
          "documentId": 382539246,
          "documentAddressId": 940553652,
          "locationTypeCode": "ShipFrom"
        }
      ],
      "summary": [
        {
          "country": "US",
          "region": "CA",
          "jurisType": "State",
          "jurisCode": "06",
          "jurisName": "CALIFORNIA",
          "taxAuthorityType": 45,
          "stateAssignedNo": "",
          "taxType": "Sales",
          "taxName": "CA STATE TAX",
          "rateType": "General",
          "taxable": 0,
          "rate": 0,
          "tax": 0,
          "taxCalculated": 0,
          "nonTaxable": 100,
          "exemption": 0
        }
      ],
      "parameters": {}
    }
    return url, verb, request, response


def commit():
    """."""
    url = 'https://sandbox-rest.avatax.com/api/v2/companies/{companyCode}/transactions/{transactionCode}/commit'
    verb = 'POST'
    request = {"commit": True}
    response = {}
    return url, verb, request, response



