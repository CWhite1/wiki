from django.shortcuts import render
import random 

from . import util


# main page that displays all current entries and page links #
def index(request):  
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),             
    })
    

# entry page which displays a current page and title #
def title(request, name):
    entries = util.list_entries()
    for entry in entries:
        if entry == name:
            return render(request, "encyclopedia/entry.html", {      
                "entry": util.get_entry(name),
                'title': entry
            })


# function searches for a page and renders with substring unless page does not exist #
def search(request):
    """Search function"""
    entries = util.list_entries()
    query = request.GET.get('q')
    matched_entry_list = [] 
    u_query = query.upper() 
    for entry in entries: 
        u_entry = entry.upper()
        if query == entry or u_query == u_entry:
            return render(request,"encyclopedia/entry.html", {
                "entry": util.get_entry(entry),
                "title": entry
                })
        elif query in entry or u_query in u_entry:
            matched_entry_list.append(entry)
            continue
        print(matched_entry_list)
    for m_entry in matched_entry_list:
        return render(request,"encyclopedia/index.html", {
            "entries": matched_entry_list,
            }) 
    else:
        return render(request,"encyclopedia/error_page.html", {
        "message" : "Sorry, This Page Does Not Exist",
        "create" : "Please Feel To Create One."
                    })



# function creates a new page unless page already exists #
def create(request):
    if request.method =="POST":
        title = request.POST['title']
        title = title.capitalize()
        content = request.POST['content']
        entries = util.list_entries()
        capTitle = title.upper()
        for entry in entries:
            capEntry = entry.upper()
            if title == entry or capEntry == capTitle:  
                return render(request,"encyclopedia/error_page.html", {
                    "message" : "Sorry, This Page Already Exists"
                })
        
        return render(request,"encyclopedia/entry.html", {
                "content" : util.save_entry(title, content),
                "entry": util.get_entry(title),
                "title": title          
            })
    else:
        return render(request,"encyclopedia/create.html", {     
    })


# function edits an existing page and puts current page info into text area #
def edit(request, name):
    if request.method == "POST":
        content = request.POST['content'] 
        return render(request,"encyclopedia/entry.html", { 
                "content" : util.save_entry(name, content),   
                "title": name,    
                "entry": util.get_entry(name),  
                  
                })
    else:
        return render(request,"encyclopedia/edit.html", { 
                "edit_title": name,    
                "edit_entry": util.get_entry(name),       
                })


# function that randomly selects a page with random.choice() function
def randoms(request):
    entries = util.list_entries()
    s_entries = random.choice(entries)
    print(s_entries)
    return render(request, "encyclopedia/entry.html", {
            "title": s_entries,    
            "entry": util.get_entry(s_entries), 
            
            })
            


#Notes       

    # from django import forms 
    #class NewTaskForm(forms.Form):
    #    content = forms.CharField(label="", widget= forms.Textarea(attrs={'placeholder':'Content'}))
        

    # in order to create default tables inside django database, must type python manage.py migrate
