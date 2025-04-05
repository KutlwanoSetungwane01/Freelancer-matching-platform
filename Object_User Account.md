## 1. User Account - State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Unregistered
    Unregistered --> PendingVerification : User registers
    PendingVerification --> Active : Email verified
    Active --> Suspended : Admin suspends account
    Suspended --> Active : Admin reactivates
    Active --> Deactivated : User deactivates account
    Deactivated --> Active : User reactivates account
    Active --> Deleted : User deletes account
    Suspended --> Deleted : Admin deletes account
```
### User Account - State Diagram Explanation

This diagram shows the different stages a user account can go through on the platform.

- A user starts as **Unregistered**, then registers and enters **Pending Verification**.
- After verifying their email, the account becomes **Active**.
- The account can be **Suspended** by an admin, **Deactivated** by the user, or permanently **Deleted**.
- Users can also reactivate their accounts after deactivation.

## 2. Job Post - State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Published : User submits job post
    Published --> Closed : Job filled or deadline passed
    Draft --> Deleted : User deletes draft
    Published --> Archived : Job manually archived
    Closed --> Archived : Archived after job is filled

```
## Job Post - State Diagram Explanation


This diagram shows the lifecycle of a Job Post on the platform.

- A job starts as a Draft and moves to Published when submitted.

- Once a job is filled or expires, it transitions to Closed.

- From there, it may be Archived for future reference.

- Users can also delete a job while it's still in draft mode.

## 3. Proposal - State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Submitted : Freelancer submits proposal
    Submitted --> Reviewed : Client views proposal
    Reviewed --> Accepted : Client accepts proposal
    Reviewed --> Rejected : Client rejects proposal
    Accepted --> Withdrawn : Freelancer withdraws before contract
    Draft --> Deleted : Freelancer deletes draft
```

## Proposal - State Diagram Explanation


This diagram represents the states a Proposal goes through from creation to decision.

- A proposal begins as a Draft, then moves to Submitted when sent.

- The client then Reviews the proposal and either Accepts or Rejects it.

- If accepted, the freelancer can still Withdraw the proposal before a contract is signed.

- Drafts can also be Deleted by the freelancer before submission.

## 4. Project - State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Initiated
    Initiated --> InProgress : Work begins
    InProgress --> OnHold : Client pauses project
    OnHold --> InProgress : Client resumes project
    InProgress --> Completed : Work is finished
    InProgress --> Canceled : Project is canceled mid-way
    OnHold --> Canceled : Client cancels during pause
```

## Project - State Diagram Explanation


This diagram illustrates the lifecycle of a Project from start to finish.

- A project starts as Initiated, then moves to In Progress when the freelancer begins working.

- It can be Paused (On Hold) by the client and later resumed.

- Once the work is done, the project moves to Completed.

- Projects can also be Canceled either mid-way or while on hold.

## 5. Contract - State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Active : Both parties sign
    Active --> Completed : Project successfully delivered
    Active --> Disputed : One party raises an issue
    Disputed --> Resolved : Dispute resolved and contract completed
    Disputed --> Terminated : Contract cancelled due to dispute
    Draft --> Cancelled : Client or freelancer cancels before signing
```

## Contract - State Diagram Explanation


This diagram defines how a Contract progresses through the system.

- Starts in Draft, becomes Active once both parties agree.

- From Active, it can move to Completed if delivered, or Disputed if issues arise.

- Disputes can be either Resolved or lead to Termination.

- Drafts can also be Cancelled if either party backs out before signing.

## 6. Payment - State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Processed : Payment is processed
    Processed --> Completed : Payment is successfully received
    Processed --> Failed : Payment failed
    Failed --> Retry : User retries payment
    Completed --> Refunded : Payment is refunded
    Pending --> Canceled : Payment canceled by user
```
## Payment - State Diagram Explanation


This diagram outlines the lifecycle of a Payment.

- Payments begin in Pending, and once processed, they can either be Completed or Failed.

- Failed payments can be retried, while completed payments can later be Refunded.

- Users also have the option to cancel the payment while it’s still in the pending state.

## 7. Review - State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Submitted : User submits review
    Submitted --> Approved : Admin approves review
    Approved --> Published : Review goes live
    Approved --> Rejected : Admin rejects review
    Published --> Edited : User edits the review
    Published --> Deleted : User or admin deletes review

```
## Review - State Diagram Explanation


This diagram defines the lifecycle of a Review.

- A review starts in Draft, and once submitted, it moves to Submitted.

- Admin approval is needed for it to be Approved and then Published.

- Reviews can also be Rejected by admins or Edited by the user after publication.

- Both users and admins can Delete reviews.

## 8. Message - State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Sent : User sends message
    Sent --> Delivered : Message delivered to recipient
    Delivered --> Read : Recipient reads message
    Read --> Replied : Recipient replies to message
    Replied --> Read : Sender reads the reply
    Sent --> Failed : Message delivery failed
    Sent --> Canceled : User cancels the message
```
## Message - State Diagram Explanation


This diagram outlines the lifecycle of a Message.

- A message begins as a Draft, then gets Sent by the user.

- Once sent, it moves to Delivered, and if read, it becomes Read.

- After reading, the recipient can Reply, and the sender can read the response.

- Messages can also Fail to deliver or be Canceled before sending.


