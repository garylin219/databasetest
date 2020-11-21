CREATE DATABASE memberData;
use memberData;

CREATE TABLE IF NOT EXISTS memberList (
    `SID` VARCHAR(9) CHARACTER SET utf8,
    `name` VARCHAR(15) CHARACTER SET utf8
);

INSERT INTO memberList VALUES
	('CBB107012','ChiWei'),
	('CBB107018','JingXuan'),
	('CBB107038','HongWei'),
	('CBB107039','ShangSheng'),
	('CBB107041','HueiKai');
