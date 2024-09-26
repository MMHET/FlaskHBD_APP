from flask import Blueprint,render_template
import time

view = Blueprint('view',__name__,template_folder='web/static')

def timelocal():
    curr_time = time.strftime("%H:%M", time.localtime())
    
    return curr_time

@view.route('/')
def home():
    curr_time = timelocal()
    return render_template("index.html", curr_time = curr_time) ## Change this from render.html to index html since thisis the first page 

'TT7\web\static\render.html'
