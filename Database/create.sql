CREATE TABLE BusinessEvents(
	ID INTEGER PRIMARY KEY NOT NULL,
	EventTypeID INT,
	Origin INT REFERENCES Cities(ID),
	Destination INT REFERENCES Cities(ID),
	Weight REAL,
	Volume REAL,
	TimeOfEntry INTEGER,
	Priority INT,
	PricePerGram REAL,
	PricePerCC REAL,
	Company INT REFERENCES Company(ID),
	TransportType TEXT,
	DayOfWeek INT,
	Frequency REAL,
	Duration REAL);
CREATE TABLE EventTypes(
	EventTypeID INTEGER PRIMARY KEY,
	Event TEXT NOT NULL);
CREATE TABLE TransportRoutes(
	ID INTEGER 	PRIMARY KEY,
	Origin INT REFERENCES Cities(ID),
	Destination INT REFERENCES Cities(ID),
	Company INT REFERENCES company(ID),
	TransportType TEXT,
	DeliverDay INT,
	PricePerGram REAL,
	PricePerCC REAL,
	Frequency REAL,
	Duration REAL
);
CREATE TABLE CustomerRoutes(
	ID INTEGER PRIMARY KEY,
	Origin INT REFERENCES Cities(ID),
	Destination INT REFERENCES Cities(ID),
	Priority INT,
	TransportType TEXT,
	PricePerGram REAL,
	PricePerCC REAL
);

CREATE TABLE Mail(
	ID INTEGER PRIMARY KEY,
	Origin INT REFERENCES Cities(ID),
	Destination INT REFERENCES Cities(ID),
	costKPS REAL,
	costClient REAL,	
	Priority INT,
	Volume REAL,
	Weight	REAL,
	TimeOfEntry INTEGER
);

CREATE TABLE Cities(
	ID INTEGER PRIMARY KEY,
	Name TEXT NOT NULL
);
CREATE TABLE Company(
	ID INTEGER PRIMARY KEY,
	Name TEXT NOT NULL
);
