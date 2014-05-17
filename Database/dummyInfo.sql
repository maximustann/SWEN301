INSERT INTO Cities(Name) VALUES("Wellington");
INSERT INTO Cities(Name) VALUES("Auckland");
INSERT INTO Cities(Name) VALUES("Hamilton");
INSERT INTO Cities(Name) VALUES("Rotorua");
INSERT INTO Cities(Name) VALUES("Palmeston North");
INSERT INTO Cities(Name) VALUES("Dunedin");
INSERT INTO Cities(Name) VALUES("Christchurch");


INSERT INTO Company(Name) VALUES("Nz Air");
INSERT INTO company(Name) VALUES("Planet Express");


INSERT INTO EventTypes(Event) VALUES("Mail Delivery");
INSERT INTO EventTypes(Event) VALUES("Customer Price Update");
INSERT INTO EventTypes(Event) VALUES("Transport Cost Update");
INSERT INTO EventTypes(Event) VALUES("Transport Discontinued");



INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 2, 2, "Air", 1, 1.2, 1.5, 36, 1);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 2, 2, "Land", 2, 1, 1, 36, 12);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(2, 3, 1, "Land", 2, 2, 1, 36, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(2, 4, 1, "Land", 3, 2, 1, 36, 3);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(1, 5, 1, "Land", 4, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(3, 5, 2, "Air", 5, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(5, 6, 2, "Land", 6, 1.6, 1.2, 37, 2);
INSERT INTO TransportRoutes(Origin, Destination, Company, TransportType, DeliverDay, PricePerGram, PricePerCC, Frequency, Duration) VALUES(6, 7, 2, "Land", 7, 1.6, 1.2, 37, 2);



INSERT INTO CustomerRoutes(Origin, Destination, Priority, TransportType, PricePerGram, PricePerCC) VALUES(1, 7, 2, "Land", 1.7, 1.3);
INSERT INTO CustomerRoutes(Origin, Destination, Priority, TransportType, PricePerGram, PricePerCC) VALUES(1, 2, 1, "Air", 2, 2);
INSERT INTO CustomerRoutes(Origin, Destination, Priority, TransportType, PricePerGram, PricePerCC) VALUES(1, 3, 2, "Land", 1.7, 1.3);



