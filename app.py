import google, urllib2, bs4, re
from flask import Flask, render_template, request

app = Flask(__name__)

def query(s):
    """
    TL;DR: Searches input on google.

    Arguments:
    s (string) - A query string; what you are searching for.
       -Ex. "who played spiderman"

    Returns:
    A list of names (strings) from the html of the top 5 google search results from the query.

    """
    results = google.search(s, num = 5, start = 0, stop = 5)

    r = []
    for pg in results:
        r.append(pg)
    url = urllib2.urlopen(r[0])
    page = url.read()
    soup = bs4.BeautifulSoup(page, "html.parser")
    raw = soup.get_text()
    #raw2 = re.sub("[ \t\n](\w|\d)+"," ",raw)
    #print raw2
    text = re.findall("(\b?[A-Z][a-z]*('|-)?(\b|\s)){2,}",raw)
    names = []
    for dict in text:
        for i in dict:
            if i != unicode('') and i != unicode(' ') and i != unicode('\n'):
                names.append(i)    
    return names

def mostPopular(results):
    """
    TL;DR: Goes through list of names to find most frequent.

    Arguments:
    results (list) - the list of names passed from a query(s) call.
       -Ex. ["Andrew Garfield", "Tobey Maguire", ...]

    Returns:
    The most frequently occuring name (string) from the names list.
    """
     
    retString = ''
    
    tempMaxCount = 0
    
    for name in results:
        count = results.count(name)
        if count > tempMaxCount:
            tempMaxCount = count
            retString = name
    
    return retString

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
            all_results = query( raw_search )
            # r = best result
            r = mostPopular( all_results )
            
            return render_template("home.html", result = r)
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port = 8000)



