# 🏨 Hotel Booking Agent System using CrewAI

An intelligent multi-agent hotel booking assistant built with **CrewAI** and powered by **NVIDIA NIM LLMs**. The system demonstrates how multiple AI agents can collaborate to understand customer requirements, search for suitable hotels, and generate a professional booking summary.

---

## 📌 Project Overview

This project simulates a hotel booking workflow using CrewAI's multi-agent architecture. Instead of relying on a single AI assistant, specialized agents collaborate to perform different responsibilities throughout the booking process.

The project is designed as a demonstration of:

- Multi-Agent AI Systems
- CrewAI Framework
- NVIDIA NIM Large Language Models
- Sequential Task Orchestration
- Context Sharing Between Agents

---

## 🚀 Features

- 🤖 Multi-agent collaboration
- 🏨 Hotel recommendation workflow
- 💬 Customer requirement analysis
- 📋 Booking summary generation
- 🧠 Agent memory support (optional)
- 🔄 Sequential task execution
- ⚡ NVIDIA NIM integration
- 📦 Easily extensible with APIs

---

# 🏗 Project Architecture

```
                User
                  │
                  ▼
      Travel Consultant Agent
                  │
                  ▼
    Hotel Search Specialist Agent
                  │
                  ▼
      Booking Assistant Agent
                  │
                  ▼
          Final Booking Summary
```

---

# 🤖 Agents

## 1. Travel Consultant

### Responsibilities

- Collect customer travel requirements
- Understand destination
- Gather travel dates
- Identify customer budget
- Record preferred hotel type
- Capture special requests

---

## 2. Hotel Search Specialist

### Responsibilities

- Analyze customer preferences
- Compare available hotels
- Recommend the best hotel options
- Consider

- Budget
- Amenities
- Location
- Ratings
- Availability

---

## 3. Booking Assistant

### Responsibilities

- Review selected hotel
- Verify reservation details
- Generate booking confirmation
- Prepare booking summary

---

# 📋 Workflow

```
Customer Request
        │
        ▼
Travel Consultant
        │
Collect Preferences
        │
        ▼
Hotel Search Specialist
        │
Compare Hotels
        │
        ▼
Booking Assistant
        │
Generate Confirmation
        │
        ▼
Final Response
```

---

# 🛠 Tech Stack

- Python
- CrewAI
- NVIDIA NIM
- LiteLLM
- UV
- JSONC
- dotenv

---

# 📂 Project Structure

```
project_crewai/
│
├── agents/
│   ├── travel_consultant.jsonc
│   ├── hotel_search_specialist.jsonc
│   └── booking_assistant.jsonc
│
├── knowledge/
│   └── user_preference.txt
│
├── tools/
│
├── skills/
│
├── crew.jsonc
├── .env
├── pyproject.toml
├── README.md
└── .gitignore
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/project_crewai.git
```

Move into the project

```bash
cd project_crewai
```

Create a virtual environment

```bash
conda create -n crewai python=3.11
conda activate crewai
```

Install dependencies

```bash
crewai install
```

or

```bash
uv sync
```

---

# 🔑 Environment Variables

Create a `.env` file.

Example

```env
NVIDIA_API_KEY=your_nvidia_api_key
```

If using OpenAI-compatible endpoints

```env
OPENAI_API_KEY=your_nvidia_api_key
OPENAI_BASE_URL=https://integrate.api.nvidia.com/v1
```

---

# ▶ Running the Project

```bash
crewai run
```

---

# 📈 Example Workflow

### User Input

```
Destination:
Kathmandu

Check-in:
2026-02-15

Check-out:
2026-02-18

Guests:
2 Adults

Budget:
$120 per night

Amenities:
WiFi
Breakfast
Swimming Pool
```

### AI Output

```
Recommended Hotel:
Hotel Himalaya

Rating:
4.7 ⭐

Price:
$108/night

Amenities

✔ Free WiFi
✔ Swimming Pool
✔ Breakfast Included
✔ Airport Shuttle

Estimated Total

$324
```

---

# 🌟 Future Improvements

- Booking.com API Integration
- Amadeus Hotel Search API
- Google Maps Integration
- Hotel Availability Search
- Live Pricing
- Payment Gateway
- PDF Booking Confirmation
- Streamlit Frontend
- RAG Knowledge Base
- Voice Assistant
- Docker Deployment

---

# 📚 Learning Objectives

This project demonstrates:

- Multi-Agent AI Systems
- Agent Collaboration
- Context Passing
- Sequential Workflows
- CrewAI Configuration
- LLM Integration
- NVIDIA AI APIs

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Submit a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Suraj Sah Kanu**

Machine Learning Engineer | AI Research Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

Email: surajsah132@gmail.com

---

⭐ If you found this project useful, consider giving it a star on GitHub.