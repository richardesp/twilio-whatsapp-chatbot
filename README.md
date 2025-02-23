# Twilio WhatsApp Chatbot

Twilio WhatsApp Chatbot is a FastAPI-based service designed to interact with users via WhatsApp using the Twilio API. This chatbot processes incoming WhatsApp messages, integrates with OpenAI for responses, and caches data using Redis.

## **Features**
- 📩 Receive and process WhatsApp messages via Twilio Webhooks.
- 🤖 Integrate OpenAI for message processing.
- 🐳 Containerized using **Docker & Docker Compose**.
- ✅ Code formatting and linting with **Black, Ruff, and MyPy**.
- 🔄 Pre-commit hooks to enforce coding standards.

---

## **Getting Started**

### **Prerequisites**
Ensure you have the following installed:
- [Python 3.12.1](https://www.python.org/)
- [Docker & Docker Compose](https://www.docker.com/)
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- A [Twilio account](https://www.twilio.com/) with WhatsApp API access.
- An [OpenAI API key](https://platform.openai.com/signup/).
- A running Redis instance.

---

## **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/richardesp/twilio-whatsapp-chatbot.git
cd twilio-whatsapp-chatbot
```

### **2. Set Up the Development Environment**
We use `uv` for dependency management.

#### **Install `uv` (if not installed)**
```bash
pip install uv
```

#### **Create and Activate a Virtual Environment**
```bash
uv venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows (PowerShell)
```

#### **Install Dependencies**
```bash
uv pip install -r requirements.dev.txt
```

---

## **Running the Application Locally**

### **Using `docker-compose.dev.yml`**
For development, the environment is configured using Docker Compose.

#### **Start the Development Environment**
```bash
make up-dev
```
or
```bash
docker-compose -f docker/docker-compose.dev.yml up -d --force-recreate
```

#### **Stop the Development Environment**
```bash
make down-dev
```
or
```bash
docker-compose -f docker/docker-compose.dev.yml down
```

#### **Rebuild Containers**
```bash
make build-dev
```

#### **View Logs**
```bash
make logs-dev
```

---

## **API Endpoints**

### **1. Process Incoming WhatsApp Messages**
**Endpoint:**  
```
POST /whatsapp
```

**Description:**  
Handles webhook events sent by WhatsApp and processes messages using Twilio, Redis, and OpenAI.

**Request Body (Form Data):**
```json
{
  "From": "whatsapp:+1234567890",
  "To": "whatsapp:+0987654321",
  "Body": "Hello, chatbot!",
  "MessageSid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

**Response Example:**
```json
{
  "message": "Response sent successfully"
}
```

**Dependencies Injected:**
- `TwilioClient`: Sends WhatsApp messages via Twilio.
- `RedisClient`: Caches processed messages.
- `OpenAIClient`: Generates AI-based responses.

**Error Handling:**
- `500 Internal Server Error` if message processing fails.

For testing, use [ngrok](https://ngrok.com/) to expose your local server:
```bash
ngrok http 8000
```
Then, configure Twilio's Webhook URL in the Twilio Console.

---

## **Environment Variables**
Create a `.env` file in the project root with the following variables:

```ini
# Ngrok Configuration
NGROK_AUTHTOKEN=your_ngrok_auth_token

# Twilio API Credentials
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_TEMPLATE_CONTENT_SID=your_twilio_template_content_sid

# Redis Configuration
REDIS_HOSTNAME=your_redis_host
REDIS_PORT=your_redis_port

# OpenAI API Key
OPENAI_APIKEY=your_openai_api_key
```

---

## **Development Workflow**
### **Code Formatting & Linting**
Before committing, ensure code follows project standards.

#### **Run Formatters & Linters**
```bash
black . && ruff . && mypy --ignore-missing-imports .
```

#### **Enable `pre-commit` Hooks**
```bash
pre-commit install
```

To manually run checks on all files:
```bash
pre-commit run --all-files
```

---

## **Deployment**
For production, use:

```bash
make up-prod
```
or
```bash
docker-compose -f docker/docker-compose.prod.yml up -d --force-recreate
```

To stop the production environment:
```bash
make down-prod
```

---

## **Contributing**
We welcome contributions! See the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Questions and Support**  
For any questions, open an issue or contact the maintainers:  
- GitHub: [@richardesp](https://github.com/richardesp)