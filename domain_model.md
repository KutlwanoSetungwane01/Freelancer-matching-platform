### Domain Model: Freelancer Job Matching Platform

| **Entity**    | **Attributes**                                                      | **Relationships**                                                         |
|---------------|---------------------------------------------------------------------|---------------------------------------------------------------------------|
| **User**      | userId, name, email, role (freelancer/employer)                    | Creates Profile, Posts JobPosts, Sends Messages, Gives/Receives Reviews  |
| **Profile**   | profileId, skills, portfolio, rating                                | Belongs to User                                                           |
| **JobPost**   | jobId, title, description, skillsRequired, budget, status          | Created by User (Employer), Receives Proposals                           |
| **Proposal**  | proposalId, coverLetter, bidAmount, status                         | Submitted by User (Freelancer), Targets a JobPost                        |
| **Contract**  | contractId, startDate, endDate, terms                              | Binds Freelancer to JobPost after Proposal acceptance                     |
| **Message**   | messageId, senderId, receiverId, content, timestamp                | Exchanged between Users                                                  |
| **Review**    | reviewId, rating, comment, reviewerId, reviewedUserId              | Given by one User to another after a Contract                            |
| **Payment**   | paymentId, amount, date, status                                     | Linked to a Contract                                                     |
