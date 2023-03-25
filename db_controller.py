import pyodbc


class DbController:
    def __init__(self):
        self.__connection_to_db = pyodbc.connect(
            r'Driver={SQL Server};Server=DESKTOP-LCT9RP5;Database=янтарная комната;Trusted_Connection=yes;')
        self.__cursor = self.__connection_to_db.cursor()
        self.__persons = self.init_persons()
        self.__places = self.init_places()
        self.__versions = self.init_versions()
        self.__search_attempts = self.init_search_attempts()

    def init_persons(self):
        self.__cursor.execute('SELECT id_персона, ФИО, id_гражданство, описание FROM персона')
        row = []
        while 1:
            item = self.__cursor.fetchone()
            if not item:
                break
            row.append(item)
        persons = map(lambda x: {'id': int(x.id_персона), 'name': x.ФИО, 'id_nationality': int(x.id_гражданство),
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
        search_att = map(lambda x: {'id': int(x.id_попытка_поиска), 'id_versions': int(x.id_версия), 'date_start': x.дата_начала,
                                 'date_finish': x.дата_окончания}, row)
        return list(search_att)

    def get_search_attempts(self):
        return self.__search_attempts










    def add_person(self, name: str, nationality: int, description: str):
        self.__cursor.execute("INSERT INTO персона (id_персона, ФИО, id_гражданство, описание) "
                              "VALUES (?, ?, ?, ?)", len(self.__persons) + 1, name, nationality, description)
        self.__connection_to_db.commit()
        self.__persons = self.init_persons()
