from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from num2words import num2words
from numberstotextapp.utils.number_to_english import hello

# Create your views here.

@csrf_exempt
@require_http_methods(["GET","POST"])
def num_to_english(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            number = data.get('number', '')
        else:
            number = request.GET.get('number', '')

        num_in_english = num2words(number, lang='en')
        return JsonResponse({"status": "ok", "num_in_english": num_in_english})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
    