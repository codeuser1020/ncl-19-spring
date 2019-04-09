#  RADIUS

### We have been using RADIUS to authenticate users on our network. Review a packet capture to see what information an attacker could obtain if they intercept our traffic.

1. What is the IP address of the NAS?
Doing some [research on how the Radius protocol works](http://marker.to/0o9gsj) we can see that it involves communication between a network access server (NAS) and a Radius server. Also we can look to the network flow to see which IP we are looking for.

![flow](https://upload.wikimedia.org/wikipedia/commons/5/50/Drawing_RADIUS_1812.svg)

So we want the source address of an Access-Request packet.
<details>
    <summary>Flag</summary>
    
        10.0.252.13
</details>

2. What is the IP address of the RADIUS server?
Based on the previous question we know the destination of the same packet is the IP of the server.
<details>
    <summary>Flag</summary>

        10.0.252.42
</details>

3. How many requests were accepted by the RADIUS server?
Applying the filter `radius.code == 2` to the Wireshark filter gives us the number of requests accepted (look for number of packets displayed in bottom right corner).
<details>
    <summary>Flag</summary>

        84
</details>

4. What authentication scheme is being used with RADIUS?
The [wikipedia page for Radius](http://marker.to/2xT3a5) mentions a few different types of authentication schemes typically used in Radius including  PAP, CHAP and EAP. I decided to use the search funciton in Wireshark to look for each of these as strings within the `Packet details` and one of them is found within the packets.
<details>
    <summary>Flag</summary>

        EAP
</details>

5. How many access requests were made by "hana.harb"?
At first I searched for the string `hana.harb` in the `Packet details`. Right clicking on one of the results I use the `Apply as Filter`  option to only show packets relating to this username by applying the filter `radius.User_Name == "hana.harb"`. Since they are only asking for access **requests** I added a second filter with the && logical opperator `radius.User_Name == "hana.harb" && radius.code == 1`. The number of displayed packets in the bottom right is the flag.
<details>
    <summary>Flag</summary>

        22
</details>

6. What is the MAC address for the device owned by "sally.berro"?
This can be a bit missleading since they aren't asking for the MAC address of the device that sent the packet. Looking though one of the request packets, you can see two mac addresses for the attributes `radius.Called_Station_Id` and `radius.Calling_Station_Id`. Reading the [RFC for the radius protocol](https://tools.ietf.org/html/rfc2865#section-5.31) tells us we want the calling station ID.
<details>
    <summary>Flag</summary>

        30-07-4d-53-77-f5
</details>

7. How many different access points received access requests?
Based on the previous question we know we need the number of unique mac addresses that were called. I decided to write a [python script](radius.py) using [PyShark](https://kiminewt.github.io/pyshark/) to create a set of these mac addresses to get the count of unique devices that received the access requests.
<details>
    <summary>Flag</summary>

        43
</details>
