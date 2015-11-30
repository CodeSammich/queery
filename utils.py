import google, urllib2, bs4, re, csv

def whoQuery(s):
    """
    TL;DR: Searches input on google for "who" questions.

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

    f = open("first_names.csv")
    csvf = csv.reader(f)
    l = open("last_names.csv")
    csvl = csv.reader(l)
    ans = []
    i=0
    while (i < len(names)-1):
        firstValid = False
        lastValid = False
        first= names[i].rstrip()
        last = names[i+1].rstrip()
        for row in csvf:
            if first == row[0]:
                firstValid = True
        for row in csvl:
            if last == row[0]:
                lastValid = True
        
        if firstValid and lastValid:
            ans.append(first+" "+last)
        i+=2
        
    return ans

def whenQuery(s):
    """
    TL;DR: Searches input on google for "when" questions.

    Arguments:
    s (string) - A query string; what you are searching for.
       -Ex. "when did World War I start"

    Returns:
    A list of names (strings) from the html of the top 5 google search results from the query.
    """
    results = google.search(s, num = 5, start = 0, stop = 5)

    r = []
    for pg in results:
        r.append(pg)

    dates = []
    for n in range (0,9):
        url = urllib2.urlopen(r[n])
        page = url.read()
        soup = bs4.BeautifulSoup(page, "html.parser")
        raw = soup.get_text()
        text = re.findall("\d{2}(-|\/)?\d{2}(-|\/)?\d+", raw)
        for dict in text:
            for i in dict:
                if i != unicode('') and i != unicode(' ') and i != unicode('\n'):
                    dates.append(i)
    return dates

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

a = whoQuery("who played Spiderman")
print a
print mostPopular(a)
#b = whenQuery("when did World War I start")
#print b
#print mostPopular(b)
