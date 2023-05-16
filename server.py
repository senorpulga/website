from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name) # ist bereits ein str

def write_to_file(data):
    with open("venv/database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {email}, {subject}, {message}")

def write_to_csv(data):
    with open("venv/database.csv", newline="", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "save to database failed."
    else:
        return "something went wrong."
    
    # next: Video 8