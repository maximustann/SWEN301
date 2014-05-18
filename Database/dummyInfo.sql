INSERT INTO Company(Name) VALUES("Nz Air");
INSERT INTO company(Name) VALUES("Planet Express");


INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 2, 2, "Air", 1, 1.2, 1.5, 36, 1);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 2, 2, "Land", 2, 1, 1, 36, 12);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(2, 3, 1, "Land", 2, 2, 1, 36, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(2, 4, 1, "Land", 3, 2, 1, 36, 3);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 5, 1, "Land", 4, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(3, 5, 2, "Air", 5, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(5, 6, 2, "Land", 6, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(6, 7, 2, "Land", 7, 1.6, 1.2, 37, 2);

INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 2, 2, "Land", 7, 6, 6, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 5, 1, "Land", 7, 3, 3, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(2, 3, 2, "Land", 7, 7, 7, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(3, 4, 3, "Land", 7, 8, 8, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(5, 6, 2, "Land", 7, 4, 4, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(6, 7, 1, "Land", 7, 5, 5, 37, 2);



INSERT INTO CustomerRoutes(Origin, Destination, Priority, PricePerGram, PricePerCC) VALUES(1, 7, 2, 1.7, 1.3);
INSERT INTO CustomerRoutes(Origin, Destination, Priority, PricePerGram, PricePerCC) VALUES(1, 2, 1, 2, 2);
INSERT INTO CustomerRoutes(Origin, Destination, Priority, PricePerGram, PricePerCC) VALUES(1, 3, 2, 1.7, 1.3);



