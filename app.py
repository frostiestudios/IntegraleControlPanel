from bottle import static_file, route, run, template, request, redirect
import sqlite3
@route('/<filename:path>')
def index(filename):
    return static_file(filename, root='')
@route('/')
def index():
    return static_file('index.html',root='')

@route('/sigma')
def sigma():
    return static_file('sigma.html',root='')

@route('/servers')
def servers():
    conn = sqlite3.connect('content.db')
    c = conn.cursor()
    c.execute("SELECT id, rid, class, car, track FROM servers")
    result = c.fetchall()
    c.close()
    output = template('servers', rows=result)
    return output
@route('/servers/new',method='GET')
def new():
    if request.GET.get('save','').strip():
        raceclass = request.GET.get('class','').strip()
        car = request.GET.get('car','').strip()
        track = request.GET.get('track','').strip()
        conn = sqlite3.connect('content.db')
        c = conn.cursor()
        c.execute("INSERT INTO servers (class,car,track) VALUES (?,?,?)",(raceclass,car,track))
        conn.commit()
        c.close()
        return redirect('/servers')
    else:
        return template("new")
run(host='localhost',port=5150,debug=True,reloader=True)