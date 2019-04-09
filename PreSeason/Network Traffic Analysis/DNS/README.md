# DNS

### We think that a hacker was able to modify some of our DNS records. Analyze a packet capture that we have created from running DNS queries.

1. What organization operates the DNS resolver used in this capture?
For this question, I took the IP address of the DNS server (209.244.0.3) and did a quick google search leading me to the [answer](http://marker.to/kdH0MV).
2. What is the IPv4 address responsible for www.cityinthe.cloud?
Based on the [DNS record types](https://ns1.com/resources/dns-types-records-servers-and-queries) we know that we are looking for an Address Mapping record (A Record) for the website `www.cityinthe.cloud`. Expanding the answer section within wireshark gives us the answer `dns.a`.
<details>
    <summary>Flag</summary>
    
        232.135.80.85
</details>

3. What is the IPv6 address responsible for www.cityinthe.cloud?
This would be a IP Version 6 Address record (AAAA Record). The response packet can be expanded to find the answer.
<details>
    <summary>Flag</summary>

        c2d1:e1b:5bdd:3fbd:addd:3793:6078:ad97
</details>

4. Who is the mail provider for cityinthe.cloud?
5. What is the handle of the hacker that tampered with the DNS records?
For this question you just have to search through and look through and find anything weird about any of the packets. At first I thought the answer was in the request for the `cityinthe.clod`.  Eventually I realized it was weird to see a TXT request, and within the answer was the flag within the `dns.txt`.
<details>
    <summary>Flag</summary>

        zer0dark0 was here
</details>

6. What IP address was queried for reverse lookup?
Since it is a reverse lookup we are looking for a PTR Record. A key part of this question is knowing the [format](https://simpledns.com/help/ptr-records) of these requests as the IP is reversed and then appended to the string `.in-addr.arpa`. With this information the flag is found in the request of the PTR lookup `10.10.174.108.in-addr.arpa`.
<details>
    <summary>Flag</summary>

        108.174.10.10
</details>

7. What organization operates the IP adddress that was queried for reverse lookup?
The `dns.ptr.domain_name` value from the PTR response packet answer reveals the company name in the resolved address.
<details>
    <summary>Flag</summary>

        LinkedIn
</details>

8. Which FQDN is responsible for the majority of TCP SIP traffic to cityinthe.cloud?
To find the answer for this question we have to look at the answers from the SRV packet response for the _sip.**_tcp**.cityinthe.cloud address. Based on the [SRV record format](https://en.wikipedia.org/wiki/SRV_record) we are looking for the answer with the lowest priority and highest weight.
```
_sip._tcp.cityinthe.cloud: type SRV, class IN, priority 10, weight 40, port 5060, target sip1.cityinthe.cloud
_sip._tcp.cityinthe.cloud: type SRV, class IN, priority 20, weight 0, port 5060, target sip3.cityinthe.cloud
_sip._tcp.cityinthe.cloud: type SRV, class IN, priority 10, weight 60, port 5060, target sip2.cityinthe.cloud
```
<details>
    <summary>Flag</summary>

        sip2.cityinthe.cloud
</details>

9. Which FQDN is the backup for TCP SIP traffic if all other servers are not available for cityinthe.cloud?
<details>
    <summary>Flag</summary>

        sip3.cityinthe.cloud
</details>
