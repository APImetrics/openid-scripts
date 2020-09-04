# openid-scripts
Scripts for getting set up with OpenID-based services, such as Open Banking.

If you intend to use JWT signing, you will need to have KMS turned on for your org, and a valid signing certificate 
uploaded to our KMS.

# Pages

1. [Open Banking Directory explorer](Open Banking Directory explorer.ipynb)
1. [OpenID Connect inspect setup](OpenID Connect inspect setup.ipynb)
1. [OAuth APIs - private_key_jwt](OAuth APIs - private_key_jwt.ipynb)
1. [OBIE - Account and Transaction APIs](OBIE - Account and Transaction APIs.ipynb)
1. [OBIE - Account Consent APIs](OBIE - Account Consent APIs.ipynb)


## [Open Banking Directory explorer](Open Banking Directory explorer.ipynb)
This page just helps exploring the ASPSPS JSON as obtained from the Open Banking API.

## [OpenID Connect inspect setup](OpenID Connect inspect setup.ipynb)
This page lets you inspect a .well-known openid-connect JSON for some key information. 
It then lets you create a workflow that can be used for registering yourself as a client dynamically

## [OAuth APIs - private_key_jwt](OAuth APIs - private_key_jwt.ipynb)
This page sets up the Auth Settings, API Calls and Workflows to allow you to authenticate against an Open ID Connect OAuth 2 endpoint.

## [OBIE - Account and Transaction APIs](OBIE - Account and Transaction APIs.ipynb)
This page sets up OBIE Open Banking Account Consent APIs

## [OBIE - Account Consent APIs](OBIE - Account Consent APIs.ipynb)
This page sets up OBIE Open Banking Account and Transaction APIs
