## Reflection 
This assignment focused on applying the repository pattern to the Freelancer Job Matching Platform I’ve been working on. At first, I found it a bit confusing, especially understanding how interfaces and in-memory storage fit together. However, breaking the work down step by step made it more manageable.

Creating the generic Repository interface helped me realize how much code can be reused. It was useful to learn that I don’t have to write the same CRUD methods again for each entity — I could just extend the base interface. It also helped me understand how abstraction works in real software systems.

The most challenging part for me was writing the in-memory repository implementations. Even though the logic was similar, I had to stay focused and make sure I used the correct IDs and attributes for each entity. Once I got the pattern right, the rest of the repositories were easier to build.

I chose to use the Factory Pattern for the abstraction mechanism because it made sense to create a central place that returns the correct storage backend. I liked that I could just switch the storage type later without changing all the code. The Factory also made me see how design patterns are useful in planning for future changes.

For future-proofing, I added a stub for a database repository. This made me realize how important it is to write code that can evolve. Even though I didn’t fully implement the database version, just preparing for it made my system more flexible.

Adding a class diagram that showed the relationship between the interface, in-memory, and database repositories helped me visualize what I built. It was a useful way to connect theory with actual code.

Overall, this assignment taught me how to organize data access logic better, and how the repository pattern separates storage from business logic. I also learned that abstraction, flexibility, and planning ahead are important in software design. I’m still learning, but I feel like I’m starting to understand how professional systems are built.
