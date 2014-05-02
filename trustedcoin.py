#!/usr/bin/python
import requests
import bitcoin
import time
import os
from bitcoin.deterministic import *
from bitcoin.transaction import *
from bitcoin.bci import *

apiurl = 'https://api.trustedcoin.com'
#/1/cosigner
#/1/cosigner/script_hash_address
#/1/cosigner/script_hash_address/send_start
#/1/cosigner/script_hash_address/send_finish
#/1/transaction/id
# contacts Example: [{"email" : "joe.random@example.com"}, {"sms" : "+14923922934"}, {"web" : "http://www.mysite.com/btc_callback"}]

def cosigner( primary_key, secondary_key, delay_in_seconds, policytype, contacts):
	payload = {"primary_key": primary_key, "secondary_key": secondary_key, "policy": {"type": policytype, "delay_in_seconds": delay_in_seconds, "contacts":  contacts}}
	headers = {'content-type': 'application/json'}
	url = apiurl + '/1/cosigner'
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	return r

def send_start(input_address,output_address,amount):
	payload = {'output_address': output_address, 'amount': int(amount)}
	url = apiurl + '/1/cosigner' + '/' + input_address + '/' + 'send_start'
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	return r

def send_finish(input_address,partial_transaction):
	payload = {'partial_transaction': partial_transaction}
	url = apiurl + '/1/cosigner' + '/' + input_address + '/' + 'send_finish'
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	r.text
	return r

def create2keys():
	directory = time.strftime("%Y-%m-%d-%H:%M:%S")
	if not os.path.exists(directory):
	    os.makedirs(directory)
	# create a random key 1
	k1 = random_key()
	#scrivo su file
	f = open(directory + '/k1.key','w')
	f.write(k1)
	f.close()
	#leggo il file
	f = open(directory + '/k1.key','r')
	k1 = f.read()
	f.close()
	print '_________________________'
	print 'secret key k1:           ' + k1
	print '_________________________'
	# create a random key 2
	k2 = random_key()
	#scrivo su file
	f = open(directory + '/k2.key','w')
	f.write(k2)
	f.close()
	#leggo il file
	f = open(directory + '/k2.key','r')
	k2 = f.read()
	f.close()
	print 'secret key k2:           ' + k2	
	print '_________________________'
	return directory




