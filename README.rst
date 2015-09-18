eth_alarm
==============================

Information
-----------

* Primary contract address.
  * authorized call sender address
  * unauthorized call sender address
* Contract source code.
* Contract ABI.
* Contract stub contract.

Concepts
--------

* Contract code can be verified against the published source code
* Service is 100% operated within the boundaries of the ethereum network.
* Trustless
  * 100% public api endpoints with no special access to contract creator.
* Supports calls that can be trusted to execute privileged functions (via authorized accounts).
* Easy to use from within your contracts (via contract ABI)
* Easy to use from javascript (using web3) or python (using populus)
* Get paid to execute scheduled calls.
* Public Property
  * Cannot be suicided

Features
--------

* Schedule any contract function call for a specified block number in the future.
* Designate specific addresses as authorized schedulers and subsequently be
  able to trust function calls that were scheduled by them.

Quick Introductions
-------------------

* Example use from a contract
  * trust fund contract.
  * lottery?
* Example use from web3
* Example use from populus

Security Vulnerability Rewards
------------------------------

* Ability to execute a function call without paying for it (caller doesn't get
  paid but the function call still gets executed)
* Ability to extract funds from another address's account.
* Ability to force another account to pay for your function call.
