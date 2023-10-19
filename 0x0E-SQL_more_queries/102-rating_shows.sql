-- Selecting tv_shows.title and the sum of ratings for each show
-- by joining tv_shows with tv_show_ratings table and calculating rating sums

-- Step 1: Selecting show titles from tv_shows table and sum of ratings from tv_show_ratings table
SELECT CONCAT(tv_shows.title, ' - ', IFNULL(SUM(tv_show_ratings.rate), 0)) AS 'Show - Rating Sum'
-- Step 2: Left join tv_show_ratings table to tv_shows table using show_id
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
-- Step 3: Group the results by show titles
GROUP BY tv_shows.title
-- Step 4: Order results in descending order by rating sum
ORDER BY SUM(tv_show_ratings.rate) DESC;
