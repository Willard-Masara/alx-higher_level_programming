-- Selecting tv_shows.title from shows without the genre "Comedy"
-- by joining tv_shows, tv_show_genres, and tv_genres tables

-- Step 1: Select tv_shows.title from tv_shows table
SELECT tv_shows.title
-- Step 2: Left join tv_show_genres table to tv_shows table using show_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Step 3: Left join tv_genres table to tv_show_genres table using genre_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Step 4: Filter shows where genre is not "Comedy" (genre_id for Comedy is 5)
WHERE tv_genres.id IS NULL OR tv_genres.id != 5
-- Step 5: Order results in ascending order by show title
ORDER BY tv_shows.title ASC;

