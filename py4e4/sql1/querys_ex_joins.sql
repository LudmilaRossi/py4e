INSERT INTO Artist (name) VALUES ('Led Zeppelin');
INSERT INTO Artist (name) VALUES ('AC/DC')

INSERT INTO Genre (name) VALUES ('Rock');
INSERT INTO Genre (name) VALUES ('Metal')

INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1)

INSERT INTO Track (title,rating, len, count, album_id, genre_id) VALUES ('Black Dog', 5, 297, 0, 2, 1);
INSERT INTO Track (title,rating, len, count, album_id, genre_id) VALUES ('Stairway', 5, 482, 0, 2, 1);
INSERT INTO Track (title,rating, len, count, album_id, genre_id) VALUES ('About to Rock', 5, 313, 0, 1, 2);
INSERT INTO Track (title,rating, len, count, album_id, genre_id) VALUES ('Who made Who', 5, 207, 0, 1, 2)

SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id
SELECT Track.title, 
	Genre.name 
	FROM Track JOIN Genre 
	ON Track.genre_id = Genre.id
	
SELECT Track.title, Artist.Name, Album.title, Genre.name 
	FROM Track JOIN Genre JOIN Album JOIN Artist
	ON Track.genre_id = Genre.id AND
	Track.album_id = Album.id AND 
	Album.artist_id = Artist.id
	