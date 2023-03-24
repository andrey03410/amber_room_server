import pyodbc


class DbController:
    def __init__(self):
        self.__connection_to_db = pyodbc.connect(
            r'Driver={SQL Server};Server=DESKTOP-EBLKJFC;Database=янтарная комната;Trusted_Connection=yes;')
        self.__cursor = self.__connection_to_db.cursor()
        self.__persons = self.init_persons()

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

    def add_person(self, name: str, nationality: int, description: str):
        self.__cursor.execute("INSERT INTO персона (id_персона, ФИО, id_гражданство, описание) "
                              "VALUES (?, ?, ?, ?)", len(self.__persons) + 1, name, nationality, description)
        self.__connection_to_db.commit()
        self.__persons = self.init_persons()
