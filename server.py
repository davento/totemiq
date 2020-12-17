from flask import Flask,render_template, request, session, Response, redirect, url_for, send_file, send_from_directory, safe_join, abort

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_index():
    return render_template("index.html")

@app.route("/menu", methods=['GET'])
def home():
    return render_template("menu.html")

@app.route("/artists", methods=['GET'])
def info():
    return render_template("artists.html")

@app.route("/works", methods=['GET'])
def works():
    return render_template("works.html")

@app.route("/images/words/<id>")
def worksPreview(id):
    try:
	    return send_file('/works/assets/'+id+'.png', attachment_filename=id+'.png')
    except Exception as e:
	    return str(e)

@app.route("/works/<id>")
def worksId(id):
    return render_template("works/" + id + ".html")

@app.route("/assets/<id>")
def worksGlb(id):
    try:
	    return send_file('/assets/'+id, attachment_filename=id)
    except Exception as e:
	    return str(e)

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))

#if __name__ == "__main__":
#   app.run(debug=True)
