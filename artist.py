import web
import nav
from DB import Db 
web.config.debug = True

urls = (
    '/', 'artist',
    '/index', 'index',
    '/artist', 'artist'
)

class artist:
    def GET(self):
        d = Db()
        db = d.getDb()
        albumids=db.select('Album', limit=10)
        artists=db.select('Artist', limit=10)
        result = '<html><head><title>Artist.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<div class="container">'
        result += '<h2 style="text-align: center;">Liste des artistes</h2>'
        result += '<table class="table">'
        result += '<thead class="table table-dark">'
        result += '<tr><th>Id</th><th>Artists</th></tr>'
        result += '</thead>'
        result += '<tbody class="table-primary">'
        for artist in artists:
            result +='<tr>'
            for albumid in albumids:
                result +='<td>'+str(albumid.AlbumId)+'</td>'
                break
            result +='<td>'+artist.Name+'</td>'
            result +='</tr>'
        result += '</tbody>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()