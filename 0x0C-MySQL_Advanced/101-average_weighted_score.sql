-- procedure
--
delimiter ??

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(b.weight * a.score) / SUM(b.weight) FROM corrections AS a
        RIGHT JOIN projects AS b ON a.project_id = b.id
        WHERE a.user_id = users.id
    );
END??
