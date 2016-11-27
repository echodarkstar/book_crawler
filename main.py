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
de=ast.literal_eval(list[2])
for i in list[:2]:
	d=ast.literal_eval(i)
	tree.insert("",0,text=d["title"], values=(d["author"],d["price"], d["btype"], d["website"]))


tree.pack()

tree2 = ttk.Treeview(root)
tree2["columns"]=("rating", "count")
tree2.column("rating", width=100 )
tree2.column("count", width=200 )
tree2.heading("rating", text="Rating")
tree2.heading("count", text="Rating Count")
tree2.insert("",0,text="Goodreads info", values=(de["rating"], de["count"]))
tree2.pack()
root.mainloop()
