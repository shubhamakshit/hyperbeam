from flask import Flask, render_template, request, redirect
from datetime import datetime
import os

app = Flask(__name__)
data_file = os.path.join("static", "data.csv")


def read_csv():
    with open(data_file, "r") as file:
        read_data = []
        count = 0 

        for x in file.readlines():
            name = x.split(',')[0]
            link = x.split(',')[1]
            print(f'Name: {name}\nLink:{link}')
            read_data.append([str(name),str(link)])

        print(read_data)
        return read_data


def write_to_csv(new_data):
    fieldnames = ["Date", "URL"]
    print(new_data)
    with open(data_file,'w+') as file:
        for data in new_data:
            file.writelines(new_data[data]+",")
        file.writelines('\n')



@app.route("/")
def index():
    data = read_csv()
    return render_template("index.html", data=data)


@app.route("/add_data", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        new_data = {
            "Date": request.form.get("date"),
            "URL": request.form.get("url"),
        }

        write_to_csv(new_data)
        return redirect("/")

    return render_template("add_data.html")


@app.route('/delete-all')
def delete():
    with open(data_file,'w+') as file:
        file.writelines("")
    return redirect('/')

if __name__ == "__main__":
    app.run()
