from django.shortcuts import render
#MAiqCZt7iGYZT6BCJb8mmw==hOTujPTQA0czLegf
#MAiqCZt7iGYZT6BCJb8mmw==07zqAtG2soKfCtg8
# Create your views here.
def home(request):
     import json
     import requests
     if request.method== 'POST':
          query=request.POST['query']
          api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
          api_request = requests.get (api_url + query, headers = {'X-Api-Key': 'MAiqCZt7iGYZT6BCJb8mmw==07zqAtG2soKfCtg8'})
          try:
            api = json.loads(api_request.content)
            print(api_request.content) 
          except Exception as e:
               api="oops! There was an error"
               print(e)
          return render(request, 'home.html',{'api':api})
     else:
         return render(request, 'home.html',{'query':'Enter a valid query'})
         
        
     


     
