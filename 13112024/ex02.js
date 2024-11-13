// Define the student object
const student = {
    name: "ksr",
    dept: "Aiml",
    courses: ["cse", "aids", "aiml", "csbs"],
    
    // Method to print a greeting message
    greeting() {
        let msg = `My name is ${this.name} and dept is ${this.dept}`;
        console.log(msg);
    },

    // Method to list all the courses
    listCourses() {
        console.log(`Courses: ${this.courses.join(", ")}`);
    }
};

// Calling the methods
student.greeting();
student.listCourses();