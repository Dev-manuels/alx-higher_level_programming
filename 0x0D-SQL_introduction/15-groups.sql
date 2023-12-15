-- script that lists the number of records with the same score
-- in table second_table
SELECT score, COUNT(*) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY number DESC;
