
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Tableros` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`idTablero`	INTEGER NOT NULL,
	`numeroColumna`	INTEGER,
	`numeroFila`	INTEGER,
	`valor`	INTEGER
);
INSERT INTO `Tableros` VALUES (2,0,0,0,1);
INSERT INTO `Tableros` VALUES (3,0,1,0,2);
INSERT INTO `Tableros` VALUES (4,0,2,0,3);
INSERT INTO `Tableros` VALUES (5,0,2,1,3);
INSERT INTO `Tableros` VALUES (6,0,1,1,1);
INSERT INTO `Tableros` VALUES (7,0,0,1,2);
INSERT INTO `Tableros` VALUES (8,1,0,0,3);
INSERT INTO `Tableros` VALUES (9,1,1,0,2);
INSERT INTO `Tableros` VALUES (10,1,1,1,1);
INSERT INTO `Tableros` VALUES (11,1,0,1,3);
INSERT INTO `Tableros` VALUES (12,1,0,2,1);
INSERT INTO `Tableros` VALUES (13,1,1,2,2);
INSERT INTO `Tableros` VALUES (14,2,0,0,4);
INSERT INTO `Tableros` VALUES (15,2,1,0,3);
INSERT INTO `Tableros` VALUES (16,2,2,0,1);
INSERT INTO `Tableros` VALUES (17,2,3,0,2);
INSERT INTO `Tableros` VALUES (18,2,3,1,5);
INSERT INTO `Tableros` VALUES (19,2,2,1,4);
INSERT INTO `Tableros` VALUES (20,2,1,1,2);
INSERT INTO `Tableros` VALUES (21,2,0,1,1);
INSERT INTO `Tableros` VALUES (22,2,0,2,6);
INSERT INTO `Tableros` VALUES (23,2,1,2,5);
INSERT INTO `Tableros` VALUES (24,2,2,2,3);
INSERT INTO `Tableros` VALUES (25,2,3,2,6);
CREATE TABLE IF NOT EXISTS `Raking` (
	`idJugador`	INTEGER,
	`Puntaje`	INTEGER,
	FOREIGN KEY(`idJugador`) REFERENCES `Jugadores`(`id`)
);
CREATE TABLE IF NOT EXISTS `Jugadores` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`nombre`	TEXT,
	`contraseña`	TEXT
);
INSERT INTO `Jugadores` VALUES (1,'Martin','123');
INSERT INTO `Jugadores` VALUES (2,'admin','admin');
COMMIT;
