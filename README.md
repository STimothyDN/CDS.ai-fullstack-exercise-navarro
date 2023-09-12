# CDS.ai Full-Stack Developer Exercise

## About this repository

This repository includes a barebones full-stack web application built with the following technologies:

* Backend
  * Python
  * [FastAPI](https://fastapi.tiangolo.com/)
  * [Pandas](https://pandas.pydata.org/)
* Frontend
  * Javascript
  * [Vue.js](https://vuejs.org/)
  * [Chart.js](https://www.chartjs.org/docs/latest/)

This application mimics a standard data visualization application at CDS.ai - a Python-based backend reads data, manipulates it, and returns it. A Javascript-based frontend retrieves this data from the backend and visualizes it.

## The Exercise
In this exercise, developer candidates are expected to spend no more than 2-4 hours on tasks of their choosing and provide their repository to our interviewers prior to their interview. 

The intent of this exercise is to give us a starting point for conversation rather than a gatekeeping test of developer ability. Come prepared to talk about your solution(s) and any challenges you may have faced, as well as what you'd do with more time. 

We understand that while this application is built using technologies we love at CDS.ai, they may be new to you! If wrapping your head around new-to-you technologies, languages and frameworks takes the bulk of your time and no tasks are completed, that's perfectly acceptable - just be prepared to talk about your experience. We also recognize that this exercise is new to us too - if you run into any technical hurdles, feel free to email alexharding@rti.org for any troubleshooting or questions.

For delivery, please choose one of the following options:
* Use the repository template feature to create your own version of this repository, and either provide us with a link if public or reach out to our HR contact for a list of usernames to grant access to if private
* Create an archive (zip, tarball) of your code and provide us with that via email or file share

---
## Tasks

What follows is a list of tasks you can perform in this repository. These are roughly separated into three buckets: frontend, backend, and full stack. 

### Frontend

* Bar Chart Changes:
  * The categories in the bar charts are not cased for display (`education_level` instead of `Education Level`). Add formatting for the category, both in the title of the visualization and the tooltip.
  * In the `education_level` bar chart, order the education levels.
  * Refactor the bar chart component to show percentages instead of counts.
    * As an optional addition, refactor this chart to be a stacked bar chart in which each bar shows the percentage of "true" and percentage of "false".
  * Make each bar in the chart have a different color.
  * Some visually impaired users use a screen reader and can't see the contents of our visualization. Add a table below the visualization with the contents of the visualization.
    * Optionally, add a button that toggles between the bar chart and the table instead of showing both.
* Data Filtering:
  * Add a filter that allows users to filter the dataset to only include rows where `sex` is equal to `Male`.
  * Add a filter that allows users to specify an age range to include on their charts.
* Advanced Charting:
  * Try refactoring this visualization to a different chart type, such as a pie chart or polar area chart.
    * Allow users to toggle between chart types.
  * Create a new visualization that shows the percentage of each education category that makes over 50k in a year. This can be grouped, stacked, or any visualization that you think expresses this information.
* State Management:
  * Refactor the application to use a [Pinia](https://pinia.vuejs.org/) store for the census data rather than passing the census data from the parent to the individual components.

### Backend

* Add a PostgreSQL database to this application. Load the CSV into the database, and have the FastAPI backend read from the database instead of the CSV file.
* Finish the `summary-stats` endpoint present in the backend. A set of visualizations already exists on the frontend, but does not become visible unless data is returned from the `summary-stats` API endpoint. 
  * To see the expected output, check out `summary_stats.json`
  * For `sex`, `race`, and `education_level`, check out pandas `groupby`
  * For "bonus points", try adding a list of outliers to the `age` dictionary
    * The box plot will still work without them
    * To calculate outliers
      * age < 1st quartile - (1.5 x interquartile range)
      * age > 3rd quartile + (1.5 x interquartile range)

### Full Stack

* Implement any of the "Filtering" tasks from the frontend section, but transmit the filter values to the backend and apply the filtering on the backend.
* Add authentication (a username/password) to this application. Here are some helpful documents:
  * [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
  * [Helpful article on JWT Auth in FastAPI](https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/)

---

## Developer Setup

This repository includes containerization using Docker. CDS.ai frequently uses Docker to containerize our applications so that they are more portable and infrastructure-agnostic. Using Docker to set up this application locally is fully optional, and may ease your speed of development as you don't have to install and debug environments for both Python and Javascript. If you would like to set up the Python and Javascript applications natively, see the "native" section below.

### Docker

Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

From the root directory of this repository, run `docker-compose up`. This will build the Docker images for the frontend and backend and run both containers.

Note that if you choose to use Docker for this application, you may need to rebuild images after adding dependencies to the frontend or backend during your exercise.

For the frontend, we are following a common docker-compose pattern in which we redirect `node_modules` to an empty volume. The reason for this is because `npm install` will often include OS-dependent binaries, so this allows the `node_module` folder to be separate for local and container development. If you wish to install dependencies into the frontend while using docker for development, you must do so *inside of the container*`. You can do so in either of the following ways:

```bash
docker exec -it cds.ai-fullstack-frontend sh ## opens an interactive terminal inside of the docker container

docker exec -it cds.ai-fullstack-frontend npm install --save library-name-here ## installs libraries
```

### Native

Alternatively, you can set up both the frontend and backend natively.

#### Backend (Python)

Install [Python 3.9 or later](https://www.python.org/downloads/). From the `backend` directory of this repository, use a Python dependency management strategy of your choosing and install the required packages with `pip install -r requirements.txt`. Then run `uvicorn main:app --reload` to run the development server.

#### Frontend (Javascript)

Install [Node.js 18 or later](https://nodejs.org/en/download). From the `frontend` directory of this repository, run `npm install` to install dependencies, and `npm run dev` to run the development server.

### Usage

Once installed and running, the backend will be available at `http://localhost:8000` and the frontend will be available at `http://localhost:5173`.
