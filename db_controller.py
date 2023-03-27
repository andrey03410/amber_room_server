import pyodbc


class DbController:
    def __init__(self):
        self.__connection_to_db = pyodbc.connect(
            r'Driver={SQL Server};Server=DESKTOP-LCT9RP5;Database=янтарная комната;Trusted_Connection=yes;')
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

    def init_persons(self):
        self.__cursor.execute('SELECT id_персона, ФИО, id_гражданство, описание FROM персона')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)

        #nationality = map(lambda x: {'id': int(x.id_персона)}, self.__nationality)
        persons = map(lambda x: {'id': int(x.id_персона), 'name': x.ФИО,
                                 'id_nationality': int(x.id_гражданство) ,
                                 'description': x.описание}, row)
        return list(persons)

    def get_persons(self):
        return self.__persons

    def init_places(self):
        self.__cursor.execute('SELECT id_места, место, описание FROM место')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        places = map(lambda x: {'id': int(x.id_места), 'name': x.место, 'description': x.описание}, row)
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

        self.__cursor.execute('SELECT id_попытка_поиска, id_версия, дата_начала, дата_окончания FROM попытка_поиска')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        search_att = map(
            lambda x: {'id': int(x.id_попытка_поиска), 'id_versions': int(x.id_версия), 'date_start': x.дата_начала,
                       'date_finish': x.дата_окончания}, row)
        return list(search_att)

    def get_search_attempts(self):
        return self.__search_attempts

    def init_finds(self):

        self.__cursor.execute('SELECT id_находки, находка, дата_создания, id_попытка_поиска, описание FROM находки')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        find = map(lambda x: {'id': int(x.id_находки), 'name': x.находка, 'date': x.дата_создания,
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
            'SELECT id_исследование, id_организация, id_попытка_поиска, описание, id_тип_исследования, локальное_место FROM исследование')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        research = map(lambda x: {'id': int(x.id_исследование), 'id_organization': x.id_организация,
                                  'id_search_attempts': x.id_попытка_поиска,
                                  'description': x.описание, 'id_type_research': int(x.id_тип_исследования),
                                  'local_place': x.локальное_место}, row)
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


    def add_person(self, name: str, nationality: int, description: str):
        self.__cursor.execute("INSERT INTO персона (id_персона, ФИО, id_гражданство, описание) "
                              "VALUES (?, ?, ?, ?)", len(self.__persons) + 1, name, nationality, description)
        self.__connection_to_db.commit()
        self.__persons = self.init_persons()
