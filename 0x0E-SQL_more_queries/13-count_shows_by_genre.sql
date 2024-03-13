-- script that lists all shows contained in hbtn_0d_tvshows that have at least
SELECT DISTINCT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_show_genres
 INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id 
 INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id  
 GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
