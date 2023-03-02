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
        a2=db.select('Album', limit=10)
        albumids=db.select('Album', limit=10)
        artists=db.select('Artist', limit=10)
        genres=db.select('Genre', limit=10)
        media_types=db.select('MediaType', limit=10)
        playlists=db.select('Playlist', limit=10)
        tracks=db.select('Track', limit=10)
        result = '<html><head><title>Gestionnaire de musiques</title></head>'
        result = '<html><head><title>Server.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<div class="container">'
        result += '<h2 style="text-align: center;">Liste principale</h2>'
        result += '<table class="table">'
        result += '<thead class="table-dark">'
        result += '<tr><th>Id</th><th>Genre</th><th>Artists</th><th>Album</th><th>Track</th><th>Media type</th><th>Playlist</th></tr>'
        result += '</thead>'
        result += '<tbody class="table-primary">'
        for playlist in playlists:
            result +='<tr>'
            for albumid in albumids:
                result +='<td>'+str(albumid.AlbumId)+'</td>'
                break
            for genre in genres:
                result +='<td>'+genre.Name+'</td>'
                break
            for artist in artists:
                result +='<td>'+artist.Name+'</td>'
                break
            for a in a2:
                result +='<td>'+a.Title+'</td>'
                break
            for track in tracks:
                result +='<td>'+track.Name+'</td>'
                break
            for media_type in media_types:
                result +='<td>'+media_type.Name+'</td>'
                break
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
