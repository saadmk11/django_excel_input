import xlrd

from django.db.models import Q
from django.shortcuts import render, redirect

from .models import UserInfo


def upload(request):
    if request.method == 'POST':
        data = request.FILES.get('data')
        if data:
            work_book = xlrd.open_workbook(str(data))
            sheet = work_book.sheet_by_index(0)

            for row in range(1, sheet.nrows):
                info = UserInfo()
                info.name = sheet.cell(row, 0).value
                info.country = sheet.cell(row, 1).value
                info.email = sheet.cell(row, 2).value
                info.save()
            return redirect("search")

    return render(request, 'xlimport/upload_form.html', {})


def search(request):
    queryset = UserInfo.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(country__icontains=query) |
            Q(email__icontains=query)
            ).distinct()

    context = {"queryset": queryset}

    return render(request, 'xlimport/search.html', context)
