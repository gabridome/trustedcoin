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

input_address = sys.argv[1]
output_address = sys.argv[2]
amount = sys.argv[3]
# Trusted coin request a 50 000 satoshis fee so be sure to have them overall the address balance.


#send a transaction to have the script unsigned:
r = send_start(input_address, output_address, amount)
print r.text

redeem_script = str(r.json()['inputs'][0]['redeemScript'])
scriptPubKey = str(r.json()['inputs'][0]['scriptPubKey'])
unsigned_transaction = str(r.json()['unsigned_transaction'])
vout = r.json()['inputs'][0]['vout']
txid = str(r.json()['inputs'][0]['txid'])

#recovering the private key from the directory
f = open(input_address + '/k1.key', 'r')
k1 = f.read()
f.close()
k1
#signing the unsigned_transaction with one key (k1):
sig1 = multisign(unsigned_transaction,vout,redeem_script,k1)
partial_transaction = apply_multisignatures(unsigned_transaction,vout,redeem_script, sig1)

print 'signed by me transaction:' 
print partial_transaction
# mando la transazione firmata a trustedcoins:

r = send_finish( input_address,partial_transaction )
r.text
transaction_status_id = str(r.json()['transaction_status_id'])

# per avere informazioni sull stato della transazione:
statusrequest = requests.get('https://api.trustedcoin.com//1/transaction/' + transaction_status_id)

status = str(statusrequest.json()['status'])
tx_id =  str(statusrequest.json()['tx_id'])

print 'The transaction ' + tx_id + 'is ' + status

