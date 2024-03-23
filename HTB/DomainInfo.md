# Domain Information
Deals with all information about target’s presence in the internet.
- gather information and try to understand the target’s functionalities and which tech, structures are necessary for their services
- gathered passively, we try to remain hidden and navigate as “customers” or “visitors”

When passively gathering information, we can use 3rd-party services to understand the company better.
- more often than not, we can take note of the tech stack they use in their very own main website
	- we can do this if they just show their tech stack, or literally scan them

## Online Presence
lets assume a medium-sized company hired us to test their entire infrastructure from a black-box perspective
- we have only received a scope of targets
- obtain further info ourselves

The first point of presence we can review is the **`SSL certificate`**
- we can view this in firefox by clicking the lock icon in the search bar
- this allows us to see what domains are under the same certificate
- we can also view this in [`crt.sh`](https://crt.sh) which contains certificate transparency logs

The example in HTB shows the target to be `inlanefreight.com`, and a `crt.sh` search was done to enumerate their websites
- It is important to try and take note of websites locally hosted, not the ones that are hosted in 3rd-party like `AWS`
- `host` was done on each available website, and run through `shodan`
```bash
sycasec@htb[/htb]$ for i in $(cat subdomainlist);do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f4 >> ip-addresses.txt;done
sycasec@htb[/htb]$ for i in $(cat ip-addresses.txt);do shodan host $i;done
```
- the `shodan` part showed sum juicy information

Next, a `dig` on `inlanefreight.com` was performed
```bash
$ dig any inlanefreight.com
```
- not sure what `any` keyword does here
- **A** records: addresses that point to a subdomain
- **MX** records: mail server records that manage the email of the company, very interesting
	- held by google in the case of the HTB example, so skip
- **NS** records: name servers used to resolve **Fully Qualified Domain Name** (FQDN) to IP addresses
- **TXT** records: contain verification keys for different third-party providers 

## Cloud Resources 
We know that cloud is used to host company websites
- while they are secured by cloud providers internally, sysadmins can fuck this up
- Some resources can be accessed without authentication if configured incorrectly:
	- **`S3 buckets`**
	- **`blobs (azure)`**
	- **`cloud storage (Google Cloud Provider)`**

- we can search for this with google dorks technique:
	- `intext:<company name> inurl:amazonaws.com` → AWS
	- `intext:<company name> inurl:blob.core.windows.net` → Azure

we can dig deeper with GrayHatWarfare 
- sometimes SSH private and public keys are leaked
- we can also get information on files stored on the cloud storage

## Staff
- we can identify staff for potential spearphishing attacks on LinkedIn
- we have already done this with a certain company