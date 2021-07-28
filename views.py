from django.shortcuts import render,get_object_or_404
from .models import  Category,Story
from django.db.models import Q

# Create your views here.
def story_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    story = Story.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)
    return render(request, 'story_list.html', {'categories':categories,
                                              'category':category,
                                              'story':story,
                                              })

def story_detail(request,slug):
    story=get_object_or_404(Story,slug=slug)
    return render(request,'story_detail.html',{'story':story})

def search(request):
    query=None
    results=[]
    if request.method=="GET":
        query=request.GET.get('search')
        results=Story.objects.filter(Q(title__icontains=query) | Q(answer1__icontains=query) | Q(answer2__icontains=query) | Q(answer3__icontains=query) | Q(answer4__icontains=query) | )
    return  render(request,'search.html',{'query': query,
                                          'results': results})
