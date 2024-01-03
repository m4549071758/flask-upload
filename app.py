from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/upload", methods=["POST", "GET"])
def upload_file():
    if request.method == "POST":
        if request.files.getlist("file")[0].filename:
            upload_files = request.files.getlist("file")
            for upload_file in upload_files:
                #受信したファイルをtmp/に保存
                upload_file.save(os.path.join("./upload", upload_file.filename))
        else:
            return "No file part."
    return render_template("upload.html")

if __name__ == "__main__":
    app.run()