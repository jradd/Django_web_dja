""" Views for the base application """

from django.shortcuts import render, render_to_response

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from blog.models import Post, PostAdmin

def main(request):
    """Main Listing"""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)
    
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
	posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
	posts = paginator.page(paginator.num_pages)
	
    return render_to_response("base/list.html", dict(posts=posts, user=request.user))


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

