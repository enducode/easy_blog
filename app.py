import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_DEFAULT_MIMETYPE = 'text/html'

app = Flask(__name__)
app.config.from_object(__name__)
flatPages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
def index():
    pages = (p for p in flatPages if 'date' in p.meta)
    return render_template('index.html', pages = pages)

@app.route('/page/<path:path>/')
def page(path):
    page = flatPages.get_or_404(path)
    return render_template('page.html', page=page), 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run()