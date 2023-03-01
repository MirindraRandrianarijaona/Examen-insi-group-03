def nav():
    result = '<nav class="navbar navbar-expand-sm bg-dark navbar-dark justify-content-center">'
    result += '<ul class="navbar-nav">'
    result += '<li class="nav-item"><a class="nav-link" href="/index">Accueil</a></li>'
    result += '<li class="nav-item"><a class="nav-link" href="/genre">Genre</a></li>'
    result += '<li class="nav-item"><a class="nav-link" href="/artist">Artists</a></li>'
    result += '<li class="nav-item"><a class="nav-link" href="/album">Album</a></li>'
    result += '<li class="nav-item"><a class="nav-link" href="/track">Track</a></li>'
    result += '<li class="nav-item"><a class="nav-link" href="/media">Media type</a></li>'
    result += '<li class="nav-item"><a class="nav-link" href="/playlist">Playlist</a></li>'
    result += '</ul>'
    result += '</nav>'
    return result