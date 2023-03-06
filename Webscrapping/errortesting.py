from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://www.alphazoneeyeclinic.com/can-rheumatoid-arthritis-affect-the-eyes/")
except HTTPError as e:
    print(e)
except URLError as e:
    print("This server could not be found")
else:
    print("it worked")