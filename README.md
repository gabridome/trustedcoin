trustedcoin
===========

scripts to use trustedcoin service with Vitalik Buterin's pybitcointools
Hi,
This collection of scripts haven't got a name yet.
It is just a handful way to use Trustedcoin.com services (http://api.trustedcoin.com/#/) 
from python with the help of Vitalik Buterin's pybitcointools (https://github.com/vbuterin/pybitcointools).

First be sure to install Vitalik tools properly: sudo pip install bitcoin

Then the functions are in the trustedcoin.py script.

I have put a couple of scripts:

1.  createmultisig.py builds a multisig address (warning: you have to edit the contacts variable with YOUR reference).
	the script requires to be edited to add your references in the "contacts" variable

	and requires two parameters:
	* policytype (either "latency" or "approval" without the quotes)
	* Delay in seconds ie: 86400 for 1 day 

	example:    createmultisig.py latency 86400

	It will create a folder named as the generated address (es: 3guGJGIHImceop..) in which it will store the 2 keys randomly generated.
	This address has a policy that when you spend fron it Trustedcoin will send you a message with which you can cancel the expence.

2 ones you have your multisig addres which incorporates you security policy you can actually:
	2.1 Send some satoshi on the address
	2.2 when the address has a non empty balance you can spend with send.py script.
		This script will ask trustedcoin to initiate a multisig transaction from the multisig address you specify, the choosen destination and the amount
		Trustedcoin will replyin the background with a single-signed transaction. The script will sign it with one of your two keys and resend the transaction to Trusted coins.

I'm a great bitcoin believer but an horrible programmer so feel free to change everything.

Thanks to Vitalik Buterik for his incredible job.
Thanks to James D'Angelo for his tutorials and suggestions (http://www.youtube.com/channel/UCgo7FCCPuylVk4luP3JAgVw).

Warning: Trustedcoin is not free! every transaction costs 50 000 satoshis. Consider it when you calculate your transactions.

Just for the taste of it drop a tip only if you have apreciated.
	
	3GtUeJjuFQDnfFzG8F8H3fsVH1JZkryHQJ

Gabridome
