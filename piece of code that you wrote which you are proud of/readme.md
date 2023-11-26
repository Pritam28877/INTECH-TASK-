# Notes App using Node.js and MongoDB

## Overview
This repository contains the code for a Notes App implemented using Node.js and MongoDB. The application provides a dashboard for users to manage their notes, including features such as pagination, viewing, updating, deleting, adding, and searching notes.

## Prerequisites
Make sure you have the following installed on your machine:
- Node.js
- MongoDB

## Getting Started
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Pritam28877/Notes-App-Nodejs.git
   ```

2. Install dependencies:
   ```bash
   cd Notes-App-Nodejs
   npm install
   ```

3. Set up your MongoDB database and update the connection details in the `config/database.js` file.

4. Start the application:
   ```bash
   npm start
   ```

5. Open your browser and visit [http://localhost:3000](http://localhost:3000) to access the application.

## Features

### 1. Dashboard
- The dashboard displays a paginated list of notes for the currently logged-in user.
- Each note is truncated to show a brief preview of the title and body.

### 2. View Specific Note
- Clicking on a note in the dashboard takes you to a detailed view of that particular note.

### 3. Update Note
- You can edit and update a specific note by navigating to the note view and making changes.

### 4. Delete Note
- Notes can be deleted, and the dashboard is updated accordingly.

### 5. Add Note
- Users can add new notes by visiting the "Add Note" page.

### 6. Search Notes
- The application provides a search functionality to find notes based on titles and bodies.
- Search results are displayed in a paginated manner.

## Directory Structure
- `controller/dashboardController.js`: Contains the main logic for handling dashboard-related actions.
- `models/Notes.js`: Defines the MongoDB schema for the `Note` model.
- `views/`: Contains the EJS templates for rendering different pages.
- `routes/`: Defines the routes for different actions (viewing, updating, deleting, adding, searching notes).

## Credits
This project was developed by [Your Name] as a part of [mention any course or learning resources].

Feel free to explore, modify, and enhance the application based on your requirements. If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository.

Happy coding! 🚀