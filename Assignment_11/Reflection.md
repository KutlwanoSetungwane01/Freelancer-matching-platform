# **Reflection – Assignment 11: Repository Pattern Implementation**

This assignment was honestly very challenging for me. When I first read about the repository pattern, I struggled to fully understand how all the pieces fit together — the interfaces, in-memory implementations, factories, and future storage options. It felt overwhelming at times because it wasn’t just about coding; it was about designing a system properly, and that was something very new to me.

At first, creating the generic Repository interface was confusing. I had a hard time wrapping my head around why we need a base structure when I could just create simple classes. But after going through examples and asking for help, I slowly realized that using a base repository avoids repeating code, and it makes the system easier to manage if changes happen later.

The in-memory implementations were another difficult part. Even though the logic was almost the same for each entity, I kept feeling unsure if I was doing it right, especially when handling IDs and matching the relationships. Copying and adapting the structure for every object like User, JobPost, Proposal, and others felt tiring and repetitive, but at the same time, I started seeing a pattern, and that made it a little easier.

Adding the Factory Pattern for the storage was interesting but still not easy. It took me a while to understand that the factory would help switch between in-memory storage and future databases without changing my core logic. Once I understood that, it made a lot of sense why bigger systems use these kinds of patterns.

Creating the stub for the database repository reminded me that software projects are never really "finished" — they are designed to grow and adapt. Even though I didn’t build the full database part yet, preparing for it showed me the importance of thinking ahead when designing systems.

Overall, this assignment was tough. There were a lot of new concepts, and I felt stuck many times. But even though it wasn’t perfect, I really tried my best to follow the instructions, understand the repository pattern, and complete all the required parts. I learned that in real software engineering, organizing the system properly is just as important as writing code that works. I still have a lot to learn, but I’m proud that I managed to push through and finish the assignment despite the challenges.
