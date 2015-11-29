from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        #gets input from search box
        raw_search = request.form["search"]
        
        if(raw_search == ''):
            return render_template("home.html")
        else:
            # all_results = all possible results
            all_results = utils.query( raw_search )
            # r = best result
            r = utils.mostPopular( all_results )
            
            return render_template("home.html", result = r)
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port = 8000)



