# -*- coding: utf-8 -*-

#!/usr/bin/python
import unittest,sqlalchemy, json
from domain.build import Build
from orm.database import db_session, engine, Base
from utils.json_utils import JsonUtil

class UserUt(unittest.TestCase):
    '''A Unit Test Demo'''

    def setUp(self):
        import domain
        Base.metadata.create_all(engine) 

        
#     def tearDown(self):
#         Base.metadata.drop_all(engine)
        
    def test_insert(self):
 
        t1 = Build('BDR-64423', '234567', '13.4', 'dev1')
        db_session.add(t1)
        db_session.commit()

    def test_version(self):
        self.assertEquals('0.8.1',sqlalchemy.__version__,\
                          'version number not match')
        
if __name__=='__main__': unittest.main()