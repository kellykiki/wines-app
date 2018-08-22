from flask_frozen import Freezer
from app import app, Wine

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def wine():
    for wine in Wine.query.all():
        yield { 'index': wine.index }

if __name__ == '__main__':
    freezer.freeze()