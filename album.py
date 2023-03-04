import web
import nav
from DB import Db 
web.config.debug = True

urls = (
    '/', 'album',
    '/index','index',
    '/album', 'album'
)

class album:
    def GET(self):
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=10)
        albumids=db.select('Album', limit=10)
        result = '<html><head><title>Album.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<div class="container">'
        result += '<h2 style="text-align: center;">Liste des albums</h2>'
        result += '<table class="table text-center">'
        result += '<thead class="table-dark">'
        result += '<tr><th>Id</th><th>Album</th></tr>'
        result += '</thead>'
        result += '<tbody class="table-primary">'
        for a in a2:
            result +='<tr>'
            for albumid in albumids:
                result +='<td>'+str(albumid.AlbumId)+'</td>'
                break
            result +='<td>'+a.Title+'</td>'
            result +='</tr>'
        result += '</tbody>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()