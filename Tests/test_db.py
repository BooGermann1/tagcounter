from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tagcounter.misc import BadResultException, DB_LOCATION
import pickle
from Tagcounter.dao import DAO, TagDictionary
import pytest

url_set_EC0 = ("yandex.ru", {"html": 3, "p": 2, "head": 1})


def test_save():
    """Test checks whether persistent module saves data in DB correctly"""
    orm_entity = DAO()
    orm_entity.save(url_set_EC0[0], url_set_EC0[1])

    """Create own test connection to db"""
    Base = declarative_base()
    engine = create_engine('sqlite:///' + DB_LOCATION)
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    """Check if binary data in db matches pickled input data"""
    restored = session.query(TagDictionary).filter(TagDictionary.url == url_set_EC0[0]).one()
    assert pickle.dumps(url_set_EC0[1]) == restored.dictionary


def test_read():
    """Test checks whether persistent module restores written data properly"""
    orm_entity = DAO()
    orm_entity.save(url_set_EC0[0], url_set_EC0[1])
    assert url_set_EC0[1] == orm_entity.read(url_set_EC0[0])


def test_no_results():
    """Test checks whether persistent module raises an exception if no requested data was found"""
    orm_entity = DAO()

    """Create own test connection to db"""
    Base = declarative_base()
    engine = create_engine('sqlite:///' + DB_LOCATION)
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    """Clear db from stored records"""
    session.query(TagDictionary).delete()
    session.commit()

    with pytest.raises(BadResultException):
        orm_entity.read(url_set_EC0[0])
