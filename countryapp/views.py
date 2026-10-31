from django.shortcuts import render,redirect
from django.db import transaction
from .models import Capital,Countries
from .forms import CountryCapitalForm
def insertcountry(request):
    error = None
    if request.method == "POST":
        form = CountryCapitalForm(request.POST)

        if form.is_valid():
            countryname = form.cleaned_data['countryname'].strip()
            capitalname = form.cleaned_data['capitalname'].strip()

            if Countries.objects.filter(
                countryname__iexact=countryname
            ).exists():
                error = "This country already exists. Please enter another country."

            else:
                with transaction.atomic():
                    country = Countries.objects.create(
                        countryname=countryname
                    )

                    Capital.objects.create(
                        country=country,
                        capitalname=capitalname
                    )

                return redirect('countrylist')

    else:
        form = CountryCapitalForm()

    return render(
        request,
        'insertcountry.html',
        {'form': form, 'error': error}
    )

def countrylist(request):
    countries = Countries.objects.select_related('capital').all()
    return render(request,'countrylist.html',{'countries':countries})

# Create your views here.
