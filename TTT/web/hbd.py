from flask import Blueprint,render_template

hbd = Blueprint('hbd',__name__,template_folder='TTT/web/static')

@hbd.route('/')
def card():
    return render_template('card.html')
