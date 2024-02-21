from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageCreateForm

# Create your views here.
from .models import Image


@login_required
def image_create(request):
    if request.method == "POST":
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image added successfully")

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request, "images/image/create.html", {"section": "images", "form": form})

def detail(request, img):
    image = get_object_or_404(Image, slug=img)
    return render(request,
                  "images/image/detail.html",
                  {"image": image})
