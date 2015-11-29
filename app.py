import google, urllib2, bs4, re

def query(s):
    """
    TL;DR: Searches input on google.

    Arguments:
    s (string) - A query string; what you are searching for.
       -Ex. "who played spiderman"

    Returns:
    A string of names from the html of the top 5 google search results from the query.

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

print query("Who is Morgan Freeman")



