
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 2, 'Meowland', "Air", 1, 1.2, 1.5, 36, 1);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 2, 'Woofland', "Land", 2, 1, 1, 36, 12);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(2, 3, 'Meowland', "Land", 2, 2, 1, 36, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(2, 4, 'Meowland', "Land", 3, 2, 1, 36, 3);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 5, 'Meowland', "Land", 4, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(3, 5, 'Woofland', "Air", 5, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(5, 6, 'Woofland', "Land", 6, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(6, 7, 'Woofland', "Land", 7, 1.6, 1.2, 37, 2);

INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 2, 'Woofland', "Land", 7, 6, 6, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 5, 'Meowland', "Land", 7, 3, 3, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(2, 3, 'Woofland', "Land", 7, 7, 7, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(3, 4, 'Rrawkland', "Land", 7, 8, 8, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(5, 6, 'Woofland', "Land", 7, 4, 4, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(6, 7, 'Meowland', "Land", 7, 5, 5, 37, 2);



INSERT INTO CustomerRoutes(Origin, Destination, Priority, PricePerGram, PricePerCC) VALUES(1, 7, 2, 1.7, 1.3);
INSERT INTO CustomerRoutes(Origin, Destination, Priority, PricePerGram, PricePerCC) VALUES(1, 2, 1, 2, 2);
INSERT INTO CustomerRoutes(Origin, Destination, Priority, PricePerGram, PricePerCC) VALUES(1, 3, 2, 1.7, 1.3);

INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(1, 2, 4.0, 6.0, 1, 5.0, 5.0, 1, 1);
INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(1, 2, 3.0, 6.0, 1, 5.0, 5.0, 1, 1);
INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(1, 2, 9.0, 6.0, 1, 5.0, 5.0, 1, 1);
INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(1, 2, 31.0, 4.0, 1, 5.0, 5.0, 1, 1);
INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(1, 3, 9.0, 6.0, 1, 5.0, 5.0, 1, 1);
INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(1, 3, 34.0, 4.0, 1, 5.0, 5.0, 1, 1);
INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(1, 3, 9.0, 6.0, 2, 5.0, 5.0, 1, 1);
INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(1, 3, 34.0, 4.0, 2, 5.0, 5.0, 1, 1);

