# Branch Protection Rules – Assignment 13

## Why These Rules Matter

Branch protection rules are essential for maintaining code quality, especially in collaborative projects. For this assignment, I set up rules on the `main` branch to ensure that:

- Code cannot be merged without a **pull request** (PR).
- At least **one review** is required to approve changes.
- **Status checks must pass** before merging, which means all tests must succeed.
- The branch must be **up to date** before merging to avoid breaking changes.

This setup ensures that:
- Code is reviewed by someone else (even if I'm working solo, it's a good habit).
- Broken code doesn’t reach production.
- GitHub Actions will automatically run tests, and failing tests will block merging.

Even though I couldn't enable "Include administrators" or "Do not allow direct pushes," the current setup still enforces strict quality control and follows best practices used in real-world development.
