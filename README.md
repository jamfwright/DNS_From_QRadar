# DNS_From_QRadar
Convert the DNS flow payloads from base64 to DNS records.

This Python script decodes the Base64 payload of a DNS interaction into a standard DNS record. This works with the Base64 payload provided by QRadar Qflows, but should work with any Base64 encoded DNS packet payloads.

Usage:

The usage and function of this program are rather simple. All you need to do is run the Python script. When prompted paste in the Base64 payload from a QRadar flow record. The script uses dnslib to then output the DNS payload in a readable manner.

This is useful for incident response and forensics.
