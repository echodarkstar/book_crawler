import subprocess
from tkinter import *
import ast
from tkinter import ttk
f = open('books.jl', 'r+')
def deleteContent(f):
    f.seek(0)
    f.truncate()
deleteContent(f)
print("Check out the info on the book you need across different websites!")
a = input("Enter name of book\t")
amazon='scrapy crawl first -a category={} -o books.jl'.format(a.replace(" ", "+"))
booksadda = 'scrapy crawl adda -a category={} -o books.jl'.format(a.replace(" ", "+"))
goodreads = 'scrapy crawl good -a category={} -o books.jl'.format(a.replace(" ", "+"))
subprocess.call('/bin/bash -c "$GREPDB"', shell=True, env={'GREPDB': amazon})
subprocess.call('/bin/bash -c "$GREPDB"', shell=True, env={'GREPDB': booksadda})
subprocess.call('/bin/bash -c "$GREPDB"', shell=True, env={'GREPDB': goodreads})
root = Tk()
list = f.readlines()
tree = ttk.Treeview(root)
tree["columns"]=("author","price","type", "website","blurb")
tree.column("author", width=300 )
tree.column("price", width=100)
tree.column("type", width=200 )
tree.column("website", width=200 )
# tree.column("blurb", width=300 )
tree.heading("author", text="Author")
tree.heading("price", text="Price")
tree.heading("type", text="Binding")
tree.heading("website", text="Website")
# tree.heading("blurb", text="Goodreads blurb")

for i in list[:2]:
	d=ast.literal_eval(i)
	var = StringVar()
	label = Label( root, textvariable=var, relief=RAISED )
	tree.insert("",0,text=d["title"], values=(d["author"],d["price"], d["btype"], d["website"]))


tree.pack()
root.mainloop()
