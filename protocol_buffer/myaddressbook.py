#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yujinlun
# @Date:   2016-02-17 12:00:52
# @Last Modified by:   smithallen
# @Last Modified time: 2016-02-17 15:15:40

import addressbook_pb2

# Iterates though all people in the AddressBook and prints info about them.


def ListPeople(address_book):
    for person in address_book.person:
        print "Person ID:", person.id
        print "  Name:", person.name
        if person.HasField('email'):
            print "  E-mail address:", person.email

        for phone_number in person.phone:
            if phone_number.type == addressbook_pb2.Person.MOBILE:
                print "  Mobile phone #: ",
            elif phone_number.type == addressbook_pb2.Person.HOME:
                print "  Home phone #: ",
            elif phone_number.type == addressbook_pb2.Person.WORK:
                print "  Work phone #: ",
            print phone_number.number


addressbook = addressbook_pb2.AddressBook()
person = addressbook.person.add()

person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phone.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

phone = person.phone.add()
phone.number = "555-4322"
phone.type = addressbook_pb2.Person.WORK

print addressbook

with open("test.addressbook", 'wb') as f:
    f.write(addressbook.SerializeToString())

new_addressbook = addressbook_pb2.AddressBook()
with open("test.addressbook", 'rb') as f:
    new_addressbook.ParseFromString(f.read())
    ListPeople(new_addressbook)
