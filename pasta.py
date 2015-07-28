# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for, redirect, Response
import hashlib
import cgi
app = Flask(__name__)
app.debug = True
@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        paste=request.form['paste'].encode('utf-8')
        filename=hashlib.md5(paste).hexdigest()
        paste_file = open('static/'+filename, 'w+')
        paste_file.write(paste)
	return redirect('/'+filename)
        #return render_template('add.htm', paste_id=filename)

@app.route("/", methods=['POST', 'GET'])
def hello(page_name=None):
	if request.method == 'POST':
        	paste=request.form['paste'].encode('utf-8')
	        filename=hashlib.md5(paste).hexdigest()
	        paste_file = open('static/'+filename, 'w+')
	        paste_file.write(paste)
	        return request.url_root+filename+'\n'
	else:
	    return render_template('main.htm', page_name=page_name)
@app.route("/<id>")
def show(id=None):
    try:
        paste_file=open('static/'+id, 'r')
    except:
        return render_template('main.htm')
        raise
#    paste=paste_file.read()
    paste=[]
    for line in paste_file:
        paste.append(line.decode('utf-8'))
    return render_template('show.htm', paste=paste, paste_id=id)
@app.route("/raw/<id>")
def show_raw(id=None):
    try:
        paste_file=open('static/'+id,'r')
    except:
        return render_template('page.htm')
	raise
    return Response(paste_file.read(), mimetype="text/plain")
if __name__ == "__main__":
    app.run(debug=True)
