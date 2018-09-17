#Elvar Þór Sævarsson
#Verkefni 3
#10.9.2018

from bottle import *

@route("/")
def index():
    gogn = {
        'title': 'Modular template',
        'content': '<h3>Hallo Modular templates!</h3>',
        'footer': 'Höfundur &copy 2018 Elvar'
    }
    return template('base.tpl', gogn)


# template 1 dæmi - if else
@route("/page1")
def index():
    return template("index1.tpl")
# Template 2 dæmi - dæmi um lykkju - loop
@route("/page2")
def index():
    return template("index2.tpl")
# Template 3 dæmi - dæmi senda gildi í template
@route("/page3")
def index():
    return template("index3.tpl", nafn="Guðmundur")
# Template 4 dæmi -
@route("/page4")
def index():
    my_dict = {'number':'123','street': 'Fake str', 'city': 'Fakeville'}
    return template("index1.tp1",my_dict)
@route("/page5")
def index():
    info = {'title': 'Beatles',
            'names': ['John','Paul','George','Ringo']}
    return template("index5.tp1",info)

@error(404)
def villa(error):
    return "<h2 style='color:red'>Þessi síða finnst ekki</h2>"


run(host="localhost",port=8080,reloader=True,debug=True)
