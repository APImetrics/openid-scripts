# openid-scripts
Scripts for getting set up with OpenID-based services, such as Open Banking.

If you intend to use JWT signing, you will need to have KMS turned on for your org, and a valid signing certificate 
uploaded to our KMS.

# Pages

1. [Open Banking Directory explorer](./Open%20Banking%20Directory%20explorer.ipynb)
1. [OpenID Connect inspect setup](./OpenID%20Connect%20inspect%20setup.ipynb)
1. [OAuth APIs - private_key_jwt](./OAuth%20APIs%20-%20private_key_jwt.ipynb)
1. [OBIE - Account and Transaction APIs](./OBIE%20-%20Account%20and%20Transaction%20APIs.ipynb)
1. [OBIE - Account Consent APIs](./OBIE%20-%20Account%20Consent%20APIs.ipynb)


## [Open Banking Directory explorer](./Open%20Banking%20Directory%20explorer.ipynb)
This page just helps exploring the ASPSPS JSON as obtained from the Open Banking API.

## [OpenID Connect inspect setup](./OpenID%20Connect%20inspect%20setup.ipynb)
This page lets you inspect a .well-known openid-connect JSON for some key information. 
It then lets you create a workflow that can be used for registering yourself as a client dynamically

## [OAuth APIs - private_key_jwt](./OAuth%20APIs%20-%20private_key_jwt.ipynb)
This page sets up the Auth Settings, API Calls and Workflows to allow you to authenticate against an Open ID Connect OAuth 2 endpoint.

## [OBIE - Account and Transaction APIs](./OBIE%20-%20Account%20and%20Transaction%20APIs.ipynb)
This page sets up OBIE Open Banking Account Consent APIs

## [OBIE - Account Consent APIs](./OBIE%20-%20Account%20Consent%20APIs.ipynb)
This page sets up OBIE Open Banking Account and Transaction APIs
