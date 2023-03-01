import web
import nav
from DB import Db 
web.config.debug = True

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=2)
        result = '<html><head><title>test</title></head>'
        result = '<html><head><title>Server.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        for a in a2:
            result += a.Title + ',(' + str(a.ArtistId) + ') <br/>'
        result += '</body></html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
