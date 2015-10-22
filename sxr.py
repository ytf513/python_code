## sxr.py:xml-rpc server code
from SimpleXMLRPCServer import SimpleXMLRPCServer
def happy():
    print "I play Python.!"
    sxr=SimpleXMLRPCServer(("", 8080), allow_none=True)
    sxr.register_function(happy)
    sxr.serve_forever()
