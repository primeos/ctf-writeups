# Day 05: OSINT 1

Challenge text:
```
It's all about transparency

Santa has hidden your daily present on his server, somewhere on port 443.
Start on https://www.hackvent.org and follow the OSINT traces.
```

OSINT (open-source intelligence) was the key/hint.
This challenge was actually pretty cool and interesting.

Visiting [https://www.hackvent.org/](https://www.hackvent.org/) resulted in the
following message:
```
The flag for day 05 is already here, but not exactly here.
Watch out for other virtual hosts and find the right place.
```

`->` Need to find another virtual host.

## First attempt: Use DNS (didn't work)

- A record: 80.74.140.188 (same result)
- PTR record: urb80-74-140-188.ch-meta.net. (same result)
- No AAAA record

## Second attempt: HTTPS `->` Use CT (certificate-transparency) logs

I used the following tool
[https://crt.sh/?q=%25.hackvent.org](https://crt.sh/?q=%25.hackvent.org):
```
Identity LIKE '%.hackvent.org'
crt.sh ID	 Logged At   	Not Before	Not After	Identity	Issuer Name
990029827	2018-11-30	2018-11-30	2019-02-28	osintiscoolisntit.hackvent.org	C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3
990029337	2018-11-30	2018-11-30	2019-02-28	osintiscoolisntit.hackvent.org	C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3
989958160	2018-11-30	2018-11-30	2019-02-28	www.hackvent.org	C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3
989947411	2018-11-30	2018-11-30	2019-02-28	www.hackvent.org	C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3
```

(I've tried "hackvent.%" first but that didn't work.)

## Solution

- Domain: osintiscoolisntit.hackvent.org
- Flag: HV18-0Sin-tI5S-R34l-lyC0-oo0L

## Other interesting stuff

- [https://www.shodan.io/host/80.74.140.188](https://www.shodan.io/host/80.74.140.188)
- [https://censys.io/ipv4/80.74.140.188](https://censys.io/ipv4/80.74.140.188)
  - 21/FTP `->` 220 Welcome to Santas FTP-Server `->` TODO

## Really good OSINT site (tool collection)

- [https://osintframework.com/](https://osintframework.com/)
