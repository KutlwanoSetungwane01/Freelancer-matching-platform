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
## Explanation

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

## 4. Create Contract Workflow
```mermaid
flowchart TD
    A(Start) --> B[Client selects proposal]
    B --> C[Click 'Create Contract']
    C --> D[Specify payment terms and deadlines]
    D --> E[Validate contract details]
    E --> F{Are details valid?}
    F -- No --> G[Show error]
    G --> D
    F -- Yes --> H[Generate contract]
    H --> I[Store contract]
    I --> J[Notify freelancer]
    J --> K(End)
``` 
## Explanation

This flow covers creating a contract between a client and freelancer. Validating terms ensures fairness and prevents errors. Notifying the freelancer helps initiate project work promptly, which supports system efficiency and agreement traceability.


## 5. Payment Processing Workflow
```mermaid
flowchart TD
    A(Start) --> B[Client initiates payment]
    B --> C[Enter payment details]
    C --> D[Validate details]
    D --> E{Is payment valid?}
    E -- No --> F[Show error]
    F --> C
    E -- Yes --> G[Process payment]
    G --> H[Update transaction records]
    H --> I[Notify both parties]
    I --> J(End)
```

## Explanation
This diagram models the payment workflow, focusing on accuracy, validation, and notifications. It aligns with the requirement for secure, traceable financial transactions. This also builds trust and supports real-time payment tracking.


## 6. Deliver Work Workflow
```mermaid
flowchart TD
    A(Start) --> B[Freelancer logs in]
    B --> C[Go to active contract]
    C --> D[Upload completed work]
    D --> E[Add message or comments]
    E --> F[Submit work]
    F --> G[Notify client]
    G --> H(End)
```
## Explanation
This diagram highlights how freelancers submit deliverables. Optional messaging fosters communication. Notifying the client ensures timely review, enhancing collaboration and meeting the platform’s delivery-tracking requirement.

---
## 7. Leave Review Workflow
```mermaid
flowchart TD
    A(Start) --> B[Job marked complete]
    B --> C[Client/Freelancer logs in]
    C --> D[Go to 'Leave Review']
    D --> E[Write rating and comment]
    E --> F[Submit review]
    F --> G[Validate and store review]
    G --> H[Update user profile]
    H --> I(End)
```
## Explanation
This activity covers the feedback loop, crucial for credibility and trust. Reviews are validated and stored, and profiles updated to reflect performance. This supports platform transparency and enhances decision-making for future collaborations.


## 8. Report Issue Workflow

```mermaid
flowchart TD
    A(Start) --> B[Login]
    B --> C[Go to "Report Issue"]
    C --> D[Select issue type]
    D --> E[Describe problem]
    E --> F[Attach evidence (optional)]
    F --> G[Submit report]
    G --> H[Store report and alert admin]
    H --> I(End)
```
## Explanation
This flow gives users a way to report problems. Attaching evidence helps the admin assess the issue quickly. It supports the system’s requirement for support and conflict resolution, ensuring user protection and platform integrity.


