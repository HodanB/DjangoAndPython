from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Are we going vegan? No pork for my fork!",
    "febuary": "Skinny season! Juice cleanse",
    "march": "KETO, KETO, K-E-T-O LET'S GO!",
    "april": "Are we going vegan? No pork for my fork!",
    "may": "Skinny season! Juice cleanse",
    "june":"KETO, KETO, K-E-T-O LET'S GO!",
    "july": "Are we going vegan? No pork for my fork!",
    "august": "Skinny season! Juice cleanse",
    "september": "KETO, KETO, K-E-T-O LET'S GO!",
    "october": "Are we going vegan? No pork for my fork!",
    "november": "Skinny season! Juice cleanse",
    "december": None,
}
# using reverse() helps avoid hardocing URLs = 
#   if you ever change the pattern, you only need to update it in urls.py and not everywhere else


def home(request):
    list_months = []
    months = list(monthly_challenges.keys())

    for  month in months:
        month_path = reverse("monthly-challenge",  args=[month] )
        list_months.append({"name": month, "url":month_path})
    
    
    return render(request, "challenges/homepage.html", {
        "list_months": list_months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This number is not supported")
    else:
        order_month = months[month - 1]
        redirect_path = reverse("monthly-challenge", args=[order_month])
        return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {
                      "text": challenge_text,
                      "month": month
                      })
    except:
        raise Http404()
        #to use my 404.html template:
        #response_data = render_to_string("404.html")    
        #return HttpResponseNotFound(response_data)
    
