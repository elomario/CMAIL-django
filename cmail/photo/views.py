from django.shortcuts import render
from photo import Photo
def upload_photo(request):
    if request.method == 'POST':
        uploaded_photo = Photo(image = request.POST)
        if uploaded_photo.is_valid():
            # file is saved
            uploaded_photo.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})
# Create your views here.
