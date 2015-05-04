import urllib


def crack(host):
    scheme, host = urllib.splittype(host)
    if scheme:
        host = urllib.splithost(host)[0]
    localhost = urllib.localhost()
    crackit = ' '.join([localhost, host])
    with open('C:\windows\system32\drivers\etc\hosts', 'a') as f:
        f.write('\n' + crackit)
