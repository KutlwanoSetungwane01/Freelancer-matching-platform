## API Documentation

### GET /api/contracts
- **Description:** Fetch all contracts.
- **Response:** List of contract objects.

### POST /api/contracts
- **Description:** Create a new contract.
- **Request body:**
```json
{
  "id": "contract001",
  "job_post_id": "job123",
  "freelancer_id": "user456",
  "status": "active"
}
