# Project Overview

This project is designed to streamline access to and adjustment of crucial data feeds, essential for trading analysis and stock price monitoring. The meticulously configured data is seamlessly integrated into Perspective, thereby augmenting trading insights.

To provide traders with a comprehensive view of all monitored trading strategies, multiple screens typically exhibit a diverse range of live and historical data at their workstations. This holistic approach ensures traders are well-informed and equipped to make informed decisions.

Given the substantial influx of information and data, clear visualization is imperative, considering UI/UX considerations. This clarity plays a pivotal role in empowering traders with effective tools to enhance their performance in the trading domain.

## Dockerization

To Dockerize the project, follow these instructions carefully:

1. Start your Docker Desktop application.

2. Create a `Dockerfile` for both the backend and frontend in their respective folders. This means you should create a `Dockerfile` file inside the `frontend` folder and also inside the `backend` folder.

3. Navigate back to the root folder and create a `docker-compose.yml` file that will contain both the frontend and backend services. Write the YAML for the services which will start the containers.

4. Run the command below to start the `docker-compose.yml` file that will run both the frontend and backend containers:

    ```bash
    docker-compose up -d
    ```

5. To stop the containers, run:

    ```bash
    docker-compose down
    ```

6. To remove the volumes associated with each container, run:

    ```bash
    docker-compose down -v
    ```

7. Navigate to your Docker Desktop to see the status of your containers and ensure they are running smoothly.

Following these steps ensures a smooth Dockerization of the project, enabling seamless deployment and management of both frontend and backend services.
