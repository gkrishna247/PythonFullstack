// Define the Car class
class Car {
    constructor(model, year, isAvailable) {
        this.model = model;
        this.year = year;
        this.isAvailable = isAvailable;
    }

    // Method to check out the car
    checkout() {
        console.log(this.isAvailable 
            ? `${this.model} has been checked out.` 
            : `${this.model} is not available.`);
        this.isAvailable = false; // Mark as unavailable after checkout
    }

    // Method to check in the car
    checkin() {
        console.log(!this.isAvailable 
            ? `${this.model} has been checked in.` 
            : `${this.model} was already available.`);
        this.isAvailable = true; // Mark as available after check-in
    }
}

// Create car objects
const car1 = new Car("Tesla Model S", 2023, true);
const car2 = new Car("Honda Civic", 2020, false);

// Perform check-in and check-out operations
console.log(car1.model);
car1.checkout();
car1.checkin();

console.log(car2.model);
car2.checkout();
car2.checkin();