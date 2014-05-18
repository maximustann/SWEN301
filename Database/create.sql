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
	Company TEXT,
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
	Company TEXT,
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
	TimeOfEntry INTEGER,
	DeliverTime INTEGER
);

CREATE TABLE Cities(
	ID INTEGER PRIMARY KEY,
	Name TEXT NOT NULL
);

CREATE TABLE DaysOfWeek(
	ID INTEGER PRIMARY KEY,
	Day TEXT NOT NULL
);

CREATE TABLE TransportTypes(
	ID INTEGER PRIMARY KEY,
	Type TEXT NOT NULL
);

CREATE TABLE Priorities(
	ID INTEGER PRIMARY KEY,
	Priority TEXT NOT NULL
);


INSERT INTO EventTypes (Event) VALUES
('Transport Cost Update');
INSERT INTO EventTypes (Event) VALUES
('Customer Price Update');
INSERT INTO EventTypes (Event) VALUES
('Transport Discontinued');
INSERT INTO EventTypes (Event) VALUES
('Mail Delivery');
	
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

INSERT INTO Priorities(Priority) VALUES
('Standard');
INSERT INTO Priorities(Priority) VALUES
('Air');

CREATE VIEW CustomerDisplayRoutes AS 
  SELECT origin.Name AS Origin, 
         dest.Name AS Destination, 
         prior.Priority AS Priority,
         PricePerGram, PricePerCC
  FROM CustomerRoutes AS CR
  JOIN Cities AS origin ON CR.Origin = origin.ID
  JOIN Cities AS dest ON CR.Destination = dest.ID
  JOIN Priorities AS prior ON CR.Priority = prior.ID;

CREATE VIEW TransportDisplayRoutes AS
SELECT origin.Name AS Origin, 
         dest.Name AS Destination, 
	 Company,
         TransportType, DeliverDay,
         PricePerGram, PricePerCC,
         Frequency, Duration
  FROM TransportRoutes AS TR
  JOIN Cities AS origin ON TR.Origin = origin.ID
  JOIN Cities AS dest ON TR.Destination = dest.ID;
