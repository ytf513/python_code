# happy.py xml-rpc client code
from xmlrpclib import ServerProxy
sp = ServerProxy("http://localhost:8080")
sp.happy()
