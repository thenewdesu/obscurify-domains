import socket
import urllib.parse
from tkinter import *
import  win32clipboard
root = Tk()
root.title('default')
def rooot(cb):
    d = '{0}'.format(cb)
    root.title(d)
tex = Text()
tex.pack(side=RIGHT)
def rev(id):
    s = u'{}\n'.format(id[::-1])
    tex.insert(END, s)
    tex.see(END)
    print('reverse:',s)
def usd(id):
    website = id
    def replace_usd(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
    reps ={'a' : '\u0250',
'b' : 'q',
'c' : '\u0254',
'd' : 'p',
'e' : '\u01DD',
'f' : '\u025F',
'g' : '\u0183',
'h' : '\u0265',
'i' : '\u0131',
'j' : '\u027E',
'k' : '\u029E',
'l': '\u0283',
'm' : '\u026F',
'n' : 'u',
'r' : '\u0279',
't' : '\u0287',
'v' : '\u028C',
'w' : '\u028D',
'y' : '\u028E',
'.' : '\u02D9',
'[' : ']',
'(' : ')',
'{' : '}',
'?' : '\u00BF',
'!' : '\u00A1',
"\'" : ',',
'<' : '>',
'_' : '\u203E',
';' : '\u061B',
'\u203F' : '\u2040',
'\u2045' : '\u2046',
'\u2234' : '\u2235',
'\r' : '\n' }
    txt = replace_usd(website.lower(), reps)
    print("Upside down:",txt)
    s = u'{}\n'.format(txt)
    tex.insert(END, txt)
    tex.see(END)             # Scroll if necessary
######################
def bubble(id):
    website = id
    def replace_bubble(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
    reps = {
"a":"\u24D0",
"b":"\u24D1",
"c":"\u24D2",
"d":"\u24D3",
"e":"\u24D4",
"f":"\u24D5",
"g":"\u24D6",
"h":"\u24D7",
"i":"\u24D8",
"j":"\u24D9",
"k":"\u24DA",
"l":"\u24DB",
"m":"\u24DC",
"n":"\u24DD",
"o":"\u24DE",
"p":"\u24DF",
"q":"\u24E0",
"r":"\u24E1",
"s":"\u24E2",
"t":"\u24E3",
"u":"\u24E4",
"v":"\u24E5",
"w":"\u24E6",
"x":"\u24E7",
"y":"\u24E8",
"z":"\u24E9",
"A":"\u24B6",
"B":"\u24B7",
"C":"\u24B8",
"D":"\u24B9",
"E":"\u24BA",
"F":"\u24BB",
"G":"\u24BC",
"H":"\u24BD",
"I":"\u24BE",
"J":"\u24BF",
"K":"\u24C0",
"L":"\u24C1",
"M":"\u24C2",
"N":"\u24C3",
"O":"\u24C4",
"P":"\u24C5",
"Q":"\u24C6",
"R":"\u24C7",
"S":"\u24C8",
"T":"\u24C9",
"U":"\u24CA",
"V":"\u24CB",
"W":"\u24CC",
"X":"\u24CD",
"Y":"\u24CE",
"Z":"\u24CF"
}
    txt = replace_bubble(website, reps)
    print("unicode:",txt)
############################################
    s = u'{} \n'.format(txt)
    tex.insert(END, txt)
    tex.see(END)             # Scroll if necessary
def black(id):
    website = id
    def replace_black(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
    reps = {
            'a':'\uD835\uDC1A',
            'b':'\uD835\uDC1B',
            'c':'\uD835\uDC1C',
            'd':'\uD835\uDC1D',
            'e':'\uD835\uDC1E',
            'f':'\uD835\uDC1F',
            'g':'\uD835\uDC20',
            'h':'\uD835\uDC21',
            'i':'\uD835\uDC22',
            'j':'\uD835\uDC23',
            'k':'\uD835\uDC24',
            'l':'\uD835\uDC25',
            'm':'\uD835\uDC26',
            'n':'\uD835\uDC27',
            'o':'\uD835\uDC28',
            'p':'\uD835\uDC29',
            'q':'\uD835\uDC2A',
            'r':'\uD835\uDC2B',
            's':'\uD835\uDC2C',
            't':'\uD835\uDC2D',
            'u':'\uD835\uDC2E',
            'v':'\uD835\uDC2F',
            'w':'\uD835\uDC30',
            'x':'\uD835\uDC31',
            'y':'\uD835\uDC32',
            'z':'\uD835\uDC33',
            'A':'\uD835\uDC00',
            'B':'\uD835\uDC01',
            'C':'\uD835\uDC02',
            'D':'\uD835\uDC03',
            'E':'\uD835\uDC04',
            'F':'\uD835\uDC05',
            'G':'\uD835\uDC06',
            'H':'\uD835\uDC07',
            'I':'\uD835\uDC08',
            'J':'\uD835\uDC09',
            'K':'\uD835\uDC0A',
            'L':'\uD835\uDC0B',
            'M':'\uD835\uDC0C',
            'N':'\uD835\uDC0D',
            'O':'\uD835\uDC0E',
            'P':'\uD835\uDC0F',
            'Q':'\uD835\uDC10',
            'R':'\uD835\uDC11',
            'S':'\uD835\uDC12',
            'T':'\uD835\uDC13',
            'U':'\uD835\uDC14',
            'V':'\uD835\uDC15',
            'W':'\uD835\uDC16',
            'X':'\uD835\uDC17',
            'Y':'\uD835\uDC18',
            'Z':'\uD835\uDC19'}
    txt = replace_black(website, reps)
    print("unicode:",txt)
############################################
    s = u'{} \n'.format(txt)
    tex.insert(END, txt)
    tex.see(END)             # Scroll if necessary
    #tex.delete('1.0', END)    try:
def s_neg(id):
    website = id
    def replace_S_neg(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
    reps = {
'a':'\uD83C\uDD70',
'b':'\uD83C\uDD71',
'c':'\uD83C\uDD72',
'd':'\uD83C\uDD73',
'e':'\uD83C\uDD74',
'f':'\uD83C\uDD75',
'g':'\uD83C\uDD76',
'h':'\uD83C\uDD77',
'i':'\uD83C\uDD78',
'j':'\uD83C\uDD79',
'k':'\uD83C\uDD7A',
'l':'\uD83C\uDD7B',
'm':'\uD83C\uDD7C',
'n':'\uD83C\uDD7D',
'o':'\uD83C\uDD7E',
'p':'\uD83C\uDD7F',
'q':'\uD83C\uDD80',
'r':'\uD83C\uDD81',
's':'\uD83C\uDD82',
't':'\uD83C\uDD83',
'u':'\uD83C\uDD84',
'v':'\uD83C\uDD85',
'w':'\uD83C\uDD86',
'x':'\uD83C\uDD87',
'y':'\uD83C\uDD88',
'z':'\uD83C\uDD89'}
    txt = replace_S_neg(website.lower(), reps)
    print("unicode:",txt)
############################################
    s = u'{} \n'.format(txt)
    tex.insert(END, txt)
    tex.see(END)             # Scroll if necessary
def wat():
    tex.delete('1.0', END)
la = p_ent = Entry(root)
la.pack()
z = Button(root, text="black",fg= 'blue',  command= lambda: black(Entry.get(p_ent))).pack(fill=X)
z = Button(root, text="square (neg)",fg= 'blue',  command= lambda: s_neg(Entry.get(p_ent))).pack(fill=X)
z = Button(root, text="bubble",fg= 'blue',  command= lambda: bubble(Entry.get(p_ent))).pack(fill=X)
z = Button(root, text="reverse",fg= 'blue',  command= lambda: rev(Entry.get(p_ent))).pack(fill=X)
z = Button(root, text="upside down",fg= 'blue',  command= lambda: usd(Entry.get(p_ent))).pack(fill=X)
z = Button(root, text="clear",fg= 'blue',  command= wat).pack(fill=X)
z = Button(root, text="Title?",fg= 'blue',  command= lambda: rooot(Entry.get(p_ent))).pack(fill=X)

root.mainloop()
