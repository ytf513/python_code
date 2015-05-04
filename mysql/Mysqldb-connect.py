import MySQLdb

try:
	conn=MySQLdb.connect(host="127.0.0.1",user="alex",passwd="alex",db="alex",port=3306)
	cur=conn.cursor()
	cur.execute('select * from alex.pet')
	print "connected to the database named alex.pet"
	cur.close
	conn.close
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0],e.args[1])
	
