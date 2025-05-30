# from faker import Faker
from flask import Flask, jsonify

def abc():
    print('Started')

    domains = ["aaa", "bbb", "ccc"]

    j = jsonify(domains)

    #print(j)


abc()