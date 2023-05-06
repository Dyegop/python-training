"""
DJANGO VIEWS:
    -Every view recieves a request and returns a response.
    -A reponse is an object of HttpResponse from django http module.
    -For example:
        def january(request):
            return HttpResponse("Apply for LinkedIn job offers everyday!")
    -We can add parameters that must be passed in the url to return a view.
    -For example:
        def monthly_challenge(request, month: str):
            return HttpResponse(f"We are in {month}!")

    -Reverse function:
        -Given a url pattern, Django uses url() to pick the right view and generate a page (url--> view).
        -Sometimes, like when redirecting, you need to go in the reverse direction and give Django the name of a view,
        and Django generates the appropriate url (view name --> url).
        -To go from view name to url, we use reverse() function.
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string


monthly_challenges = {
    'january': 'Apply for LinkedIn job offers everyday!',
    'february': 'Walk for at least 20 minutes everyday!',
    'march': 'Study Django for at least 30 minutes everyday!',
    'april': 'Apply for LinkedIn job offers everyday!',
    'may': 'Walk for at least 20 minutes everyday!',
    'june': 'Study Django for at least 30 minutes everyday!',
    'july': 'Apply for LinkedIn job offers everyday!',
    'august': 'Walk for at least 20 minutes everyday!',
    'september': 'Study Django for at least 30 minutes everyday!',
    'october': 'Apply for LinkedIn job offers everyday!',
    'november': 'Walk for at least 20 minutes everyday!',
    'december': 'Study Django for at least 30 minutes everyday!'
}

# Create your views here
def index(request):
    months = list(monthly_challenges.keys())

    list_items = [f'<li><a href="{reverse("month-challenge", args=[month])}">{month.capitalize()}</a></li>'
                  for month in months]

    response_data = f'<ul>{"".join(list_items)}</ul>'
    return HttpResponse(response_data)  # Every endpoint must return an HttpResponse


def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges[month]

        # Option 1
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

        # Option 2 (shortcut)
        # We can add a dictionary arg, called context
        # Keys will act as variables in the html and output the value (challenge_text in this case)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")


def monthly_challenge_by_number(request, month: int):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])  # /challenge/month
                                                                       # We must add the same args required in the path
    # return HttpResponseRedirect(f'/challenges/{redirect_month}')  # Redirect url with harcoded url
    return HttpResponseRedirect(redirect_path)  # Redirect url using reverse()
