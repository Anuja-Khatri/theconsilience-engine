# Production Infrastructure

The full stack, stated plainly. Every absent technology is a deliberate choice.

## What is in the stack

| Component | Technology | Purpose |
|---|---|---|
| Backend framework | FastAPI (Python, async) | API server with auto-documented OpenAPI |
| Database | Postgres via Supabase | Relational data, auth, row-level security, REST API |
| Migrations | Alembic | Versioned database schema changes tracked in Git |
| Job queue | Postgres-backed | Comparison jobs queued and processed |
| Backend hosting | Railway | PaaS, approximately $20/month |
| Frontend hosting | Vercel | Free tier |
| Document storage | S3-compatible encrypted | Source documents, per-workspace prefixes |
| Extraction models | Claude Haiku and Sonnet via Anthropic Batch API | Typed claim extraction at 50% cost |

## What is NOT in the stack

| Absent technology | Why |
|---|---|
| Kafka | Replaced by Postgres job queue. Same function, zero operational overhead. |
| Redis | Not needed. Session state in Postgres. Caching not required at current scale. |
| Celery | Replaced by Postgres job queue. |
| Kubernetes | Overkill for a single-server deployment. Railway handles scaling. |
| Microservices | Monolith is correct at this scale. Every microservice boundary is a maintenance burden. |
| Pinecone / vector DB | V1 used Pinecone. V2 does not need it. Matching is graph-based, not embedding-based. |
| Fine-tuned models | No LoRA, no domain adapters. Schema-constrained extraction is sufficient. |

## Cost

The entire production system runs on approximately $20/month for backend hosting plus Anthropic API costs for extraction (Batch API at 50% discount). No GPU costs. No vector database costs. No Kubernetes cluster costs.

This is deliberate. Infrastructure cost scales with the number of comparisons run, not with idle capacity.

## Deployment

CI/CD pipeline. Environment management. Versioned database migrations. Content hash verification on every deployment. The full lifecycle from code change to running system is automated.
