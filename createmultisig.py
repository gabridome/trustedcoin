#!/usr/bin/python
import sys
import requests
import bitcoin
import time
import os
from bitcoin.deterministic import *
from bitcoin.transaction import *
from bitcoin.bci import *
from trustedcoin import *

# syntax: contacts = [{"email":"email1@somedomain.com"},{"email":"email2@somedomain.com"},{"sms":"+12345678910"},{"web":"https://somecall-back.com"}]

contacts = [{"email":"gabriele.domenichini@gdtre.net"},{"email":"gabridome@gmail.com"}]

if len(sys.argv) <2:
	policytype = raw_input('Policy type? Latency or approval: ')
	delay_in_seconds = raw_input('seconds before validating the transaction or to confirm the expense: ')
	response = raw_input('\nCreation of a multisig address with a ' + policytype + ' policy\n and ' + delay_in_seconds + ' seeconds of delay.\nIs it OK (Y/N)? ')
	if response == 'n':
		sys.exit('\n    Usage: ' + sys.argv[0] + ' policytype delay_in_seconds\n\n    where policy type can be latency or approval\n\n    Es: ' + sys.argv[0] + ' approval 7200' + '\n')

print len(sys.argv)
print sys.argv[1]
print sys.argv[2]

if len(sys.argv) == 3:
	if sys.argv[1] not in ('latency' , 'approval'):
		sys.exit('\n    The policy type can be only "latency" or "approval"' + '\n')
	policytype = sys.argv[1]
	delay_in_seconds = sys.argv[2]
print 'policy: ' + policytype
print 'delay_in_seconds: ' + delay_in_seconds

# Trusted coin request a 50 000 satoshis fee so be sure to have them overall the address balance.

# "type": "latency" oppure "allow"

# Take two public keys from the files and put it into the variables p3 and p2
directory = create2keys()
f = open(directory + '/k1.key','r')
k1 = f.read()
f.close()
global p1
p1 = privtopub(k1)
print 'public key p1:           ' + p1
print '_________________________'

f = open(directory + '/k2.key','r')
k2 = f.read()
f.close()
global p2
p2 = privtopub(k2)
print 'public key p2:           ' + p2
print '_________________________'

#Send two public key to trustedcoins and receive the script, the the third public key and the address. It memorize the necessary data in variables
r = cosigner(p1,p2,delay_in_seconds,policytype,contacts)
address = str(r.json()['address'])
script = str(r.json()['script'])
trustedcoin_pubkey = str(r.json()['trustedcoin_pubkey'])
trustedcoin_fee_address = str(r.json()['trustedcoin_fee_address'])
trustedcoin_fee = str(r.json()['trustedcoin_fee'])
balance = str(r.json()['balance'])
helpstring = str(r.json()['help'])

print 'generated p2sh address:  ' + address
print '_________________________'
print 'primary public key :     ' + p1
print '_________________________'
print 'secondary public key:    ' + p2
print '_________________________'
print 'generated public key:    ' + trustedcoin_pubkey
print '_________________________'
print 'script:'
print script

f = open(directory + '/r.json', 'w')
f.write(r.text)
f.close()
os.rename(directory, address)

