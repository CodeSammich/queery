import google, urllib2, bs4, re

def query(s):
    """
    TL;DR: Searches input on google.

    Arguments:
    s (string) - A query string; what you are searching for.
       -Ex. "who played spiderman"

    Returns:
    A list of URLs that google finds pertaining to the query.

    """
    results = google.search(s, num = 5, start = 0, stop = 5)

    r = []
    for pg in results:
        r.append(pg)
    url = urllib2.urlopen(r[0])
    page = url.read()
    soup = bs4.BeautifulSoup(page, "html.parser")
    raw = soup.get_text()
    text = re.sub("[ \t\n](\w|\d)+"," ",raw)
    return text

print query("Who is Morgan Freeman")




