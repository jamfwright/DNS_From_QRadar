__author__ = 'jfwright'

'''

DNS Decode QRadar

This script will take the base64 flow of a DNS interaction
and convert it into a human readable DNS query/response.

QRadar will generate a base64 payload that can be used
with this script.

'''

import dnslib
import binascii


payload = raw_input("Paste the base64 DNS payload here:  ")

binary_payload = binascii.a2b_base64(payload)

translated_payload = dnslib.DNSRecord.parse(binary_payload)

print(translated_payload)
