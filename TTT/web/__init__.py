from flask import Flask 

def create_app():
    app = Flask (__name__)
    
    from .view import view
    from .all_funcs import all_funcs
    from.hbd import hbd
    
    app.register_blueprint(view,url_prefix='/')
    
    ## this is the test unit (including the import) 
    
    app.register_blueprint(all_funcs,url_prefix='/play')
    
    ##this for the BD card html
    
    app.register_blueprint(hbd, url_prefix='/go')
    
    ## end of test 
    
    return app
