from django.shortcuts import render
from review.models import Post, Comment


def background(request):
	post_list = Post.objects.all()
	hits_list = []
	for post in post_list:
		hits = post.hits
		hits_list.append(hits)
	
	hits_list.sort(reverse=True)
	most1hits = hits_list[0]
	most2hits = hits_list[1]
	post1 = Post.objects.get(hits = most1hits)
	post2 = Post.objects.get(hits = most2hits)
	return render(request, 'layout.html',{'post1':post1, 'post2':post2,})

def introduce(request):
	from django.shortcuts import render
	from review.models import Post, Comment