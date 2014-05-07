#!/usr/bin/env python

import sqlite3 as lite
import sys


class login():
    def __init__(self):
        self.con = None
        self.cur = None
    def conn(self):
        try:
            self.con = lite.connect("../Database/Users.db")
        except lite.Error, e:
            print("Error %s:" % e.args[0])
            sys.exit(1)
    
    def login(self, username, password):
        self.cur = self.con.cursor()
        self.cur.execute("SELECT * FROM UserDetails")
        while True:
            row = self.cur.fetchone()
            if row == None:
                #first 0 denotes failure, second 1 denote user not exist
                return 0, 1
            if username == row[1]:
                if password == row[2]:
                    if row[3] == 1:
                    #first 1 denotes success, second 1 denotes manager
                        return 1, 1
                    else:
                    #first 1 denotes success, second 1 denotes employee
                        return 1, 0
                else:
                    #first 0 denotes failure, second 0 denote wrong password
                    return 0, 0
        

if __name__ == "__main__":
    user = login()
    user.conn()
    x, y = user.login("a", "123456")
    print x, y
