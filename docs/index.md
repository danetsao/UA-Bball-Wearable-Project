# Project Goals

  &nbsp;&nbsp;&nbsp;&nbsp;The original goal of this project was to create software for a pair of smart glasses which could analyze live basketball film for team personnel, ball location, and posession identification, and use this data to select and popup relevant stats on the glasses' display. This would allow basketball coaching personnel to get access to live in-game statistics quicker, which would help with quicker decision making on the court. However, due to problems with the supplier of the smart glasses, we decided to pivot the project goal to focus on a web app leveraging the functionality described above. \
  &nbsp;&nbsp;&nbsp;&nbsp;Our new goal was twofold. The first part of the goal was to create a software tool which could use computer vision to analyze basketball film and annotate it with relevant statistics. The second, and arguably more important goal was to build the foundation for the original goal of the project while also creating a potentially helpful tool. We specifically chose the path that we did because it would allow for the vast majority of our work to be built upon in the future. The three specific sub-goals we focused on can be seen below:

  * **Create user-friendly software to automate the analysis of basketball film**
  * **Automate the retrieval of live and historical basketball statistics**
  * **Establish a solid foundation for the original project of wearable smart glasses despite the absence of hardware**


# Approach

[Approach](/docs/sprint.md)


# Tech Stack

| Tool       | Purpose     |
|------------|-------------|
| [Streamlit](https://streamlit.io/) | Build web app wrapper |
| [Roboflow](https://roboflow.com/)  | Create image dataset |
| [YOLOv8](https://ultralytics.com/yolov8) | Train and implement CV model |
| [OpenCV](https://opencv.org/)      | CV execution |
| [SQLite](https://sqlite.org/)      | Store roster info and stats |

[More on Tech](/docs/tech.md)


# Documentation

  &nbsp;&nbsp;&nbsp;&nbsp;For documentation on the work which we have completed, please see the github link below. Read the relevant README.md documents for each module, and view the commented code to see our implementation.
[Project GitHub](https://github.com/wriemer/UA-Bball-Wearable-Project)


# Project Video (Presentation + Demo)

[![](https://img.youtube.com/vi/OxT2fUXyXGc/0.jpg)](https://www.youtube.com/watch?v=OxT2fUXyXGc)


# Team Members

- Aidan Kaczor - ajkaczor@crimson.ua.edu
- Dane Tsao - dltsao@crimson.ua.edu
- Joseph Storie - jrstorie@crimson.ua.edu
- Logan Hay - ljhay@crimson.ua.edu
- Will Riemer - wjriemer@crimson.ua.edu
