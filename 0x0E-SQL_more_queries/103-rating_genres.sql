-- Selecting tv_genres.name and the sum of ratings for each genre
-- by joining tv_genres with tv_show_genres and tv_show_ratings tables and calculating rating sums

-- Step 1: Selecting genre names from tv_genres table and sum of ratings from tv_show_ratings table
SELECT CONCAT(tv_genres.name, ' - ', IFNULL(SUM(tv_show_ratings.rate), 0)) AS 'Genre - Rating Sum'
-- Step 2: Joining tv_genres with tv_show_genres table using genre_id
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Step 3: Left join tv_show_ratings table to tv_show_genres table using show_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
-- Step 4: Group the results by genre names
GROUP BY tv_genres.name
-- Step 5: Order results in descending order by rating sum
ORDER BY SUM(tv_show_ratings.rate) DESC;
