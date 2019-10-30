BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "deltagere" (
	"ID"	INTEGER NOT NULL,
	"fnavn"	TEXT NOT NULL,
	"enavn"	TEXT NOT NULL,
	"bord"	TEXT NOT NULL,
	"klasse"	TEXT NOT NULL,
	PRIMARY KEY("ID")
);
INSERT INTO "deltagere" VALUES (1,'Jonas','Dreiøe','0','2.i');
INSERT INTO "deltagere" VALUES (3,'Pia','Olsen','1','2a');
INSERT INTO "deltagere" VALUES (4,'Jonas','Dreiøe','0','2.i');
COMMIT;
