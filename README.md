# AI News Headline Generator

An AI-powered system that analyzes news articles and automatically generates engaging, SEO-friendly headlines using **Large Language Models (LLMs)** and **LangChain**.

The system reads a news article, generates multiple headline styles, ranks them based on clarity and engagement, and selects the best headline.

---

## Project Overview

News platforms rely heavily on compelling headlines to attract readers. This project demonstrates how **Generative AI** can assist journalists and content creators by automatically producing engaging headlines.

The AI system:

* Reads a news article
* Generates multiple headline variations
* Evaluates headline quality
* Selects the most impactful headline

---

## Features

* Generate **5 different headline styles**
* Breaking News headline
* SEO optimized headline
* Social media friendly headline
* Short headline
* Creative headline
* Automatic headline **ranking**
* Best headline selection
* Optional **Streamlit web interface**

---

## Technologies Used

* **Python**
* **LangChain**
* **Large Language Models (LLMs)**
* **OpenAI API / HuggingFace Models**
* **Streamlit** (for UI)

---

## Project Structure

```
ai-news-headline-generator
│
├── app.py
├── streamlit_app.py
├── headline_generator.py
├── headline_ranker.py
├── prompts.py
├── config.py
├── requirements.txt
├── README.md
│
└── data
      └── sample_article.txt
```

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/ai-news-headline-generator.git
```

Navigate to the project folder

```
cd ai-news-headline-generator
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

### Run Python Version

```
python app.py
```

This will generate headlines directly in the terminal.

---

### Run Streamlit Web App

```
python -m streamlit run streamlit_app.py
```

Then open:

```
http://localhost:8501
```

---

## Example Input

```
NASA successfully launched a new satellite designed to monitor climate change 
and provide real-time environmental data to scientists worldwide.
```

---

## Example Output

Generated Headlines

* NASA Launches Advanced Climate Monitoring Satellite
* New NASA Satellite to Track Climate Change in Real Time
* NASA’s New Satellite Could Transform Climate Science
* NASA Launches Climate Tracker
* Eyes in the Sky: NASA Sends Climate Watch Satellite into Orbit

Best Headline

New NASA Satellite to Track Climate Change in Real Time

---

## Prompt Design

The prompt instructs the LLM to behave as a **professional news editor** and generate five types of headlines:

1. Breaking News headline
2. SEO headline
3. Social Media headline
4. Short headline
5. Creative headline

This ensures variety, engagement, and readability.

---

## Headline Ranking Logic

The system evaluates headlines based on:

* Keyword relevance
* Clarity
* Ideal headline length
* Engagement potential

Each headline receives a score and the highest scoring headline is selected.

---

## Future Improvements

* Automatic news scraping from websites
* LLM-based headline quality evaluation
* Clickbait detection
* SEO keyword analysis
* Multi-language headline generation

---

## Author

**T Mohammed Sinan**

AI / Data Science Enthusiast
Machine Learning & Generative AI Projects

---

## License

This project is for educational and research purposes.
