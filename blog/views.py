from django.shortcuts import render

posts =[
  {
    'author': 'Marcel Szmania',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'January 23, 2019'
  },
  {
    'author': 'Marcel Szmania',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'January 24, 2019'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})