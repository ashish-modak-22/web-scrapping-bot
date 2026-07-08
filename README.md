# 🤖 Smart Web Bot Assistant (Python Selenium Automation Project)

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![ChromeDriver](https://img.shields.io/badge/ChromeDriver-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-Automation-orange?style=for-the-badge&logo=python&logoColor=white)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge)](https://opensource.org/licenses/Apache-2.0)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-2ea44f?style=for-the-badge&logo=windowsterminal&logoColor=white)

A modular Python automation bot that scrapes **Jobs** and **Deals** using Selenium and stores structured data in JSON format. It demonstrates real-world web scraping, automation, filtering, and data pipeline design.

</div>

---

# ⚙️ How It Works (Workflow)

User runs `main.py`
        ↓
CLI Menu appears (Jobs / Deals)
        ↓
User selects option
        ↓
Selenium opens browser (headless or normal)
        ↓
Scraper extracts data from website
        ↓
Filters remove duplicates + unwanted data
        ↓
Data is saved into JSON files
        ↓
Results printed in terminal

```

# 📁 Project Structure

web_bot/
│
├── main.py                            # Main controller (menu system)
├── scrapers/
│   ├── job_scraper.py                 # Jobs scraping logic
│   └── deals_scraper.py               # Deals scraping logic
│
├── selenium_driver/
│   └── selenium_driver_Setup.py         # Selenium driver + headless config
│
├── utils/
│   ├── data_filter.py                   # Duplicate removal + keyword filtering
│   └── json_manager.py                 # JSON load/save/update system
│
├── data/
│   ├── jobs.json
│   └── deals.json

```

# 🚀 Features

- 💼 Job scraping automation
- 💰 Product/Deals scraping
- 🧠 Duplicate removal system
- 🔍 Keyword filtering system
- 📦 JSON-based storage
- 🤖 CLI menu-driven bot
- 🕶️ Headless browser support
- ⚡ Modular architecture

---

# 📥 Clone Project

```bash
git clone https://github.com/ashish-modak-22/web_scraping_bot.git
```

---

# 🛠️ Install Dependencies

```bash
pip install selenium webdriver-manager
```

---

# ▶️ Run Project

```bash
python main.py
```

---

# 🧠 Example Output

💼 Jobs:
{
  "title": "Python Developer",
  "company": "RemoteOK",
  "link": "https://..."
}

💰 Deals:
{
  "title": "HP Laptop 15s",
  "price": "52990",
  "link": "https://..."
}

---

# 🕶️ Headless Mode (Optional)

Run browser in background:

options.add_argument("--headless")

---

# 🔥 Future Improvements

- 📊 GUI dashboard
- ⏰ Auto scheduler (daily scraping)
- 🔔 Email alerts for deals
- 📈 Price history tracking
- 🌐 Multi-site expansion

---

# 👨‍💻 Author

Ashish Modak

Python automation + web scraping learning project using Selenium, filters, and JSON pipeline.

---

# Important Notice
During use of the bot, you can copy and paste any website URLs as per your choice and should check or visit the websites frequently to access the latest content selectors using CSS Seletor and XPATH since it changes time to time and some websites uses anti scraping system to prevent data scraping.

---

## **Important Modification: An explicit wait can be done for the webdriver as per certain conditions for a smooth scrapping**

---
