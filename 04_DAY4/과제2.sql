CREATE TABLE PetOwners (
    ownerID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(255)
);

CREATE TABLE Pets (
    petID INT AUTO_INCREMENT PRIMARY KEY,
    ownerID INT NOT NULL,
    FOREIGN KEY (ownerID) REFERENCES PetOwners(ownerID),
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50),
    breed VARCHAR(50)
);

CREATE TABLE Rooms (
    roomID INT AUTO_INCREMENT PRIMARY KEY,
    roomNumber VARCHAR(50) NOT NULL UNIQUE,
    roomType VARCHAR(50),
    pricePerNight DECIMAL(10,2) NOT NULL
);

CREATE TABLE Reservations (
    reservationID INT AUTO_INCREMENT PRIMARY KEY,
    petID INT NOT NULL,
    FOREIGN KEY (petID) REFERENCES Pets(petID),    
    roomID INT NOT NULL,
    FOREIGN KEY (roomID) REFERENCES Rooms(roomID),
    startDate DATE NOT NULL,
    endDate DATE NOT NULL
);

CREATE TABLE Services (
    serviceID INT AUTO_INCREMENT PRIMARY KEY,
    reservationID INT NOT NULL,
    FOREIGN KEY (reservationID) REFERENCES Reservations(reservationID)    ,
    serviceName VARCHAR(100),
    servicePrice DECIMAL(10,2)
);