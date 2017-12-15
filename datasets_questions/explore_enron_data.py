#!/usr/bin/python
from __future__ import division
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data)
count =0
for key in enron_data:
    content = enron_data[key]
    if content['poi']==1:
        count = count +1

print count

print enron_data['PRENTICE JAMES']['total_stock_value']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
salary_num = 0
email_num =0
for key in enron_data:
    content = enron_data[key]
    if content['salary']!='NaN':
        salary_num = salary_num +1

print salary_num

for key in enron_data:
    content = enron_data[key]
    if content['email_address']!='NaN':
        email_num = email_num +1

print email_num
total_payments_num =0
for key in enron_data:
    content = enron_data[key]
    if content['total_payments']=='NaN':
        total_payments_num = total_payments_num +1

print total_payments_num
a = 0
for key in enron_data:
    content = enron_data[key]
    if content['poi']==1 and content['total_payments']=='NaN':
        a = a +1

print a