# Day 04: Flask Web Application for Growth Analysis

This project is part of the Python course assignments. It takes the previous growth analysis logic from `day03` and wraps it in a simple **Flask web application** with a user-friendly web interface.

---

## What We Did:

1. **Integrated Previous Logic (`growth_anlysis.py`):**
   - Copied and adapted the core growth analysis script from `day03`.
   - Enhanced the logic to calculate not only the **average growth rate** but also the **Max Yield** (peak OD600 value).
   - Added automated growth curve plotting using `matplotlib`.

2. **Built a Flask Web App (`app.py`):**
   - Set up a local web server using Flask.
   - Created a route that handles file uploads (`.csv` files) securely and temporary storage.
   - Connected the backend calculation and plotting functions to the web interface.

3. **Created a Simple Web Interface (`templates/index.html`):**
   - Designed a clean HTML form allowing users to upload their growth data CSV file.
   - Added dynamic display sections to show the calculated results (Average Growth Rate and Max Yield).
   - Embedded the generated growth curve graph directly onto the results page.

---

## Project Structure

```text
day04/
│
├── app.py                  # Flask web application backend
├── growth_anlysis.py       # Core business logic (analysis & plotting)
├── templates/
│   └── index.html          # HTML web interface
└── static/                 # Generated static assets (growth curve images)