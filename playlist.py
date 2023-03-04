import web
import nav
from DB import Db 
web.config.debug = True

urls = (
    '/', 'playlist',
    '/index', 'index',
    '/playlist', 'playlist'
)

class playlist:
    def GET(self):
        d = Db()
        db = d.getDb()
        playlists=db.select('Playlist', limit=10)
        result = '<html><head><title>Playlist.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<div class="container">'
        result += '<h2 style="text-align: center;">Liste des playlists</h2>'
        result += '<table class="table">'
        result += '<thead class="table table-dark">'
        result += '<tr><th>Playlist</th></tr>'
        result += '</thead>'
        result += '<tbody class="table-primary">'
        for playlist in playlists:
            result +='<tr>'
            result +='<td>'+playlist.Name+'</td>'
            result +='</tr>'
        result += '</tbody>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()