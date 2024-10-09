# Project Setup Guide

This document provides a comprehensive guide to set up the project, covering dependency installation, MongoDB configuration via Docker, and the initiation of backend and frontend services.

## 1. Downloading the Project and Installing Dependencies

### Step 1: Cloning the Repository

To begin, clone the project repository to your local machine:

```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Installing Python and Required Packages

Ensure you have Python installed (version 3.8 or higher is recommended). You will also need `pip` to install the required Python packages:

```bash
pip install -r backend/requirements.txt
```

### Step 3: Installing Node.js and Docker

To run the frontend and MongoDB, it is essential to have **Node.js** and **Docker** installed.

- **Node.js**: Download and install from the [official Node.js website](https://nodejs.org/).
- **Docker**: Download and install from the [official Docker website](https://www.docker.com/).

## 2. Running MongoDB with Docker and Loading Data

### Step 1: Pull the MongoDB Docker Image

First, download the MongoDB image from Docker Hub:

```bash
docker pull mongo
```

### Step 2: Run the MongoDB Container

Start the MongoDB container, mapping it to port `27017` and persisting the data using a local volume:

```bash
docker run --name mongodb-container -d -p 27017:27017 -v ~/mongodb-data:/data/db mongo
```

### Step 3: Load Data into MongoDB

To load data from the `data.json` file into the MongoDB container, execute the following steps:

1. Copy the `data.json` file into the MongoDB container:

   ```bash
   docker cp /path/to/data.json mongodb-container:/data.json
   ```

2. Access the MongoDB container's shell:

   ```bash
   docker exec -it mongodb-container bash
   ```

3. Import the data into the `sample_supplies` database:

   ```bash
   mongoimport --db sample_supplies --collection sales --file /data.json --jsonArray
   ```

## 3. Running the Backend

Navigate to the backend directory and start the FastAPI server using **Uvicorn**:

```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The backend will now be running and accessible at `http://localhost:8000`.

## 4. Running the Frontend

Navigate to the frontend directory and start the development server:

```bash
cd ../frontend
npm install  # Install necessary dependencies
npm run dev  # Start the development server
```

The frontend will be available at `http://localhost:3000`.

## Summary

- **Clone the repository** and install **Python**, **Node.js**, and **Docker**.
- **Run MongoDB** within a Docker container and import the data from `data.json`.
- **Start the backend** service using **Uvicorn**.
- **Start the frontend** using `npm run dev`.

Upon completing these steps, you should have the application running successfully. If any issues arise, please consult the project's documentation or contact support for further assistance.
