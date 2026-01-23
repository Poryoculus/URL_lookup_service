
MALWARE_URLS = {
    "http://bad.com/malware",
    "http://evil.com/phish",
    "http://notsecure.com/attack",
    "http://notsoftserver.com/hack",
}

#This url are just test data and will be changed by a json in the local 
#or even a     return not is_malware(url)

def is_malware(url: str) -> bool:
    return url in MALWARE_URLS
