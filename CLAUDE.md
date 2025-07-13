# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Multi-Modal (MM) Agent Chatbot application with a Python FastAPI backend and Next.js frontend. The system includes user authentication, file management, document parsing, and chat functionality with OpenAI integration.

## Development Commands

### Frontend (Next.js)
- **Development**: `cd frontend && pnpm dev` (uses Turbopack)
- **Build**: `cd frontend && pnpm build`
- **Lint**: `cd frontend && pnpm lint`
- **Type checking**: `cd frontend && npx tsc --noEmit`

### Backend (FastAPI/Python)
- **Development**: `cd backend && poetry run fastapi dev src/backend/main.py`
- **Install dependencies**: `cd backend && poetry install`
- **Database migrations**: `cd backend && poetry run alembic upgrade head`

### Docker Development
- **Full stack**: `docker-compose up --build`
- **Frontend only**: `docker-compose up frontend`
- **Backend only**: `docker-compose up backend db`

## Architecture Overview

### Backend Structure (`backend/src/backend/`)
- **FastAPI application** with modular router design
- **Database**: PostgreSQL with SQLAlchemy ORM and Alembic migrations
- **Authentication**: JWT-based with bcrypt password hashing
- **File handling**: Document parsing with PyMuPDF
- **AI Integration**: OpenAI API for chat functionality

Key modules:
- `main.py`: FastAPI app with CORS middleware and router registration
- `models.py`: SQLAlchemy models (User, File with UUID primary keys)
- `database.py`: Database configuration and session management
- `routers/`: Modular API endpoints (auth, users, files, chat)
- `document_parser.py`: PDF text extraction functionality

### Frontend Structure (`frontend/src/`)
- **Next.js 15** with App Router and TypeScript
- **Authentication flow**: Login/signup pages with context-based state management
- **UI Components**: Radix UI primitives with Tailwind CSS styling
- **Pages**: Chat interface (`/chat`) and file management (`/files`)

Key components:
- `app/(app)/`: Protected app routes with shared layout
- `contexts/auth-context.tsx`: Authentication state management
- `components/ui/`: Reusable Radix UI components
- `middleware.ts`: Route protection and authentication checks

## Database Schema

- **Users**: UUID primary key, name, email, hashed_password
- **Files**: UUID primary key, name (duplicated), content_type, size, user relationship
- **Alembic migrations** in `backend/alembic/versions/`

## API Architecture

RESTful API with the following router modules:
- `/auth`: Login, logout, registration endpoints
- `/users`: User management
- `/files`: File upload, retrieval, and parsing
- `/chat`: Chat functionality with OpenAI integration

## Development Workflow

1. **Database setup**: Ensure PostgreSQL is running (via Docker or local)
2. **Backend**: Install dependencies with Poetry, run migrations, start FastAPI dev server
3. **Frontend**: Install dependencies with pnpm, start Next.js dev server
4. **Full stack testing**: Use docker-compose for complete environment

## Important Notes

- Frontend has existing CLAUDE.md with detailed component and routing information
- No test files currently exist in the codebase
- Backend uses Poetry for dependency management
- Frontend uses pnpm for package management
- Authentication uses JWT tokens with protected routes via Next.js middleware
- CORS is configured to allow all origins in development