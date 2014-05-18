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

CREATE TABLE DaysOfWeek(
	ID INTEGER PRIMARY KEY,
	Day TEXT NOT NULL
);

CREATE TABLE TransportTypes(
	ID INTEGER PRIMARY KEY,
	Type TEXT NOT NULL UNIQUE
);

INSERT INTO EventTypes (Event) VALUES
('TransportCostUpdate');
INSERT INTO EventTypes (Event) VALUES
('CustomerPriceUpdate');
INSERT INTO EventTypes (Event) VALUES
('TransportDiscontinued');
INSERT INTO EventTypes (Event) VALUES
('MailDelivery');
	
INSERT INTO DaysOfWeek(Day) VALUES
('Sunday');
INSERT INTO DaysOfWeek(Day) VALUES
('Monday');
INSERT INTO DaysOfWeek(Day) VALUES
('Tuesday');
INSERT INTO DaysOfWeek(Day) VALUES
('Wednesday');
INSERT INTO DaysOfWeek(Day) VALUES
('Thursday');
INSERT INTO DaysOfWeek(Day) VALUES
('Friday');
INSERT INTO DaysOfWeek(Day) VALUES
('Saturday');

INSERT INTO TransportTypes(Type) VALUES
('Air');
INSERT INTO TransportTypes(Type) VALUES
('Land');
INSERT INTO TransportTypes(Type) VALUES
('Sea');
