
malware_urls = {
    "http://bad.com/malware",
    "http://evil.com/phish",
    "http://notsecure.com/attack",
    "http://notsoftserver.com/hack",
        }
#This url are just test data and will be changed by a json in the local 
#or even a     return not is_malware(url)

def is_malicious_url(url: str) -> bool:
    return url in malware_urls

