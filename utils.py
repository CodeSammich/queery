import google, urllib2, bs4, re

def whoquery(s):
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

    names = []
    for n in range (0,9):
        url = urllib2.urlopen(r[n])
        page = url.read()
        soup = bs4.BeautifulSoup(page, "html.parser")
        raw = soup.get_text()
        text = re.findall("(\b?[A-Z][a-z]*('|-)?(\b|\s))(\b?[A-Z][a-z]*('|-)?(\b|\s))",raw)
        for dict in text:
            for i in dict:
                if i != unicode('') and i != unicode(' ') and i != unicode('\n'):
                    names.append(i)
    ans = []
    i=0
    while (i < len(names)-1):
        ans.append(names[i].rstrip()+" " + names[i+1].rstrip())
        i+=2
    return ans

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

