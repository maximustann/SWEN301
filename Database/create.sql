CREATE TABLE BusinessEvents(
	ID INTEGER PRIMARY KEY NOT NULL,
	EventTypeID INT,
	Origin INT,
	Destination INT,
	Weight REAL,
	Volume REAL,
	TimeOfEntry DATETIME,
	Priority INT,
	PricePerGram REAL,
	PricePerCC REAL,
	Firm Text,
	TransportType TEXT,
	DayOfWeek INT,
	Frequency REAL,
	Duration REAL);
CREATE TABLE EventTypes(
	Event TEXT NOT NULL,
	EventTypeID INTEGER NOT NULL);
CREATE TABLE TransportRoutes(
	ID INTEGER PRIMARY KEY NOT NULL,
	EventID INT );
CREATE TABLE CustomerRoutes(
	ID INTEGER PRIMARY KEY NOT NULL,
	EventID INT);
