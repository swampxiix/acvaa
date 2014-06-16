import urllib

def wiley_auth():
    wiley_url = 'http://onlinelibrary.wiley.com/login-proxy-tps?targetURL=http://onlinelibrary.wiley.com/resolve/doi?DOI=10.1111/(ISSN)1467-2995&domain=acvaa.org'
    response = urllib.urlopen(wiley_url)
    redirect = response.read()
    return redirect
