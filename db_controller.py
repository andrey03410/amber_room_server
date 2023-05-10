import pyodbc
import settings
from datetime import datetime


class DbController:
    def __init__(self):
        self.__connection_to_db = pyodbc.connect(settings.DATABASE_CONNECTION)
        self.__cursor = self.__connection_to_db.cursor()
        self.__nationality = self.init_nationality()
        self.__organisation = self.init_organisation()
        self.__type_research = self.init_type_research()
        self.__persons = self.init_persons()
        self.__places = self.init_places()
        self.__versions = self.init_versions()
        self.__search_attempts = self.init_search_attempts()
        self.__finds = self.init_finds()
        self.__type_doc = self.init_type_doc()
        self.__document = self.init_document()
        self.__indication = self.init_indication()
        self.__research = self.init_research()
        self.__document_person = self.init_document_person()
        self.__document_author = self.init_document_author()
        self.__document_indications = self.init_document_indications()
        self.__images = self.init_images()

    def init_persons(self):
        self.__cursor.execute('SELECT id_персона, ФИО, id_гражданство, описание FROM персона')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        persons = map(lambda x: {'id': int(x.id_персона), 'name': x.ФИО,
                                 'id_nationality': int(x.id_гражданство),
                                 'description': x.описание}, row)
        return list(persons)

    def init_document_indications(self):
        self.__cursor.execute('SELECT id_документ, id_показание FROM документ_показание')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        persons = map(lambda x: {'id_document': int(x.id_документ),
                                 'id_indications': int(x.id_показание)}, row)
        return list(persons)

    def init_document_author(self):
        self.__cursor.execute('SELECT id_документ, id_автор FROM документ_автор')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        document_author = map(lambda x: {'id_document': int(x.id_документ),
                                 'id_author': int(x.id_автор)}, row)
        return list(document_author)

    def get_persons(self):
        return self.__persons

    def init_places(self):
        self.__cursor.execute('SELECT id_места, место, описание, координата_х, координата_у FROM место')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        places = map(lambda x: {'id': int(x.id_места), 'name': x.место, 'description': x.описание, 'coord_x': x.координата_х, 'coord_y': x.координата_у}, row)
        return list(places)

    def init_nationality(self):

        self.__cursor.execute('SELECT id_гражданство, гражданство FROM гражданство')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        nationality = map(lambda x: {'id': int(x.id_гражданство), 'nationality': x.гражданство}, row)
        return list(nationality)

    def get_nationality(self):
        return self.__nationality

    def get_places(self):
        return self.__places

    def init_versions(self):
        self.__cursor.execute('SELECT id_версии, id_место, описание FROM версия')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        versions = map(lambda x: {'id': int(x.id_версии), 'id_places': int(x.id_место), 'description': x.описание}, row)
        return list(versions)

    def get_versions(self):
        return self.__versions

    def init_search_attempts(self):

        self.__cursor.execute(
            'SELECT id_попытка_поиска, id_версия, описание, дата_начала, дата_окончания FROM попытка_поиска')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        search_att = map(
            lambda x: {'id': int(x.id_попытка_поиска), 'id_versions': int(x.id_версия), 'description': x.описание, 'date_start': x.дата_начала,
                       'date_finish': x.дата_окончания}, row)
        return list(search_att)

    def get_search_attempts(self):
        return self.__search_attempts

    def init_finds(self):

        self.__cursor.execute('SELECT id_находки, находка, id_попытка_поиска, описание FROM находки')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        find = map(lambda x: {'id': int(x.id_находки), 'name': x.находка,
                              'id_search_attempts': int(x.id_попытка_поиска), 'description': x.описание}, row)
        return list(find)

    def get_finds(self):
        return self.__finds

    def init_document(self):

        self.__cursor.execute('SELECT id_документ, id_тип_документа, id_попытка_поиска, дата, описание FROM документ')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        document = map(lambda x: {'id': int(x.id_документ), 'id_type_doc': int(x.id_тип_документа),
                                  'id_search_attempts': x.id_попытка_поиска,
                                  'date': x.дата, 'description': x.описание}, row)
        return list(document)

    def get_document(self):
        return self.__document

    def init_indication(self):

        self.__cursor.execute('SELECT id_показание, id_персона, показание, id_версия, дата FROM показание')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        indication = map(
            lambda x: {'id': int(x.id_показание), 'id_persons': int(x.id_персона), 'testimony': x.показание,
                       'id_versions': int(x.id_версия), 'date': x.дата}, row)
        return list(indication)

    def get_indication(self):
        return self.__indication

    def init_research(self):

        self.__cursor.execute(
            'SELECT id_исследование, id_организация, id_попытка_поиска, описание, id_тип_исследования, локальное_место, техника FROM исследование')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        research = map(lambda x: {'id': int(x.id_исследование), 'id_organization': x.id_организация,
                                  'id_search_attempts': x.id_попытка_поиска,
                                  'description': x.описание, 'id_type_research': int(x.id_тип_исследования),
                                  'local_place': x.локальное_место, 'technique': x.техника}, row)
        return list(research)

    def get_research(self):
        return self.__research

    def init_type_doc(self):

        self.__cursor.execute(
            'SELECT id_тип_документа, тип FROM тип_документа')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        type_doc = map(lambda x: {'id': int(x.id_тип_документа), 'type': x.тип}, row)
        return list(type_doc)

    def get_type_doc(self):
        return self.__type_doc

    def init_organisation(self):

        self.__cursor.execute(
            'SELECT id_организация, организация FROM организация')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        organisation = map(lambda x: {'id': int(x.id_организация), 'organisation': x.организация}, row)
        return list(organisation)

    def get_organisation(self):
        return self.__organisation

    def init_type_research(self):

        self.__cursor.execute(
            'SELECT id_тип_исследования, тип FROM тип_исследования')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        type_research = map(lambda x: {'id': int(x.id_тип_исследования), 'type': x.тип}, row)
        return list(type_research)

    def get_type_research(self):
        return self.__type_research

    def init_document_person(self):
        self.__cursor.execute(
            'SELECT id_документ, id_персона FROM документ_персона')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        document_person = map(lambda x: {'id_document': int(x.id_документ), 'id_person': int(x.id_персона)}, row)
        return list(document_person)

    def get_document_person(self):
        return self.__document_person

    def init_images(self):
        self.__cursor.execute(
            'SELECT id_фото, описание, id_документ, путь FROM фото')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        photo = map(lambda x: {'id': int(x.id_фото), 'description': x.описание, 'id_document': int(x.id_документ),
                               'path': x.путь}, row)
        return list(photo)

    def get_images(self):
        return self.__images

    def get_free_id(self, a):
        id_max = -1

        for i in a:
            if i['id'] > id_max:
                id_max = i['id']

        id_max += 1
        id = id_max
        indexx = [-1] * id_max

        for i in a:
            indexx[i['id']] = i['id']

        for i in range(1, id_max):
            if indexx[i] == -1:
                id = i
                break
        return id

    def add_person(self, name: str, nationality: int, description: str):

        self.__cursor.execute("INSERT INTO персона (id_персона, ФИО, id_гражданство, описание) "
                              "VALUES (?, ?, ?, ?)", self.get_free_id(self.__persons), name, nationality, description)
        self.__connection_to_db.commit()
        self.__persons = self.init_persons()

    def add_place(self, name: str, description: str):

        self.__cursor.execute("INSERT INTO место (id_места, место, описание, координата_х, координата_у) "
                              "VALUES (?, ?, ?, ?, ?)", self.get_free_id(self.__places), name, description, 0, 0)
        self.__connection_to_db.commit()
        self.__places = self.init_places()

    def add_version(self, id_places: int, description: str):

        self.__cursor.execute("INSERT INTO версия (id_версии, id_место, описание) "
                              "VALUES (?, ?, ?)", self.get_free_id(self.__versions), id_places, description)
        self.__connection_to_db.commit()
        self.__versions = self.init_versions()

    def add_search_attempts(self, id_versions: int, date_start: str, date_finish: str, description: str):

        self.__cursor.execute(
            "INSERT INTO попытка_поиска (id_попытка_поиска, id_версия, описание, дата_начала, дата_окончания) "
            "VALUES (?, ?, ?, ?, ?)", self.get_free_id(self.__search_attempts), id_versions,
            description, date_start, date_finish)
        self.__connection_to_db.commit()
        self.__search_attempts = self.init_search_attempts()

    def add_finds(self, name: str, id_search_attempts: int, description: str):

        self.__cursor.execute("INSERT INTO находки (id_находки, находка, id_попытка_поиска, описание) "
                              "VALUES (?, ?, ?, ?)", self.get_free_id(self.__finds), name, id_search_attempts,
                              description)
        self.__connection_to_db.commit()
        self.__finds = self.init_finds()

    def add_researches(self, id_organization: int, id_search_attempts: int, description: str, id_type_research: int,
                       local_place: str, technique: str):

        self.__cursor.execute(
            "INSERT INTO исследование (id_исследование, id_организация, id_попытка_поиска, описание, id_тип_исследования, локальное_место, техника) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)", self.get_free_id(self.__research), id_organization, id_search_attempts,
            description, id_type_research, local_place, technique)
        self.__connection_to_db.commit()
        self.__research = self.init_research()

    def add_indications(self, id_persons: int, testimony: str, id_versions: int, date: str, id_documents: list):
        id_indications = self.get_free_id(self.__indication)
        self.__cursor.execute(
            "INSERT INTO показание (id_показание, id_персона, показание, id_версия, дата) "
            "VALUES (?, ?, ?, ?, ?)", id_indications, id_persons, testimony,
            id_versions, date)
        self.__connection_to_db.commit()
        self.__indication = self.init_indication()

        for i in range(len(id_documents)):
            self.__cursor.execute(
                "INSERT INTO документ_показание (id_документ, id_показание) "
                "VALUES (?, ?)", id_documents[i], id_indications)
            self.__connection_to_db.commit()
            self.__document_indications = self.init_document_indications()


    def add_document(self, id_type_doc: int, id_search_attempts: int, date: str, description: str, id_author: list,
                     id_person: list, imageDesc: list, images: list):
        id_documents = self.get_free_id(self.__document)
        self.__cursor.execute(
            "INSERT INTO документ (id_документ, id_тип_документа, id_попытка_поиска, дата, описание) "
            "VALUES (?, ?, ?, ?, ?)", id_documents, id_type_doc, id_search_attempts,
            date, description)
        self.__connection_to_db.commit()
        self.__document = self.init_document()

        for i in range(len(id_author)):
            self.__cursor.execute(
                "INSERT INTO документ_автор (id_документ, id_автор) "
                "VALUES (?, ?)", id_documents, id_author[i])
            self.__connection_to_db.commit()
            self.__document_author = self.init_document_author()

        for i in range(len(id_person)):
            self.__cursor.execute(
                "INSERT INTO документ_персона (id_документ, id_персона) "
                "VALUES (?, ?)", id_documents, id_person[i])
            self.__connection_to_db.commit()
            self.__document_person = self.init_document_person()






