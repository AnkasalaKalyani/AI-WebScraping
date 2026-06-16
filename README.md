# 📦 AI Amazon Competitor Analysis

An AI-powered competitor intelligence platform that helps users analyze Amazon products and their competitors using real-time web scraping and GPT-4.

The application allows users to enter an Amazon ASIN and automatically retrieve product information, identify competing products, and generate actionable market insights through AI.

---

## 🚀 Features

### Product Intelligence
- Scrape Amazon product details using an ASIN.
- Support multiple Amazon marketplaces:
  - Amazon US (`.com`)
  - Amazon Canada (`.ca`)
  - Amazon UK (`.co.uk`)
  - Amazon Germany (`.de`)
  - Amazon France (`.fr`)
  - Amazon Italy (`.it`)
  - Amazon UAE (`.ae`)
- Support geo-location based scraping using ZIP/postal codes.
- Display:
  - Product title
  - Brand
  - Price
  - Currency
  - Ratings
  - Images
  - Categories
  - Buy Box information

---

## 🔍 Competitor Discovery

The system automatically identifies competing products by using multiple Amazon search strategies:

- Featured products
- Lowest-priced products
- Highest-priced products
- Highest-rated products

The application then:

- Extracts competitor ASINs
- Removes duplicates
- Filters invalid results
- Retrieves detailed competitor information

---

## 🤖 AI Competitor Analysis

Using GPT-4 and LangChain, the application generates:

- Executive summaries
- Product positioning analysis
- Top competitor insights
- Pricing comparisons
- Strategic recommendations
- Market opportunities

The output is structured and easy to understand for business users.

---

## 🏗️ Architecture

```text
                ┌───────────────────┐
                │   Streamlit UI    │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │  Service Layer    │
                └──────┬─────┬──────┘
                       │     │
         ┌─────────────┘     └──────────────┐
         ▼                                  ▼
┌─────────────────┐              ┌─────────────────┐
│  Oxylabs API    │              │     TinyDB      │
│ Amazon Scraping │              │ Local Storage   │
└────────┬────────┘              └────────┬────────┘
         │                                 │
         ▼                                 ▼
  Amazon Product Data             Product Repository
                 │
                 ▼
        ┌────────────────┐
        │ GPT-4 +        │
        │ LangChain      │
        └──────┬─────────┘
               ▼
      Competitor Insights
```

---

## 🛠️ Technologies Used

### Frontend
- Streamlit

### Backend
- Python

### Web Scraping
- Oxylabs Realtime API

### AI & LLM
- OpenAI GPT-4
- LangChain
- Pydantic

### Database
- TinyDB

### Environment Management
- python-dotenv

---

## 📂 Project Structure

```text
AI-WebScrapping/
│
├── main.py
├── data.json
├── pyproject.toml
├── README.md
├── .gitignore
│
└── src/
    ├── __init__.py
    ├── db.py
    ├── llm.py
    ├── oxylabs_client.py
    └── services.py
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <repository-url>
cd AI-WebScrapping
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key

OXYLABS_USERNAME=your_oxylabs_username
OXYLABS_PASSWORD=your_oxylabs_password
```

> Do not commit the `.env` file to GitHub.

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

The application will open in your browser.

---

## 📖 How to Use

### Step 1: Scrape Product Information

Enter:

- Amazon ASIN
- ZIP/Postal Code
- Amazon Marketplace

Click:

```text
Scrape Product
```

The application retrieves and stores the product details.

---

### Step 2: Analyze Competitors

Click:

```text
Start Analyzing Competitors
```

The system will:

- Search for competitors
- Collect competitor ASINs
- Retrieve detailed competitor data
- Store the results

---

### Step 3: Generate AI Insights

Click:

```text
Analyze with LLM
```

GPT-4 generates:

- Summary
- Positioning analysis
- Top competitor insights
- Recommendations

---

## 💡 Example Use Cases

This application can help:

### Amazon Sellers
- Understand their competitive landscape.
- Optimize pricing strategies.
- Identify product differentiation opportunities.

### Market Researchers
- Analyze competing products quickly.
- Generate AI-powered insights.

### E-commerce Teams
- Monitor competitor positioning.
- Support strategic decision-making.

---

## 🔮 Future Enhancements

- Export reports to PDF and Excel.
- Historical price tracking.
- Competitor trend dashboards.
- Review sentiment analysis.
- PostgreSQL integration.
- Cloud deployment using AWS or Streamlit Cloud.

---

## 👩‍💻 Author
Kalyani Ankasala

Developed as an AI-powered competitor intelligence project combining web scraping, local data persistence, and large language models to automate Amazon market analysis.
