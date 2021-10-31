from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)


# <img src="https://readme-typing-svg.herokuapp.com?font=Acme&color=%%23000000&size=30&lines=CSE+Student+At+SRM;A+Python+Developer;A+Front-End++Developer+;Singer%2C+Artist;Ai+Enthsiast">
