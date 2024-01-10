from django.shortcuts import render
from django.http import JsonResponse
import urllib

# Create your views here.
def homepage(request):
    return render(request,"homepage.html",{})

def getTimeStories(request):
    time_url = "https://time.com"
    with urllib.request.urlopen(time_url) as response:
        data = response.read().decode('utf-8')
        startIndex = data.find("latest")
        data = data[startIndex:]
        data = data[:data.find("</ul>")]
        startIndex = data.find("<ul>")
        data = data[startIndex:]
        headings = data.split('<h3 class="latest-stories__item-headline">')
        links = data.split("href")
        result = []
        for i in range(1,7):
            result.append({"title":headings[i][:headings[i].find("</h3>")].replace("’","'").replace("‘","'"),"link":"https://time.com"+links[i][2:links[i].find('">')]})
    return JsonResponse(result,safe=False)
