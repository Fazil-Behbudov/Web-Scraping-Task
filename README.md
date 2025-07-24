
# 📰 Web Scraping Task – xeberler.az

Welcome to the **Web Scraping Task** project, where we extract real-time news data from [xeberler.az](https://xeberler.az). This script collects detailed article information and compiles it into a structured CSV dataset.

---

## 📊 Project Summary

This project automates the collection of news content from the Azerbaijani news portal **xeberler.az**. The script parses headlines, links, images, categories, publication times, and full article content across multiple pages.

### ✅ Key Features

- Scrapes **40 pages** of news articles
- Extracts:
  - 🗞️ Title (`Başlıq`)
  - 🔗 Link
  - 🖼️ Image URL (`Foto url`)
  - 📆 Date (`Tarix`) and 🕒 Time (`Saat`)
  - 🏷️ Category (`Kateqoriya`)
  - 📄 Full Text (`Xəbər`)
  - 🕓 Scrap Timestamp (`Scrap tarixi`)
- Saves the data to: `Xəbərlər_az.csv`

---

## 🧪 Technologies Used

- **Python 3**
- [Requests](https://pypi.org/project/requests/) – HTTP requests
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) – HTML parsing
- [pandas](https://pypi.org/project/pandas/) – Dataframe & CSV export
- [lxml](https://pypi.org/project/lxml/) – Fast HTML parsing

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Fazil-Behbudov/Web-Scraping-Task.git
cd Web-Scraping-Task
```

### 2️⃣ Install Dependencies

Install required Python packages using pip:

```bash
pip install -r requirements.txt
```

> Or manually:
```bash
pip install requests beautifulsoup4 pandas lxml
```

### 3️⃣ Run the Script

```bash
python scraper.py
```

This will create a file called `Xəbərlər_az.csv` containing the scraped data.

---

## 🗂️ Project Structure

```
📦 Web-Scraping-Task/
├── scraper.py           # Python script for scraping
├── requirements.txt     # Required Python packages
├── Xəbərlər_az.csv      # Output dataset (generated)
└── README.md            # Project documentation
```

---

## 📌 Example Output

| Başlıq | Link | Tarix | Saat | Kateqoriya |
|--------|------|-------|------|-------------|
| Prezident çıxış etdi | https://... | 24.07.2025 | 15:30 | Siyasət |

---

## 📄 License

This project is provided for **educational and non-commercial use**. Please respect [xeberler.az](https://xeberler.az)'s content usage terms.

---

## 🙋‍♂️ Author

Developed with 💻 by **Fazil Behbudov**  
[GitHub Profile →](https://github.com/Fazil-Behbudov)

---

Feel free to fork ⭐ the repo or open an issue if you have questions!
