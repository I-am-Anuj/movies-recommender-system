# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python**, **Streamlit**, and the **TMDB API**. The system recommends the top 5 movies similar to a user's choice using cosine similarity and displays their posters fetched live via API.

---

## 🚀 Features
* **Content-Based Filtering:** Computes similarity between movies using vectorization and cosine similarity.
* **Live Posters:** Connects directly to TMDB (The Movie Database) API to display updated movie artwork.
* **Compressed Matrix:** Optimized data loading using `gzip` compression to maintain high performance with minimal storage overhead.
* **Clean UI:** Responsive layout with custom CSS styling and built-in retries for resilient network requests.

---

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Frontend/Framework:** Streamlit
* **Data Processing:** Pandas, NumPy, Scikit-learn
* **Serialization/Compression:** Pickle, Gzip
* **API Requests:** Requests (with HTTPAdapter retries)

---

## 💻 Local Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/I-am-Anuj/movies-recommender-system.git
cd movies-recommender-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 👨‍💻 Developed By
**Anuj** (NIT Raipur)  
* **GitHub:** [@I-am-Anuj](https://github.com/I-am-Anuj)
