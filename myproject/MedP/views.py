from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import requests
from django.shortcuts import render

# myapp/views.py

def search_images(query, api_key, cx, num=3):
    # Construct the API request URL with the 'searchType' parameter set to 'image'
    url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}&searchType=image&num={num}'

    # Make the API request
    response = requests.get(url)
    results=[]

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        image_results = response.json().get('items', [])
        
        if image_results:
            for i, result in enumerate(image_results, 1):
                  results.append(result['link'])
        return results
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return None




def search_view(request):
    result = None
    if 'query' in request.GET:
        # Process the search query and add some text to it
        query = request.GET.get('query', '')
        result = search_images(query, 'AIzaSyCbNpB216TpxCSmpP9ixjhjPGm_AKoK3fE', 'a1cb115d6c9a8475b', num=5)

    return render(request, 'search.html', {'result': result})
