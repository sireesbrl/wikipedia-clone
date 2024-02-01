from django.shortcuts import render
from markdown2 import Markdown
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def convert_to_html(title):
    contents = util.get_entry(title)
    markdowner = Markdown()
    if contents is not None:
        return markdowner.convert(contents)


def entry(request, title):
    contents = convert_to_html(title)
    if contents == None:
        return render(request, "encyclopedia/errors.html", {
            "message": "Entry not Found..."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": contents
        })


def search(request):
    if request.method == "POST":
        find_entry = request.POST['q']
        contents = convert_to_html(find_entry)
        if contents is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": find_entry,
                "content": contents
            })
        else:
            entries = util.list_entries()
            recommendations = []
            for entry in entries:
                if find_entry.lower() in entry.lower():
                    recommendations.append(entry)
            return render(request, "encyclopedia/search.html", {
                "query": find_entry,
                "recommendations": recommendations
            })


def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        contents = request.POST['content']
        exists = util.get_entry(title)
        if exists is not None:
            return render(request, "encyclopedia/errors.html", {
                "message": "Entry exists already!"
            })
        else:
            util.save_entry(title, contents)
            content = convert_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": content,
            })



def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content,
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        content = convert_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content,
        })
    

def get_random(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    contents = convert_to_html(entry)
    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "content": contents,
    })