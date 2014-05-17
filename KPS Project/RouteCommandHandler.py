# -*- coding: utf-8 -*-
"""
Created on Wed May 07 16:15:46 2014

@author: Patrick
"""
import sqlite3

def getLocations():
    conn = sqlite3.connect("Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT location FROM locations')
    locs = [r[0] for r in c.fetchall()]
    conn.close()
    return locs
    
def insertLocations():
    # Only do this once. This method should otherwise never be used
    f = open('locations.txt','r')
    locations = []
    for line in f:
        locations.append((None,line.strip('\n')))
    conn = sqlite3.connect("Business.db")
    c = conn.cursor()
    c.executemany('INSERT INTO Locations VALUES (?,?)',locations)
    conn.commit()
    conn.close()

    
