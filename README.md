# 🚀 SimplifiIQ – AI Research Intern Assessment  
**Developed by:** Faizan Ur Rehman  

---

## 🧠 Overview  
This project was built as part of the **SimplifiIQ AI Research Intern Assessment**.  
It automates three main tasks:  
1. **Log Analysis** – calculates total time spent by each user and on each task type.  
2. **Web Automation & Summarization** – extracts website titles and meta descriptions, then generates AI-based summaries using **Google Gemini 2.5 Flash**.  
3. **Interactive Dashboard** – visualizes all results in a clean and modern HTML dashboard with charts and tables.

---

## ⚙️ How to Run  

### ▶️ Part A – Log Analysis  
Analyze log data from `logs_sample.csv` and generate summary CSVs.
```bash
python analyze_logs.py --input logs_sample.csv
```
**Outputs:**  
- `summary_time_per_user.csv`  
- `summary_time_per_task.csv`  
- `logs_processed.csv`  

---

### 🌐 Part B – Web Automation + Summarization  
Fetch titles and meta descriptions for given URLs and create AI summaries using the Gemini API.
```bash
python scrape_summarize.py --input urls.csv --output automation_output.csv --use-network
```
**Output:**  
- `automation_output.csv` containing AI-generated summaries.  

---

### 📊 Part C – Dashboard  
Visualize everything in a single place using `dashboard.html`.
```bash
start dashboard.html
```
**Features:**  
- Modern dark theme with glassmorphism design  
- Interactive progress chart using Chart.js  
- Tables showing both Part A & B results  
- Footer credits with AI attribution  

---

## 🖼️ Screenshots  

| Dashboard | Chart | Tasks |
|------------|--------|-------|
| ![Dashboard](assets/screenshots/Dashboard.png) | ![Chart](assets/screenshots/Chart.png) | ![Tasks](assets/screenshots/Tasks.png) |

| Task A | Task B |
|--------|--------|
| ![Task A](assets/screenshots/Task%20A.png) | ![Task B](assets/screenshots/Task%20B.png) |

---

## 🧩 Tech Stack  
| Category | Tools |
|-----------|-------|
| Language | Python 3.10 |
| Libraries | Pandas, Requests, BeautifulSoup4 |
| AI Model | Google Gemini 2.5 Flash |
| Visualization | HTML, CSS, Chart.js |
| Output | CSV & Dashboard |

---

## 💬 Reflection  
> This project helped me learn how to integrate APIs, process data efficiently, and design a simple yet elegant AI-driven dashboard.  
> It demonstrates practical automation combined with real-world AI implementation.

---

## 💎 Credits  
🚀 **Summarization powered by Google Gemini 2.5 Flash**  
💻 **Developed by Faizan Ur Rehman**  
🙏 *Thank you for reviewing my SimplifiIQ AI Research Intern Assessment.*
