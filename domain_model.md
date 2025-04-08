# **Domain Model for Library System**

| Class   | Attributes                  | Methods                    | Relationships                |
|---------|-----------------------------|----------------------------|------------------------------|
| Book    | title, ISBN, status         | checkOut(), return()       | Associated with Loan         |
| User    | userId, name                | borrowBook(), returnBook() | Borrows Loan                 |
| Loan    | loanId, dueDate             | calculateFine()            | Linked to Book and User      |
