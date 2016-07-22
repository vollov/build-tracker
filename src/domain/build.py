# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Sequence, DateTime
from datetime import datetime
from orm.database import Base
import time

class Build(Base):
    __tablename__ = 'builds'
    
    id = Column(Integer,Sequence('build_id_seq'), primary_key=True)
    build_request_id = Column(String(20))
    svn_revision = Column(String(20))
    branch = Column(String(10))
    env_name = Column(String(5))
    build_date = Column(DateTime())
    
    def __init__(self, build_request_id, svn_revision, branch, env_name, build_date=datetime.now(), oid = None):
        self.build_request_id = build_request_id
        self.svn_revision = svn_revision
        self.branch = branch
        self.env_name = env_name
        self.build_date = build_date
        self.id = oid
        
    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.build_request_id, self.env_name, self.build_date)
    
    def dict(self):
        #time object to string
        #self.build_date.strftime("%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(self.build_date.timetuple())

        return {'id':self.id, 'build_request_id':self.build_request_id,\
                 'svn_revision': self.svn_revision, \
                'branch':self.branch, 'env_name':self.env_name, \
                'build_date': timestamp * 1000}
        
    @staticmethod
    def decode(data):
        #string to date time object
        #build_time = time.strptime(data['build_date'], "%Y-%m-%d %H:%M:%S")
        time_in_seconds = int(data['build_date']/1000)
        build_time = datetime.fromtimestamp(time_in_seconds)
        if 'id' in data.keys():
            return Build(data['build_request_id'],data['svn_revision'], data['branch'], data['env_name'],build_time, data['id'])
        else:
            return Build(data['build_request_id'],data['svn_revision'], data['branch'], data['env_name'],build_time)