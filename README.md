# Personalized Learning Recommendation Dashboard

An intelligent learning analytics and recommendation platform designed to understand a learner's performance, identify strengths and weaknesses, track learning progress, and provide personalized recommendations for the next learning step.

The system follows an adaptive learning cycle:

**Learn → Practice → Assess → Analyze → Recommend → Improve**

## 📌 Project Overview

Traditional learning platforms generally provide the same content to every learner. However, different learners have different knowledge levels, learning speeds, weak areas, and study patterns.

The **Personalized Learning Recommendation Dashboard** aims to solve this problem by collecting learning activity and assessment data, analyzing learner performance, and generating personalized learning insights and recommendations.

The project combines:

* Learning activity tracking
* Assessment and performance analysis
* Learner profiling
* Strength and weakness identification
* Personalized learning recommendations
* Progress visualization
* Data-driven learning insights

## 🎯 Objectives

* Track learner learning sessions and activities.
* Store assessment scores, attempts, and performance history.
* Identify topics where the learner performs well or struggles.
* Analyze learning behavior and progress over time.
* Recommend suitable topics and learning resources.
* Build a foundation for future machine learning-based personalization.
* Provide an interactive dashboard for monitoring learning progress.

## ✨ Planned Features

### 1. Learner Profile Management

* Create and manage learner profiles.
* Store basic learning-related information.
* Maintain individual learning history.

### 2. Learning Activity Tracking

Record details such as:

* Topic studied
* Study duration
* Number of attempts
* Questions attempted
* Difficulty level
* Learning timestamp
* Session information

### 3. Assessment Tracking

Store and analyze:

* Quiz scores
* Assessment results
* Correct and incorrect answers
* Number of attempts
* Topic-wise performance

### 4. Performance Analytics

Analyze learner data to identify:

* Strong topics
* Weak topics
* Frequently attempted topics
* Improvement trends
* Learning consistency
* Performance over time

### 5. Personalized Recommendations

The system will recommend:

* Topics requiring revision
* Next topics to study
* Practice questions
* Learning resources
* Suitable difficulty levels

Recommendations will be based on learner performance and learning behavior rather than generic suggestions.

### 6. Interactive Dashboard

The dashboard will display:

* Overall learning progress
* Topic-wise scores
* Strengths and weaknesses
* Assessment history
* Study activity
* Personalized recommendations

## 🏗️ System Architecture

```text
Learner
   │
   ▼
Learning Activities / Assessments
   │
   ▼
PostgreSQL Database
   │
   ▼
Data Processing & Analytics
   │
   ▼
Learner Performance Profile
   │
   ▼
Recommendation Engine
   │
   ▼
Personalized Learning Dashboard
```

## 🗄️ Database Design

The project uses PostgreSQL for structured storage of learner and learning-related data.

### Main Tables

* `users`
  Stores learner information.

* `topics`
  Stores learning topics and topic details.

* `learning_sessions`
  Stores individual study sessions.

* `assessments`
  Stores assessment and quiz performance.

* `learning_events`
  Stores detailed learner activity events for analytics and future machine learning.

The database is designed to support future analytics and recommendation models.

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL
* pgAdmin 4

### Data Processing & Analytics

* Pandas
* NumPy
* Scikit-learn

### Dashboard

* Streamlit

### Development Tools

* Git
* GitHub
* VS Code

## 📂 Project Structure

```text
Personalized-Learning-Recommendation-Dashboard/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   └── routes/
│
├── analytics/
│   └── analysis.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   └── schema.sql
│
├── requirements.txt
├── .gitignore
└── README.md
```

*Project structure may evolve as additional modules are implemented.*

## 🚀 Current Development Status

### Completed / Initial Setup

* Project repository initialized.
* PostgreSQL database configured.
* Database schema designed.
* Core learning-related tables created.
* Foreign-key relationships planned.
* Database connectivity testing initiated.

### Currently Building

* Backend database integration
* SQLAlchemy models
* APIs for learner and learning activity data
* Learning session and assessment storage

### Future Development

* Performance analytics
* Learner profiling
* Recommendation engine
* Interactive dashboard
* Machine learning-based personalization
* Recommendation effectiveness tracking

## 🔮 Future Enhancements

* Topic clustering using machine learning.
* Content-based recommendation using semantic similarity.
* Difficulty-aware recommendations.
* Predictive learner performance analysis.
* Knowledge-gap detection.
* Recommendation effectiveness evaluation.
* Adaptive learning paths.
* Explainable recommendations.

## 💡 Expected Impact

The platform aims to help learners understand **what they know, what they need to improve, and what they should learn next**, while providing educators or mentors with meaningful insights into learner progress.

## 👩‍💻 Author

**Garima Chauhan**

Developed as a personal AI/ML and learning analytics project.

## 📄 License

This project is intended for educational and development purposes.
