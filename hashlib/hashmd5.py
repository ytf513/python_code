# hashlib md5
import hashlib

inputStr=raw_input("Input the String you want to transfer md5:")

print "The md5 code:%s" % hashlib.md5(inputStr).hexdigest()
