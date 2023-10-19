-- Selecting tv_shows.title and the sum of ratings for each show
-- by joining tv_shows with tv_show_ratings table and calculating rating sums
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
