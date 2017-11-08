# coding: utf-8

# Compassionate Caching inspired by 
# http://lethain.com/an-introduction-to-compassionate-screenscraping/
import requests, time, re, random, hashlib

last_fetched_at = None

def fetch(url):
    """Load the url compassionately."""
    
    global last_fetched_at
    
    url_hash = hashlib.sha1(url.encode()).hexdigest()
    filename = 'cache-file-{}'.format(url_hash)
    try:
        with open(filename, 'r') as f:
            result = f.read()
            if len(result) > 0:
                print("Retrieving from cache:", url)
                return result
    except:
        pass
    
    print("Loading:", url)
    wait_interval = random.randint(3000,10000)
    if last_fetched_at is not None:
        now = time.time()
        elapsed = now - last_fetched_at
        if elapsed < wait_interval:
            time.sleep((wait_interval - elapsed)/1000)
        
    rsp = requests.get(url)
    last_fetched_at = time.time()
    result = (rsp.text)
    with open(filename, 'w') as f:
        f.write(result)
    return result