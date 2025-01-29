# Farm Tech

Farm Tech is an innovative online platform that aims to revolutionize the Canadian agricultural sector by optimizing land usage, fostering collaborations between landowners and farmers, and implementing digital storage solutions to reduce food waste.

## Overview

The project addresses two major challenges in Canadian agriculture: the underutilization of agricultural land and the prevalent issue of food wastage due to inadequate storage facilities. Farm Tech provides a comprehensive solution by:

1. **Land-Farmer Collaboration Platform**: This platform facilitates partnerships between landowners and farmers, enabling landowners to list their underutilized land and allowing farmers to explore and secure land for cultivation.

2. **Digital Storage Solution**: Farm Tech offers secure, temperature-regulated storage facilities tailored to meet the specific needs of different crop types. This feature helps farmers preserve their harvests, extend shelf life, and maximize market value.

3. **Crop Recommendation System**: Powered by a Random Forest algorithm, the platform provides personalized crop recommendations to farmers based on environmental factors, regional characteristics, and soil data. This data-driven approach aims to enhance agricultural productivity and profitability.

## Features

- **Land Listing and Exploration**: Landowners can list their land with comprehensive details, while farmers can search and find suitable parcels for cultivation.
- **Secure Land Agreements**: The platform facilitates clear communication and negotiation between landowners and farmers, enabling them to reach mutually beneficial agreements.
- **Crop Storage Solutions**: Farmers can access an array of secure, temperature-regulated facilities tailored to their specific crop types, ensuring optimal preservation and extended shelf life.
- **Crop Recommendation System**: By leveraging the Random Forest algorithm and analyzing datasets on temperature, humidity, rainfall, soil type, and regional demographics, the platform provides personalized crop recommendations to farmers.

## Repositories

- **Frontend**: https://github.com/HaRsH8747/farm-tech-frontend
- **Backend**: https://github.com/HaRsH8747/farm_tech_backend

## Technologies Used

- **Backend**: Django, Django Rest Framework, PostgreSQL
- **Frontend**: React
- **Machine Learning**: scikit-learn (RandomForest algorithm)

## Installation and Usage

1. Clone the repositories:
   - Frontend: `git clone https://github.com/HaRsH8747/farm-tech-frontend.git`
   - Backend: `git clone https://github.com/HaRsH8747/farm_tech_backend.git`
2. Install the required dependencies for each project (frontend and backend)
3. Set up the database for the backend:
4. Start the development servers:
- Backend:
  ```
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py migrate --run-syncdb
  python manage.py createsuperuser
  python manage.py runserver
  ```
- Frontend (replace `npm` with `yarn` if using Yarn):
  ```
  cd farm-tech-frontend
  npm install
  npm start
  ```
5. Access the application at the appropriate URL (e.g., `http://localhost:3000` for the frontend)

Detailed installation and usage instructions can be found in the respective repository README files.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [React](https://reactjs.org/)
- [scikit-learn](https://scikit-learn.org/)

## Contact

For any inquiries or support, please contact the project team at [contact@farmtech.ca](mailto:contact@farmtech.ca).
