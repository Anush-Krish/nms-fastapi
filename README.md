#  nms-fastapi

A FastAPI-based nms send notification via **Email**, **SMS**, and **In-App**. It supports Kafka-based queuing and retry logic for reliable delivery.

---

##  Features

-  Send notifications (`POST /notifications`)
-  Fetch user notifications (`GET /users/{id}/notifications`)
-  Kafka integration for async processing
-  Retry logic for failed deliveries

---

##  Project Structure

nms-fastapi/
├── app/
│ ├── api/
│ │ └── endpoints/
│ │ └── notifications.py # API routes
│ │ └── users.py # API route
│ ├── core/
│ │ └── kafka_producer.py # Kafka producer setup
│ ├── models/
│ │ └── notification.py # Pydantic schemas
│ └── main.py # FastAPI app entrypoint
├── worker/
│ └── consumer.py # Kafka consumer service
├── requirements.txt
└── README.md

-----
## Todo

 Setup Db notifications
 Integrate Firebase for SMS/email delivery
