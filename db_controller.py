import pyodbc


class DbController:
    def __init__(self):
        self.connection_to_db = pyodbc.connect(
            r'Driver={SQL Server};Server=DESKTOP-EBLKJFC;Database=янтарная комната;Trusted_Connection=yes;')
        self.cursor = self.connection_to_db.cursor()
        self.persons = self.init_persons()

    def init_persons(self):
        self.cursor.execute('SELECT id_персона, ФИО, id_гражданство, описание FROM персона')
        row = []
        while 1:
            item = self.cursor.fetchone()
            if not item:
                break
            row.append(item)
        persons = map(lambda x: {'id': int(x.id_персона), 'name': x.ФИО, 'id_nationality': int(x.id_гражданство),
                                 'description': x.описание}, row)
        return list(persons)

    def get_persons(self):
        return self.persons
