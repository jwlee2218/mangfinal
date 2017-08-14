from django.shortcuts import render
from review.models import Post, Comment


def background(request):
	post_list = Post.objects.all()
	hits_list = []
	for post in post_list:
		hits = post.hits
		hits_list.append(hits)
	
	hits_list.sort(reverse=True)
	try:
		most1hits = hits_list[0]
		most2hits = hits_list[1]
		most3hits = hits_list[2]
		if most1hits==most2hits:
			date_list=[]
			for post in Post.objects.get(hits=most1hits):
				date=post.updated_at
				date_list.append(date)
			date_list.sort(reverse=True)
			datesort1=date_list[0]
			datesort2=date_list[1]
			post1=Post.objects.get(hits=most1hits, date=datesort1)
			post2=Post.objects.get(hits=most2hits, date=datesort2)

		elif most3hits==most2hits and most1hits!=most2hits:
			datelist=[]
			for post in Post.objects.get(hits=most2hits):
				date=post.updated_at
				date_list.append(date)
			date_list.sort(reverse=True)
			datesort1=date_list[0]
			datesort2=date_list[1]
			post1=Post.objects.get(hits=mosthits)
			post2=Post.objects.get(date=datesort1, hits=most2hits)

		else:
			post1 = Post.objects.get(hits = most1hits)
			post2 = Post.objects.get(hits = most2hits)
	except:
		pass
	return render(request, 'layout.html',{'post1':post1, 'post2':post2,})

def introduce(request):
	return render(request, 'introduce.html')