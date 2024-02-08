from django.shortcuts import render
import markdown2
from . import util

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