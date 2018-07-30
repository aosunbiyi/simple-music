
from django.http import HttpResponse
from .models import Artist,Album,Song
from django.shortcuts import render ,get_object_or_404



def index(request):
    all_artists= Artist.objects.all()
    html=""
    for artist in all_artists:
        url='/music/'+ str(artist.id)
        html+='<a href="'+url+'"> '+artist.name+'</a> <br/>'
    return HttpResponse(html)

def details(request, id):
    artist1=get_object_or_404(Artist, pk=id)
    albums=artist1.album_set.all()
    context={'artist1':artist1, 'albums':albums}        
  
    return render(request,'music/details.html',context)