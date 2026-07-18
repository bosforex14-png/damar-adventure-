from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/daftar")
def daftar():
    return render_template("daftar.html")



@app.route("/submit", methods=["POST"])
def submit():

    nama = request.form["nama"]
    wa = request.form["wa"]
    alamat = request.form["alamat"]
    gunung = request.form["gunung"]
    tanggal = request.form["tanggal"]

    return render_template(
        "sukses.html",
        nama=nama,
        wa=wa,
        alamat=alamat,
        gunung=gunung,
        tanggal=tanggal
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
