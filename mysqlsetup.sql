CREATE USER 'useextractor'@'localhost' IDENTIFIED BY 'extractor';
CREATE DATABASE gamerdb;
GRANT ALL PRIVILEGES ON gamerdb TO 'useextractor'@'localhost';
CREATE TABLE users (
	pid MEDIUMINT, 
	tag CHAR(16) CHARSET utf8,
	rank MEDIUMINT,
	country VARCHAR(20),
	PRIMARY KEY(pid),
	KEY (tag),
	KEY (country)
	);
CREATE TABLE history (
	blogid INT,
	tag CHAR(16) CHARSET utf8,
	entrydate DATE,
	body TEXT CHARSET utf8,
	PRIMARY KEY (blogid),
	KEY (tag),
	FULLTEXT(body)
	);

ALTER TABLE history DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER DATABASE DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

