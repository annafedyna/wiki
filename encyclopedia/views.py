from django.shortcuts import render
import markdown2
from . import util
from django import forms

def convert_md_to_html(filename):
    content = util.get_entry(filename)
    if not content:
        return None
    else:
        markdowner = markdown2.Markdown()
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if convert_md_to_html(title) == None:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
            })
    else:
        return render(request, "encyclopedia/entry.html", {
            'title': title,
            'content' : convert_md_to_html(title)
        })
        
def search(request):
    if request.method == 'POST':
        search_text = request.POST['q']
        if search_text in [entry.lower() for entry in util.list_entries()]:
            return render(request, "encyclopedia/entry.html", {
                'title': search_text,
                'content' : convert_md_to_html(search_text)
            })
        elif search_text:
            match_query = []
            for entry in util.list_entries():
                if search_text.lower() in entry.lower():
                    match_query.append(entry)
            return render(request, "encyclopedia/search.html", {
                'match_list' : match_query
            })
          

class NewPage(forms.Form):
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 15}))
    
def create_page(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/create_page.html", {
            'form': NewPage()
        })
    else:
        title = request.POST['title']
        content = request.POST['content']
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html")
        else:
            util.save_entry(title,content)
            return render(request, "encyclopedia/entry.html", {
                'title': title,
                'content' : convert_md_to_html(title)
            })