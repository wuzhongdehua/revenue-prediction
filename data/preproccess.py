#!/usr/bin/env python

import csv
import sys
import time
import datetime

city_names = {}
city_groups = {}
types = {}
rows_train = []
rows_test = []
rows = []


def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)  # skip the headers
        for row in reader:
            rows.append(row)
    return rows

def write_csv(filename, rows):
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for row in rows:
            writer.writerow(row[1:len(row)])            

def get_all_rows(train, test):

    global rows
    global rows_train
    global rows_test

    rows_train = read_csv(train)
    rows_test = read_csv(test)
    rows = rows_train + rows_test

    return rows

def make_dict(rows, columnId):
    d = {}
    for row in rows:
        k = row[columnId]
        if k in d: continue
        d[k] = len(d)

    return d

def scan_city_name(rows):
    return make_dict(rows, 2)

def scan_city_group(rows):
    return make_dict(rows, 3)

def scan_type(rows):
    return make_dict(rows, 4)

def transform_data(rows):

    global city_names
    global city_groups
    global types    

    for row in rows:        
        row[1] = datetime.datetime.strptime(row[1], '%m/%d/%Y').date()
        row[1] = int(time.mktime(row[1].timetuple()))
        row[2] = city_names[row[2]]
        row[3] = city_groups[row[3]]
        row[4] = types[row[4]] 
    return rows


if __name__ == '__main__':
    train = 'train.csv'
    test = 'test.csv'

    rows = get_all_rows(train, test)
    city_names = scan_city_name(rows)
    city_groups = scan_city_group(rows)
    types = scan_type(rows)

    print 'total citys = %s ' % len(city_names)    
    print 'city group = %s ' % city_groups
    print 'types = %s ' % types

    t = transform_data(rows_train)
    write_csv('train_cleaned.csv', t)

    t = transform_data(rows_test)
    write_csv('test_cleaned.csv', t)    
