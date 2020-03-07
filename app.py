import os
from flask import Flask, flash, redirect, url_for, render_template, request, send_from_directory
app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "./uploads"
@app.route('/')
def hello():
    return render_template("/index.html")
    
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if request.files:
            file = request.files["file"]
            if file.filename == "":
                return render_template("upload.html")
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
            return render_template("successupload.html")
    else:
        return render_template("/upload.html")
        
@app.route("/list", methods=['GET','POST'])
def list():
    uploadedFiles =[]
    for files in os.listdir("./uploads/"):
        if files != ".DS_Store" and files != ".iAmHiding":
            uploadedFiles.append(files)
    return render_template("/list.html", content = uploadedFiles)

@app.route("/download/")
def download():
    uploadedFiles = [f for f in os.listdir("./uploads/")]
    return render_template("/download.html", content=uploadedFiles)

@app.route("/download/<path:filename>", methods= ['GET', 'POST'])
def downloadThis(filename):
    return send_from_directory(directory = './uploads/', filename = filename, as_attachment=True)

@app.route("/aboutUs")
def aboutUs():
    return render_template("/aboutUs.html")

@app.route("/contactUs")
def contactUs():
    return render_template("/contactUs.html")
        
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5001, debug = True)
