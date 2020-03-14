# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:19:29 2020

@author: User
"""

def digit_only(duplications):       #assure meet requirements for number of digits or else set to null
    for i in range(len(duplications)):
        if len(duplications[i]['ISSN']) != 8:
            duplications[i]['ISSN'] = ''
        if len(duplications[i]['e-ISSN']) != 8:
            duplications[i]['ISSN'] = ''
        if len(duplications[i]['ISBN']) not in [10,13]:   
            duplications[i]['ISBN'] = ''
        if len(duplications[i]['e-ISBN']) not in [10,13]:   
            duplications[i]['ISBN'] = ''
    return duplications

def info_compare(code1, code2): #compare two info to see if identical
    repeated = []
    repeated = set(code1) & set(code2)
    return repeated

import csv
with open ('library-titles.csv', 'r',encoding='utf8') as f:
     f_read = csv.DictReader(f)          #read all data from input file
     data = [dict(x) for x in f_read]    #convert data into dictionary

data = sorted(data, key = lambda i: i['TITLE'])     #sort the datas according to title alphabetically 

issn_read = []
eissn_read = []
isbn_read = [] 
eisbn_read = []

#store different datas in own list and remove '-' for direct comparison
issn_read = [data[i]['ISSN'].replace('-','') for i in range(len(data))] 
eissn_read = [data[i]['e-ISSN'].replace('-','') for i in range(len(data))]
isbn_read = [data[i]['e-ISBN'].replace('-','') for i in range(len(data))]
eisbn_read = [data[i]['e-ISBN'].replace('-','') for i in range(len(data))]
issn_eissn = info_compare(issn_read,eissn_read)     #compare and find same issn & eissn
isbn_eisbn = info_compare(isbn_read,eisbn_read)     #compare and find same isbn & eisbn

repeated_title = []
repeated_title_info = []
for i in range(len(data)):          #find books with the same titles
    if data[i]['TITLE'] == data[i-1]['TITLE']:
        repeated_title.append(data[i]['TITLE'])
        repeated_title_info.append(data[i])

repeated_code = []
repeated_code_info = []         #retrieve full info of books with same issn/eissn AND same isbn/eisbn
for i in range(len(data)):
    if data[i]['ISSN'] in issn_eissn or data[i]['e-ISSN'] in issn_eissn and data[i]['ISBN'] in isbn_eisbn or data[i]['e-ISBN'] in isbn_eisbn:
        repeated_code.append(data[i]['ISSN'])
        repeated_code.append(data[i]['ISBN'])
        repeated_code_info.append(data[i])

duplication = []        #retrieve full info of books with same issn/eissn AND same isbn/eisbn AND same name
duplication = [x for x in repeated_title_info if x in repeated_code_info]
digit_only(duplication)     #filter out number codes that don't meet requirements

'''
keys = duplication[0].keys()
with open('duplications.csv', 'wb') as o:
    dict_writer = csv.DictWriter(o, keys)
    dict_writer.writeheader()
    dict_writer.writerows(duplication)
'''