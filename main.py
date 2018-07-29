from flask import Flask,render_template,request, jsonify
from flask import jsonify,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from  sqlalchemy.sql.expression import func, select
app = Flask(__name__,static_folder="templates")

app.debug = True
app.config.from_object(Config)
db = SQLAlchemy(app)

from sudokumodel import Sudoku



@app.route('/getsudoku')
def get_sudoku():
    sudoku = Sudoku.query.order_by(func.random()).first()
    return jsonify(num = sudoku.id,en_level=sudoku.level_en,ru_level=sudoku.level_ru,table=sudoku.get_table())


@app.route('/getsudoku/level/<level>')
def get_sudoku_by_level(level):
    sudoku = Sudoku.query.filter_by(level_en = level).order_by(func.random()).first()
    if(sudoku is None):
        sudoku = Sudoku.query.order_by(func.random()).first()
    return jsonify(num = sudoku.id,en_level=sudoku.level_en,ru_level=sudoku.level_ru,table=sudoku.get_table())


@app.route('/getsudoku/number/<number>')
def get_sudoku_by_number(number):
    sudoku = Sudoku.query.filter_by(id = int(number)).order_by(func.random()).first()
    if(sudoku is None):
        sudoku = Sudoku.query.order_by(func.random()).first()
    return jsonify(num = sudoku.id,en_level=sudoku.level_en,ru_level=sudoku.level_ru,table=sudoku.get_table())




@app.route('/')
def main():
    return render_template('index.html')
