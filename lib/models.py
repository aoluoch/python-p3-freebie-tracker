from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref='company')
    devs = relationship('Dev', secondary='freebies', backref='companies')

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', backref='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'


class Freebie(Base):
    __tablename__ = 'freebies'
    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"