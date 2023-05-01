from bottle import static_file, route, run
@route('/<filename:path>')
def index(filename):
    return static_file(filename, root='')
@route('/')
def index():
    return static_file('index.html',root='')

@route('/sigma')
def sigma():
    return static_file('sigma.html',root='')

run(host='localhost',port=5150,debug=True,reloader=True)