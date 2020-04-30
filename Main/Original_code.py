from tkinter import *
from tkinter.filedialog import *
class ScrolledText(Frame):
    """Widget composite, associant un widget Text et une barre de défilement"""
    def __init__(self, boss, baseFont ="Times", width =100, height =50):
        Frame.__init__(self, boss, bd=2, relief =SUNKEN)
        self.text =Text(self, font =baseFont, bg ='ivory', bd =1,
                        width =width, height =height)
        scroll =Scrollbar(self, bd =1, command =self.text.yview)
        self.text.configure(yscrollcommand =scroll.set)
        self.text.pack(side =LEFT, expand =YES, fill =BOTH, padx =2, pady =5)
        scroll.pack(side =RIGHT, expand =NO, fill =Y, padx =2, pady =5)

    def importFichier(self, fichier, encodage ="Utf8"):
        "insertion d'un texte dans le widget, à partir d'un fichier"
        of =open(fichier, "r", encoding =encodage)
        lignes =of.readlines()
        of.close()
        for li in lignes:
            self.text.insert(END, li)
def chercheCible(event=None):
    "défilement du texte jusqu'à la balise <cible>, grâce à la méthode see()"
    index = st.text.tag_nextrange('cible', '0.0', END)
    st.text.see(index[0])
def save():
    filename = askopenfilename(title="Save", filetypes=[("Text File", ".txt"), ('all files','.*')]) 
    t = st.text.get("1.0", "end-1c")
    of = open(filename, "w+", encoding='Utf-8')
    of.write(t + "\n")
    of.close()

def openas():
    filename = askopenfilename(title="Ouvrir votre document", filetypes=[("Text File", ".txt"), ('all files','.*')])
    st.text.delete("0.0", END)
    st.importFichier(filename, encodage='Utf-8')


t =Tk()
fname = Menubutton(t, text='Commandes')
fname.pack(pady ='4', padx ='10')
me = Menu(fname)
me.add_command(label='Ouvrir_sous', underline=0, command=openas)
me.add_command(label='Enregistrer', underline=0, command=save)
fname.configure(menu = me)
st =ScrolledText(t, baseFont="Helvetica 12 normal", width =40, height =10)
st.pack(expand =YES, fill =BOTH, padx =8, pady =8)

# Définition de balises, liaison d'un événement <clic du bouton droit> :
st.text.tag_configure("titre", foreground ="brown",
                      font ="Helvetica 11 bold italic")
st.text.tag_configure("lien", foreground ="blue",
                      font ="Helvetica 11 bold")
st.text.tag_configure("cible", foreground ="forest green",
                      font ="Times 11 bold")
st.text.tag_bind("lien", "<Button-3>", chercheCible)

titre ="""The Original Code of PyText
\n"""
auteur ="""
Diversity_YT ©opyrights alls rights reserved !"""

# Remplissage du widget Text (2 techniques) :
st.importFichier("About.txt", encodage ="Utf-8")
st.text.insert("0.0", titre, "titre")
st.text.insert(END, auteur, "cible")
# Insertion d'une image :
photo =PhotoImage(file= "PyText.png")
st.text.image_create("2.0", image =photo)
photo2 =PhotoImage(file="PyText1.png")
st.text.image_create("2.1", image=photo2)
# Ajout d'une balise supplémentaire :
st.text.tag_add("lien", "2.4", "2.23")
height=125
width=350


t.title("PyText Editing")
t.iconbitmap("logo.icns")
t.geometry("1300x1300")
t.configure(bg='black')

image = PhotoImage(file='PyText1.png').zoom(2).subsample(4)
image1 = PhotoImage(file='PyText.png').zoom(18).subsample(20)

can = Canvas(t, width=width, height=height, bg='white')
can.create_image(width/1.5, height/2, image=image)
can.create_image(width/5.5, height/2, image=image1)
can.pack(pady ='4', padx ='10')
t.mainloop()

