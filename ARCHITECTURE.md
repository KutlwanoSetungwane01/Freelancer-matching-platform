# Freelancer Job Matching Platform - Architecture

## 1. System Overview
This platform helps freelancers find jobs based on their skills and past projects.

## 2. C4 Model Diagrams
### Context Diagram (Level 1)
```mermaid
graph TD
    Freelancer -->|Search Jobs & Apply| Platform
    Client -->|Post Jobs & Hire| Platform
    Platform -->|Matches Jobs| Freelancer
    Platform -->|Processes Payments| PaymentGateway
    Admin -->|Manages System| Platform
