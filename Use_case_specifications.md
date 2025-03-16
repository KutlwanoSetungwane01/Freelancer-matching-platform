# **Use Case Specifications for Freelancer Job Matching Platform**

## **Use Case 1: User Registration**
- **Actor:** Freelancer, Employer  
- **Preconditions:** User must have a valid email address.  
- **Postconditions:** User is successfully registered and can log in.  
- **Basic Flow:**
  1. User visits the registration page.
  2. User enters their name, email, and password.
  3. User selects their role (Freelancer or Employer).
  4. System sends a verification email.
  5. User clicks the verification link.
  6. System confirms registration and redirects to the login page.
- **Alternative Flows:**
  - **Invalid Email:** System displays an error message if an invalid email is entered.
  - **Email Already Exists:** System notifies the user and prompts login.

---

## **Use Case 2: Freelancer Applies for a Job**
- **Actor:** Freelancer  
- **Preconditions:** Freelancer must be logged in and have a complete profile.  
- **Postconditions:** Job application is submitted to the employer.  
- **Basic Flow:**
  1. Freelancer browses job listings.
  2. Freelancer clicks on a job to view details.
  3. Freelancer clicks "Apply."
  4. System prompts the freelancer to attach a cover letter (optional).
  5. System submits the application to the employer.
  6. System confirms application submission.
- **Alternative Flows:**
  - **Incomplete Profile:** System prevents application and asks the freelancer to update their profile.
  - **Job Expired:** System displays a message that the job is no longer available.

---

## **Use Case 3: Employer Posts a Job**
- **Actor:** Employer  
- **Preconditions:** Employer must be logged in.  
- **Postconditions:** Job is successfully posted and visible to freelancers.  
- **Basic Flow:**
  1. Employer logs in and navigates to "Post a Job."
  2. Employer enters job title, description, required skills, and budget.
  3. Employer sets a deadline and clicks "Submit."
  4. System verifies and saves the job listing.
  5. System displays a confirmation message.
- **Alternative Flows:**
  - **Missing Information:** System prompts the employer to fill in required fields.
  - **Budget Exceeds Limit:** System alerts the employer to adjust the budget.

---

## **Use Case 4: Employer Reviews Applications**
- **Actor:** Employer  
- **Preconditions:** Employer must have posted at least one job.  
- **Postconditions:** Employer shortlists or hires a freelancer.  
- **Basic Flow:**
  1. Employer logs in and views applications for a job.
  2. Employer filters applications by skills, experience, or ratings.
  3. Employer clicks on a freelancer’s profile for details.
  4. Employer sends a message to the freelancer or hires them.
- **Alternative Flows:**
  - **No Applications Yet:** System displays a message stating that no applications are available.
  - **Freelancer Declines Offer:** Employer receives a notification.

---

## **Use Case 5: Freelancer Updates Profile**
- **Actor:** Freelancer  
- **Preconditions:** Freelancer must be logged in.  
- **Postconditions:** Freelancer profile is updated.  
- **Basic Flow:**
  1. Freelancer logs in and navigates to the profile page.
  2. Freelancer edits their skills, experience, or portfolio.
  3. Freelancer clicks "Save Changes."
  4. System updates the profile.
  5. System confirms the update with a success message.

---

## **Use Case 6: Messaging Between Freelancer and Employer**
- **Actor:** Freelancer, Employer  
- **Preconditions:** Both users must be logged in.  
- **Postconditions:** Messages are sent and received successfully.  
- **Basic Flow:**
  1. Freelancer/employer navigates to the messaging section.
  2. User selects a conversation or starts a new chat.
  3. User types a message and clicks "Send."
  4. System delivers the message in real time.
- **Alternative Flows:**
  - **User Offline:** Message is stored and delivered when the recipient is online.
  - **Spam Detection:** System may flag messages with suspicious content.

---

## **Use Case 7: Secure Payment Processing**
- **Actor:** Freelancer, Employer  
- **Preconditions:** Employer must have a valid payment method.  
- **Postconditions:** Payment is processed successfully.  
- **Basic Flow:**
  1. Employer selects a freelancer to hire.
  2. Employer chooses a payment method.
  3. System verifies payment details.
  4. Employer confirms the transaction.
  5. System processes payment securely.
  6. Freelancer receives payment notification.
- **Alternative Flows:**
  - **Insufficient Funds:** Payment fails, and employer is notified.
  - **Technical Error:** System retries payment or asks employer to try again.

---

## **Use Case 8: Admin Manages Platform**
- **Actor:** System Administrator  
- **Preconditions:** Admin must have special access rights.  
- **Postconditions:** Platform settings are updated.  
- **Basic Flow:**
  1. Admin logs into the admin dashboard.
  2. Admin views user activity and reports.
  3. Admin updates system settings (e.g., security, policies).
  4. System applies changes.
  5. Admin logs out.
- **Alternative Flows:**
  - **Unauthorized Access:** System blocks login attempts for non-admin users.
  - **System Error:** System logs the error and alerts technical support.

