import web
import nav
from DB import Db 
web.config.debug = True

urls = (
    '/', 'genre',
    '/index','index',
    '/genre', 'genre'
)

class genre:
    def GET(self):
        d = Db()
        db = d.getDb()
        albumids=db.select('Album', limit=10)
        genres=db.select('Genre', limit=10)
        result = '<html><head><title>Genre.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<div class="container">'
        result += '<h2 style="text-align: center;">Liste des genres</h2>'
        result += '<table class="table  text-center">'
        result += '<thead class="table table-dark">'
        result += '<tr><th>Id</th><th>Genre</th></tr>'
        result += '</thead>'
        result += '<tbody class="table-primary">'
        for genre in genres:
            result +='<tr>'
            for albumid in albumids:
                result +='<td>'+str(albumid.AlbumId)+'</td>'
                break
            result += '<td>' + genre.Name + '</td>'
            result +='</tr>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()