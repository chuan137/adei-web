# coding: utf8

adei = DAL('sqlite://storage.sqlite')

adei.define_table('servers',
        Field('key', unique=True),
        Field('host'),
        Field('server'),
        Field('database'))
