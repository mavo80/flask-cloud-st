from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Simulated file storage
files = []

@app.route("/")
def index():
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload():
    filename = request.form.get("filename")
    if filename and filename not in files:
        files.append(filename)
        flash("File uploaded successfully!", "success")
    else:
        flash("File already exists or invalid filename!", "error")
    return redirect(url_for("index"))

@app.route("/update", methods=["POST"])
def update():
    old_name = request.form.get("old_name")
    new_name = request.form.get("new_name")
    if old_name in files and new_name:
        index = files.index(old_name)
        files[index] = new_name
        flash("File updated successfully!", "success")
    else:
        flash("Invalid filename or update failed!", "error")
    return redirect(url_for("index"))

@app.route("/delete", methods=["POST"])
def delete():
    filename = request.form.get("filename")
    if filename in files:
        files.remove(filename)
        flash("File deleted successfully!", "success")
    else:
        flash("File not found or invalid filename!", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)