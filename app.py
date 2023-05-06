from bottle import static_file, route, run, template, request, redirect
import sqlite3
import socket
import os
@route('/<filename:path>')
def index(filename):
    return static_file(filename, root='')
@route('/')
def index():
    return static_file('index.html',root='')

@route('/sigma')
def sigma():
    conn = sqlite3.connect('content.db')
    c = conn.cursor()
    c.execute("SELECT id, ip, name FROM computers")
    result = c.fetchall()
    c.close()
    output = template('sigma', rows=result)
    return output

@route('/sigma/new',method='GET')
def new():
    if request.GET.get('save','').strip():
        ip = request.GET.get('ip','').strip()
        name = request.GET.get('name','').strip()
        conn = sqlite3.connect('content.db')
        c = conn.cursor()
        c.execute("INSERT INTO computers (ip,name) VALUES (?,?)",(ip,name))
        conn.commit()
        c.close()
        return redirect('/sigma')
    else:
        return template("newpc")
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
#Content
#cars
@route('/cars')
def cars():
    conn = sqlite3.connect('content.db')
    c = conn.cursor()
    c.execute('SELECT id, make, model, acid, file FROM cars')
    result = c.fetchall()
    c.close()
    output = template('content', rows=result)
    return output

@route('/cars/new',method='GET')
def new():
    if request.GET.get('save','').strip():
        make = request.GET.get('make','').strip()
        model = request.GET.get('model','').strip()
        acid = request.GET.get('acid','').strip()

        upload = request.files.get('file')
        if not upload:
            return "No file selected."

        name, ext = os.path.splitext(upload.filename)
        filename = os.path.join(UPLOAD_DIR,f"{name}{ext}")
        upload.save()

        url = f"/content/{name}{ext}"
        conn = sqlite3.connect('content.db')
        c = conn.cursor()
        c.execute("INSERT INTO cars (make,model,acid,file) VALUES (?,?,?,?)",(make,model,acid,url))
        conn.commit()
        c.close()
        return redirect('/cars')
    else:
        return template("newcar")

host = socket.gethostname()
ip = socket.gethostbyname(host)    
print("--------------")   
print(host)
print(f"http://{ip}:5150")
print("--------------")


run(host='192.168.1.12',port=5150,debug=True,reloader=True)