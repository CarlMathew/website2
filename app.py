from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="template")
contact = [
  {
    "Name": "Carlito",
    "Profession": "Web Designer",
    "Years of Experience": 20,
    "Contact Number": "+63123456789",
    "Email": "carlitopogi@gmail.com"
  },
  {
    "Name": "Natalie",
    "Profession": "Graphic Designer",
    "Years of Experience": 15,
    "Contact Number": "+63123456789",
    "Email": "natalie@gmail.com"
  },
  {
    "Name": "Arthur",
    "Profession": "Photograpger",
    "Years of Experience": 18,
    "Contact Number": "+63123456789",
    "Email": "arthur@gmail.com"
  },
  {
    "Name": "Sasha",
    "Profession": "Musician",
    "Years of Experience": 24,
    "Contact Number": "+63123456789",
    "Email": "sahsa@gmail.com"
  }
]

@app.route("/")
def hello_World():
  return render_template("index.html", contact = contact)

@app.route("/api/contact")
def contacts():
  return jsonify(contact)

if __name__ == "__main__":
  app.run(host = "0.0.0.0",debug=True)
