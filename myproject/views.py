from django.shortcuts import render, redirect
from news_en.forms import NewsFormEn


def news_create_main_en(request):
	if request.method == 'POST':
		form = NewsFormEn(data=request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_item = form.save(commit=False)
			new_item.author = request.user
			new_item.save()
			return redirect(new_item)
	else:
		form = NewsFormEn(data=request.GET)
	return render(request, 'main_en.html', {'form': form})


def terms(request):
	template = 'term/term.html'
	return render(request, template)


def terms_en(request):
	template = 'term_en/term.html'
	return render(request, template)


def about(request):
	template = 'about/about.html'
	return render(request, template)


def about_en(request):
	template = 'about/about_en.html'
	return render(request, template)




