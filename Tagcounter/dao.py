from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, BLOB, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from Tagcounter.misc import BadResultException, DB_LOCATION
import pickle

Base = declarative_base()


class TagDictionary(Base):
    """DAO class"""
    __tablename__ = 'tag_dictionary'
    url = Column(String(256), primary_key=True)
    dictionary = Column(BLOB)


class DAO:

    def __init__(self):
        """Establish a connection to the db"""
        self.engine = create_engine('sqlite:///' + DB_LOCATION)
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def save(self, url, dictionary):
        serialized = pickle.dumps(dictionary)

        try:
            """If record exists already, then update"""
            restored = self.session.query(TagDictionary).filter(TagDictionary.url == url).one()
            restored.dictionary = serialized
        except NoResultFound:
            """If no record with same url was saved, then create one"""
            record = TagDictionary(url=url, dictionary=serialized)
            self.session.add(record)
        self.session.commit()

    def read(self, url):
        try:
            restored = self.session.query(TagDictionary).filter(TagDictionary.url == url).one()
        except NoResultFound:
            raise BadResultException("No such record in DB")
        return pickle.loads(restored.dictionary)