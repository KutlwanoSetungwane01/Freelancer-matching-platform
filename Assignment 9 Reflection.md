# **Reflection: Designing the Domain Model and Class Diagram**

## 1. Challenges Faced in Designing the Domain Model and Class Diagram

Designing the domain model and class diagram for the Freelancer Job Matching Platform came with several challenges. One of the biggest difficulties was identifying the **right level of abstraction**. For example, deciding whether to separate user roles into different classes or represent them using a "role" attribute in a single `User` class took some time. I eventually chose the latter for simplicity and flexibility.

Another major challenge was modeling the **relationships** between entities. Understanding how a `JobPost`, `Proposal`, and `Contract` interact was tricky because they form a lifecycle: employers create job posts, freelancers submit proposals, and once a proposal is accepted, a contract is created. Capturing this flow accurately in the model while keeping it understandable was not easy. Additionally, representing **many-to-many** relationships (like users sending and receiving messages, or giving and receiving reviews) required careful planning to ensure the model remained normalized and logical.

When designing the class diagram in Mermaid.js, I had to learn and apply **correct UML syntax**, including multiplicities and relationship types like association and composition. This required multiple attempts and revisions. I also struggled with deciding which methods to include for each class. For instance, whether `submitProposal()` should belong to `User` or `Proposal` was a small but important design consideration.

## 2. Alignment with Previous Assignments

The class diagram and domain model align well with previous assignments. In earlier work, I identified the core user stories, use cases, and workflows such as posting a job, submitting proposals, messaging, and leaving reviews. The entities designed in the domain model directly reflect those actions.

In Assignment 6, I created user stories like "As a freelancer, I want to submit a proposal" and "As an employer, I want to hire a freelancer after reviewing proposals." These were helpful in identifying key classes like `User`, `JobPost`, `Proposal`, and `Contract`. The activity diagrams and state diagrams created in Assignment 8 also influenced the design, particularly in showing how `JobPost` moves from open to closed or how `Contract` moves from active to completed.

## 3. Trade-offs Made

Several trade-offs were made for the sake of simplicity and clarity. I avoided implementing complex inheritance structures, such as having separate `Freelancer` and `Employer` subclasses of `User`. While inheritance could offer more detailed behavior per role, I opted to use a "role" attribute in the `User` class to keep the model straightforward.

Another trade-off was grouping `skills` and `portfolio` under the `Profile` class rather than duplicating these fields in the `User` class. This approach supports better separation of concerns but adds an extra layer of navigation in the model. I also decided not to include advanced features like dispute handling or reporting users to avoid overcomplicating the diagram.

## 4. Lessons Learned

This task helped me understand the importance of **planning and iteration** in object-oriented design. Creating a domain model is not just about listing entities—it's about thinking deeply about how they interact in real-world workflows. I also realized that **simplifying complex systems** while keeping the design scalable is a key part of software engineering.

I learned how powerful Mermaid.js is for quickly visualizing relationships and how crucial it is to follow consistent naming and formatting. Overall, this step solidified my understanding of how domain models, class diagrams, and user requirements come together to form the foundation of a well-structured software system.
