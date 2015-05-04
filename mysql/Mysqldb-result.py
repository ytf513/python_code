import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',user='alex',passwd='alex',port=3306)
    cur=conn.cursor()

    conn.select_db('alex')

    count=cur.execute('select * from pet')
    print 'There has %s rows record.' % count

    result=cur.fetchone()
    #print result

    results=cur.fetchmany(5)
    for r in results:
        print r


    print '=='*10
    cur.scroll(0,mode='absolute') #mode='relative'

    results=cur.fetchall()
    for r in results:
        print r

    cur1=conn.cursor()
    count1=cur1.execute("select * from pet where owner='alex'")
    print count1
    
    conn.commit()
    cur.close()
    conn.close()

except MySQLdb.Error,e:
    print "Mysql Error %d:%s" % (e.args[0],e.args[1])
