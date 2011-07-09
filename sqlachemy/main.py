import urllib2
import simplejson

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Manufacturer(Base):
  """
  Manufacturer resource
  """
  __tablename__ = 'manufacturers'
  
  id = Column(Integer, primary_key=True)
  name = Column(String(32), unique=True)
  country = Column(String(32))

  def __init__(self, resource):
    """
    Class instantiation

    @param resource resource JSON attribute
    """
    self.name = resource['name']
    self.country = resource['country']
    
  def __repr__(self):
    return "<manufacturer('%s in %s')>" % (self.name, self.country)

class Car(Base):
  """
  Car resource
  """
  __tablename__ = 'cars'
        
  id = Column(Integer, primary_key=True)
  name = Column(String(32), unique=True)
  max_speed = Column(Integer)
  year_released = Column(Integer)
  manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))

  manufacturer = relationship(Manufacturer, backref=backref('cars', order_by=id))

  def __init__(self, resource):
    """
    Class instantiation

    @param resource resource JSON attribute
    """
    self.name = resource['name']
    self.max_speed = resource['max_speed']
    self.year_released = resource['year_released']
    
  def __repr__(self):
    return "<car('%s - max speed: %d, released in %s')>" % (self.name, self.max_speed, self.year_released)

class Resources:
  """
  Main class 
  """
  def __init__(self):
    """
    Class instantiation

    @param settings dict of settings
    """
    # database engine
    self.engine = None
    # Collection of tables and their associated schema constructs
    self.metadata = None
    # database session
    self.session = None

    self.setup_connection()
    self.setup_tables()
    self.process()

  def setup_connection(self):
    """
    Create DB session
    """
    s = 'mysql://root:xxxx@localhost:3306/vroom'
    self.engine = create_engine(s)
    Session = sessionmaker(bind=self.engine)
    self.session = Session()

  def setup_tables(self):
      """
      Create tables in database.
      """
      self.metadata = Base.metadata
      # create tables: ok to call multiple times
      self.metadata.create_all(self.engine)

  def process(self):
    """
    Add resources to DB
    """
    #data = simplejson.load(urllib2.urlopen("http://api_url/manufacturers"))
    data = {"manufacturers": [
            {"name": "Peugeot", "country": "France"},
            {"name": "Chevrolet", "country": "USA"},
           ]}
    data2 = {"cars": [
             {"name": "307", "max_speed": 180, "year_released": 2002},
             {"name": "Malibu", "max_speed": 190, "year_released": 2010},
            ]}
    for i, m in enumerate(data['manufacturers']):
      manufacturer = Manufacturer(m)
      # get cars for this manufacturers
      #data2 = simplejson.load(urllib2.urlopen("http://api_url/manufacturers/%s" % mamufacturer['name']))
      cars = []
      c = data2['cars'][i]
      # add car to manufacturer's cars list
      manufacturer.cars = [Car(c)]
      # add to DB
      self.session.add(manufacturer)
    # commit changes to DB
    self.session.commit()

    # queries
    for m in self.session.query(Manufacturer).order_by(Manufacturer.id):
      print m
      for c in m.cars:
        print '-- %s' % c

r = Resources()
