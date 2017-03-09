#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
Adds a sequential number of users into a test database
with username: newusern and password newusern

Not for production usage
"""

import MySQLdb


hostname = # FILL IN 
username = # FILL IN 
password = # FILL IN 



# Simple routine to run a query on a database and print the results:
def doQuery( conn, n_users ) :
    cur = conn.cursor()

    try:
        for i in range(0,n_users):
            cur.execute("""CREATE USER \'newuser%i\'@\'localhost\' IDENTIFIED BY \'password%i\'""" % (i,i) )
            cur.execute( """GRANT ALL PRIVILEGES ON * . * TO \'newuser%i\'@\'localhost\'""" % i )
            cur.execute( """FLUSH PRIVILEGES""" )
    except MySQLdb.Error, e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print ("MySQL Error: %s" % str(e))


if __name__ == '__main__':
    print("Using mysql.connector…")
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, 20)
    doQuery( myConnection )
    myConnection.close()





