from flask import Blueprint,render_template
site = Blueprint('site',__name__,template_folder='site_templates')
#names tell it to look in the __init__.py folder
#the template_folder tells it that the templates for the site are in the sites_template

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')