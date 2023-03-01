FROM python:3-bullseye

RUN apt update
RUN apt install mariadb-client -y
RUN pip install --no-cache-dir --upgrade web.py mysqlclient
COPY ./server.py /server.py
COPY ./DB.py /DB.py
COPY ./album.py /album.py
COPY ./artist.py /artist.py
COPY ./genre.py /genre.py
COPY ./media_type.py /media_type.py
COPY ./playlist.py /playlist.py
COPY ./track.py /track.py
CMD [ "python", "/server.py" ]
