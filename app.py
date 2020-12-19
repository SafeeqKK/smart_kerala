from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("admin/admin_home.html")

@app.route('/adm_add_police_station')
def adm_add_police_station():
    return render_template("admin/Add_police_station.html")

@app.route('/adm_view_police_station')
def adm_view_police_station():
    return render_template("admin/View_police_station.html")

@app.route('/adm_edt_police_station')
def adm_edt_police_station():
    return render_template("admin/Edit_police_station.html")







if __name__ == '__main__':
    app.run()
