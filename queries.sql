USE fifa_wc2026;

-- Delete all rows from fact table first (FK constraint order matters)
DELETE FROM fact_performance;
DELETE FROM dim_players;
DELETE FROM dim_matches;

-- Reset the auto increment counter
ALTER TABLE fact_performance AUTO_INCREMENT = 1;

-- Verify all are empty
SELECT COUNT(*) FROM fact_performance;
SELECT COUNT(*) FROM dim_players;
SELECT COUNT(*) FROM dim_matches;
