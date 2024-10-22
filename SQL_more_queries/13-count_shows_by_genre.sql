-- 13-count_shows_by_genre.sql
USE `hbtn_0d_tvshows`;
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY tv_show_genres.genre_id
HAVING COUNT(tv_shows.id) > 0
ORDER BY number_of_shows DESC;