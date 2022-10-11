from multiprocessing.reduction import duplicate
import tkinter as ttk
from matplotlib.dviread import Box
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import  os
#print("Location is:",os.getcwd(),'\n\n\n')

cols=["user_id","movie_id","rating","ts"]
df=pd.read_csv("u.data",sep="\t",names=cols).drop('ts',axis=1)
item_cols=["movie_id","title"]+[str(i) for i in range(22)]
df1=pd.read_csv("u.item",encoding="ISO-8859-1",sep="|",names=item_cols)[["movie_id","title"]]
movie=pd.merge(df,df1,on="movie_id")
   
app=ttk.Tk()
app.title("Recommendation System")
app.geometry('400x400')
result=ttk.Variable(app)

frame=ttk.Frame(app)
frame.place(x=10,y=10)
box=ttk.Listbox(frame,height=10,width=50)
#box.place(x=10,y=10)
for title in movie["title"].unique():
    box.insert(ttk.END,title)
box.pack(side='left',fill='y')
#box.grid(row=0,column=0)

scroll=ttk.Scrollbar(frame,orient=ttk.VERTICAL)
scroll.config(command=box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right',fill='y')

def get_movie():
    movie_selected=box.get(box.curselection())
    print("movie:",movie_selected)

    m=movie.pivot_table(index="user_id",columns="title",values="rating")
    
    corrs=m.corrwith(m[movie_selected])
    corrs_df=pd.DataFrame(corrs,columns=["correlation"])
    corrs_df["rating"]=movie.groupby("title")["rating"].mean()
    corrs_df["count"]=movie['title'].value_counts()
    
    top_recom=list(corrs_df[corrs_df["count"]>50].sort_values(by="correlation",ascending=False).head(3).index)
    if movie_selected in top_recom:
        top_recom.remove(movie_selected)                        
    print("Recommendations:", top_recom)
    
    if top_recom:
        result.set(top_recom[0])
    else:
        result.set("Sorry no recommendations found")

ttk.Button(app,text="Find Recommendations",font=("Arial",10),command=get_movie).place(x=100,y=200)
ttk.Label(app,textvariable=result,font=('Arial',15)).place(x=100,y=300)
app.mainloop()
