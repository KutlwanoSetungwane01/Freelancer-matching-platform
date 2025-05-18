
# Freelancer-matching-platform
A platform that connects freelancers with job opportunities based on their skills and past projects.

##  Documentation (Assigment 3)
- [System Specification](SPECIFICATION.md)
- [Architecture Design](ARCHITECTURE.md)

## Learn more about this project (Assignment 4)

- [Stakeholder Analysis](STAKEHOLDER_ANALYSIS.md)
- [Functional Requirements](FUNCTIONAL_REQUIREMENTS.md)
- [Non-Functional Requirements](NON_FUNCTIONAL_REQUIREMENTS.md)
- [System Requirements](SYSTEM_REQUIREMENTS.md)
- [Reflection](REFLECTION.md)


## Use Case & Test Case Documentation (Assignment 5)

- [Use Case Diagram](Use_case_diagram.md)
- [Use Case Specifications](Use_case_specifications.md)
- [Test Cases](Test_cases.md)
- [Reflection](Reflection.md)

- ## Agile Planning Documentation (Assingment 6)

- [User Stories](User_stories.md)
- [Product Backlog](Product_backlog.md)
- [Sprint Plan](Sprint_plan.md)
- [Reflection](Reflection.md)


## GitHub Project Templates and Kanban Board Implementation (Assignment 7)
Kanban Board Customization
I customized the Kanban board to better fit the project's workflow:

‘Testing’ Column: Added to track tasks needing quality assurance (QA) testing, separating development from testing stages.

‘Blocked’ Column: Introduced to identify tasks delayed by external factors, helping the team spot bottlenecks.

Task Assignments and Labels: Tasks were categorized with labels like feature, bug, and enhancement for better organization.

Automation Features: The "Automated Kanban" template was used for automatic task movement, ensuring up-to-date task statuses.

- [Template analysis](kanban-explanation.md)
- [Reflection](kanban-reflection.md)

## Object State Modeling and Activity Workflow Modeling (Assignment 8)

In this assignment, I focused on modeling the dynamic behavior and workflows of the freelancer matching platform. The task involved creating State Transition Diagrams for key objects such as User Accounts and Projects to define their lifecycles, and Activity Diagrams to map out complex processes like user registration and project creation. These diagrams were designed to align with functional requirements and use cases to provide a clear understanding of the system's behavior. Additionally, I reflected on the challenges of designing the state transitions and workflows, balancing detail with clarity. 

- [User Account - Object State Diagram](Object_User%20Account.md)
- [Workflow Activity Diagram](Activity_Workflow.md)
- [Assignment 8 Reflection](Assignment%208_Reflection.md)

 ## Object-Oriented Design for a Freelancer Job Matching Platform (Assignment 9)
This assignment focuses on object-oriented design for the Freelancer Job Matching Platform. It includes a domain model outlining system objects and their relationships, a UML class diagram created with Mermaid.js, and a reflection discussing design challenges, choices, and how the system aligns with previous work like user stories and state diagrams.

- [Domain Model](domain_model.md)
- [Class Diagram](class_diagram.md)
- [Assignment 9 Reflection](Assignment%209%20Reflection.md)


##  Assignment 10

This assignment includes class implementations and all six major creational design patterns for the Freelancer Job Matching Platform.

### Quick Links
- [Source Code (Core Classes)](Assignment_10/src)
- [Reflection (Assignment 10)](Reflection-assignment%2010.md)

##  Assignment 11 – Repository Pattern Implementation

### Key Files and Folders

- [Repository Interfaces](Assignment_11/repositories) – Generic and entity-specific interfaces
- [In-Memory Repositories](Assignment_11/repositories/inmemory) – HashMap-based implementations
- [Factory Class](Assignment_11/factories/RepositoryFactory.py) – Storage abstraction using the Factory Pattern
- [Class Diagram](Assignment_11/class_diagram.md) – Updated UML diagram with repository relationships
- [Reflection](Assignment_11/Reflection.md) – Personal reflection on the assignment, challenges, and learnings


# Assignment 12 – Service Layer and REST API

## Link to the assignemt

-[Assignment 12](./Assignment_12)

## ⚠️ Notes

Due to persistent errors in GitHub Codespaces, the app could not be successfully run using FastAPI and Uvicorn. As a result, Swagger documentation and API testing could not be completed in the browser. However, the code structure follows all assignment requirements.

## Assignment 13: CI/CD Setup and Branch Protection
Objective:
The goal of this task was to implement continuous integration and continuous deployment (CI/CD) using GitHub Actions. I was also required to enable branch protection rules to ensure code quality and prevent unreviewed changes from being merged into the main branch.

## Actions Taken
Created a new branch called KutlwanoSetungwane01-patch-1 and pushed the changes for Assignment 13 to this branch.

Created a CI/CD workflow file named .github/workflows/ci.yml. This file includes:

- A test job that automatically runs unit tests whenever code is pushed or a pull request is created.

- A release job that builds and uploads a release artifact if tests pass and the code is pushed to the main branch.
  

Created a pull request from KutlwanoSetungwane01-patch-1 to main to integrate the changes.

Enabled branch protection rules on the main branch, which:

- Require at least one approved review before merging.

- Block merging if tests do not pass or reviews are missing.

## Challenges
Since I am the only contributor with write access to the repository, GitHub blocks me from approving my own pull request. As a result:

- The pull request remains open with the status: "Review required. Merging is blocked."

- This is expected behavior due to the branch protection settings.

## Evidence of Completion
Despite the merge being blocked, the following requirements were completed:

- The ci.yml file is present in the correct folder structure (.github/workflows/).

- The GitHub Actions workflow was triggered by the pull request and/or code push.

- The CI/CD logic was tested, and I was able to confirm it attempts to run on new pushes.
  

Screenshots were taken showing:

- The pull request.

- The contents of ci.yml.
  ## 📸 Assignment 13 Screenshots

## 📸 Assignment 13 Screenshots

### ✅ Branch Protection Rules
![Branch Protection](https://github.com/KutlwanoSetungwane01/Freelancer-matching-platform/blob/KutlwanoSetungwane01-patch-2/Screenshot%20(1).png?raw=true)


### ✅ Pull Request Blocked by Failing Test
![Failing Test PR](https://github.com/KutlwanoSetungwane01/Freelancer-matching-platform/blob/KutlwanoSetungwane01-patch-2/Screenshot%20(2).png?raw=true)


The workflow execution status in the Actions tab.

## Notes
Due to repository restrictions, the final merge was not possible without collaboration or instructor override. However, all technical CI/CD requirements were implemented and verified.

## Assignment 14 Documentation

## Assignment 14 Documentation

Please note that my Assignment 14 documents (including Readme, CONTRIBUTING.md, ROADMAP.md, REFLECTION.md, and VOTING_RESULTS.md) are located on the branch named KutlwanoSetungwane01-patch-4 and not on the main branch.

This is due to branch protection rules and merge errors I encountered while attempting to merge into main. Despite multiple attempts, the pull request could not be approved because it requires a CI check or reviewer approval, which I couldn't complete.

All required files are correctly uploaded and can be reviewed on the KutlwanoSetungwane01-patch-4 branch under the folder assignment14-docs.

















