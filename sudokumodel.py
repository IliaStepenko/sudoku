from main import db

class Sudoku(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        level_en = db.Column(db.String(20))
        level_ru = db.Column(db.String(20))
        table = db.Column(db.String(255))

        def get_table(self):
            temp = [ int(i) for i in self.table.split(",")]
            table_as_array = []
            for i in range(9):
                table_as_array.append(temp[9*i:(9*(i+1))])
            return table_as_array
