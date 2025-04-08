# **Class Diagram for Library System**

```mermaid
classDiagram
class Book {
  -title: String
  -ISBN: String
  -status: String
  +checkOut()
  +return()
}
class User {
  -userId: String
  -name: String
  +borrowBook()
  +returnBook()
}
class Loan {
  -loanId: String
  -dueDate: Date
  +calculateFine()
}

User "1" -- "0..*" Loan : borrows
Book "1" -- "0..1" Loan : associatedWith
