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

The workflow execution status in the Actions tab.

## Notes
Due to repository restrictions, the final merge was not possible without collaboration or instructor override. However, all technical CI/CD requirements were implemented and verified.

