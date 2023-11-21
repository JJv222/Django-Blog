from django.shortcuts import render
from .models import Post,Comment
from django import forms
from django.utils import timezone
# Create your views here.

class PostADDForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(max_length=500)

############################################################

def show_posts_all(request):
    post =Post.objects.all()
    context = {
        'posts':post,
    }
    return render(request,'Posts/index.html',context)

def add_new_post(request):
    form = PostADDForm()
    if request.method == 'POST':
        form = PostADDForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            author = request.user
            create_date = timezone.now()
            last_update_date = timezone.now()

            # Utwórz nowy post i zapisz go do bazy danych
            Post.objects.create(
                title=title,
                body=body,
                author=author,
                create_date=create_date,
                last_update_date=last_update_date
            )

            # Przekieruj użytkownika na stronę z postami po dodaniu nowego postu
            return render(request, 'Posts/index.html', {'posts': Post.objects.all()})
    
    # Jeśli żądanie to GET, wyświetl formularz
    return render(request, 'Posts/add_post.html', {'form': form})