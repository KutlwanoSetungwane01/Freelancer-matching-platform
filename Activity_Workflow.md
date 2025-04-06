## 1. User Registration - Activity Diagram
```mermaid
flowchart TD
    A[Start] --> B[User enters details]
    B --> C{Is email valid?}
    C -->|Yes| D[Send verification email]
    C -->|No| E[Show error message]
    D --> F[User verifies email]
    F --> G{Is verification successful?}
    G -->|Yes| H[Create user account]
    G -->|No| I[Show error message]
    H --> J[Account created successfully]
    I --> J
    E --> J
    J[End]
```
## User Registration - Activity Diagram Explanation

This workflow shows the full process a user follows when registering. It includes validation, email verification, and account activation. Ensuring only verified users become active aligns with system security and integrity requirements, and supports the functional requirement for account creation.

---
## 2. Post Job Workflow
``` mermaid
flowchart TD
    A(Start) --> B[Login as Client]
    B --> C[Click 'Post Job']
    C --> D[Enter job details]
    D --> E[Validate job details]
    E --> F{Are details valid?}
    F -- No --> G[Show error]
    G --> D
    F -- Yes --> H[Submit job]
    H --> I[Store job in database]
    I --> J[Notify freelancers]
    J --> K(End)

```
## Explanation
This diagram outlines how clients post jobs. Validation ensures complete and correct job listings. Freelancers are notified, supporting the platform’s goal of quick and relevant job exposure. This ties into requirements for job posting and system notification functionalities.

---
## 3. Submit Proposal Workflow

```mermaid
flowchart TD
    A(Start) --> B[Login as Freelancer]
    B --> C[Browse job listings]
    C --> D[Select job]
    D --> E[Write proposal]
    E --> F[Attach resume or portfolio]
    F --> G[Validate proposal]
    G --> H{Is proposal valid?}
    H -- No --> I[Show error]
    I --> E
    H -- Yes --> J[Submit proposal]
    J --> K[Store proposal in database]
    K --> L[Notify client]
    L --> M(End)
```
## Explanation 
This workflow helps freelancers apply for jobs. Validation prevents incomplete submissions. Notifying clients ensures fast proposal review, supporting agile response times and enhancing platform usability and responsiveness.


