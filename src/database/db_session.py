from peewee import *
db = PostgresqlDatabase('super_awesome_application', host='localhost', port=5432, user='mdmurtaza', password='1234')
db.connect()

