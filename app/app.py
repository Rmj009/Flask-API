# app = Flask(__name__)
# app.run(port=5000, debug=True)

import flask #from flask import Flask
# from flask import request  # , jsonify, escape
import sqlite3
# app = Flask(__name__)
app = flask.Flask(__name__)
app.config["DEBUG"] = True


# @app.route('/user/<name>')
# def user_page(name):
#   return 'User: %s' % escape(name)

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


#---------------------GET-----------------------
@app.route('/', methods=['GET'])
def home():
    return '''
<h1>{{ -- }}的个人主页</h1>
{% if bio %}
    <p>{{ bio }}</p>  {# 这里的缩进只是为了可读性，不是必须的 #}
{% else %}
    <p>自我介绍为空。</p>
{% endif %}  {# 大部分 Jinja 语句都需要声明关闭 #}
'''


# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     conn = sqlite3.connect('books.db')
#     conn.row_factory = dict_factory
#     cur = conn.cursor()
#     all_books = cur.execute('SELECT * FROM books;').fetchall()

#     return jsonify(all_books)


# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_filter():
#     query_parameters = request.args

#     id = query_parameters.get('id')
#     published = query_parameters.get('published')
#     author = query_parameters.get('author')

#     query = "SELECT * FROM books WHERE"
#     to_filter = []

#     if id:
#         query += ' id=? AND'
#         to_filter.append(id)
#     if published:
#         query += ' published=? AND'
#         to_filter.append(published)
#     if author:
#         query += ' author=? AND'
#         to_filter.append(author)
#     if not (id or published or author):
#         return page_not_found(404)

#     query = query[:-4] + ';'

#     conn = sqlite3.connect('books.db')
#     conn.row_factory = dict_factory
#     cur = conn.cursor()

#     results = cur.execute(query, to_filter).fetchall()

#     return jsonify(results)



# @app.route("/predict", methods=["POST"])
# def predict():
#   output_dict = {"success": False}  
#   if Flask.request.method == "POST":
#     data = Flask.request.json  # 讀取 json
#   return Flask.jsonify(output_dict), 200 # 回傳json, http status code

@app.route("/performance", methods=["GET"])
def performance():
  output_dict = {"success": False}
  if flask.request.method == "GET":
      return Flask.jsonify(output_dict), 200


#-------ERROR Handling----------
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



# app.run()
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)