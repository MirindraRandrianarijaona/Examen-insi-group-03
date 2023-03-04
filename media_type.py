import web
import nav
from DB import Db 
web.config.debug = True

urls = (
    '/', 'media',
    '/index', 'index',
    '/media', 'media'
)

class media:
    def GET(self):
        d = Db()
        db = d.getDb()
        media_types=db.select('MediaType', limit=10)
        result = '<html><head><title>Media_type.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<div class="container">'
        result += '<h2 style="text-align: center;">Liste des media type</h2>'
        result += '<table class="table">'
        result += '<thead class="table table-dark">'
        result += '<tr><th>Media type</th></tr>'
        result += '</thead>'
        result += '<tbody class="table-primary">'
        for media_type in media_types:
            result +='<tr>'
            result +='<td>'+media_type.Name+'</td>'
            result +='</tr>'
        result += '</tbody>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()