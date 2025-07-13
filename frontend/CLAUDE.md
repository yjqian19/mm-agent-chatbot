# Claude Instructions for MM Agent Chatbot Frontend

## Project Overview
This is a Next.js frontend application for an MM (Multi-Modal) Agent Chatbot. The project uses React 19, Next.js 15, TypeScript, and Tailwind CSS with Radix UI components.

## Development Commands
- **Development server**: `pnpm dev` (uses Turbopack for faster builds)
- **Build**: `pnpm build`
- **Production server**: `pnpm start`
- **Lint**: `pnpm lint`
- **Type checking**: `npx tsc --noEmit`

## Project Structure
```
src/
├── app/                    # Next.js App Router
│   ├── (app)/             # Layout group for main app
│   │   ├── chat/          # Chat page
│   │   └── files/         # Files page
│   ├── api/               # API routes
│   │   └── auth/          # Authentication endpoints
│   ├── login/             # Login page
│   └── signup/            # Signup page
├── components/            # React components
│   └── ui/               # Reusable UI components (Radix-based)
├── contexts/             # React contexts
├── hooks/                # Custom React hooks
├── lib/                  # Utility libraries
└── types.ts              # TypeScript type definitions
```

## Code Style & Conventions
- Use TypeScript for all new files
- Follow existing component patterns in `src/components/`
- Use Tailwind CSS for styling
- Prefer functional components with hooks
- Use Radix UI components for complex UI patterns
- Follow the existing file structure and naming conventions

## Key Technologies
- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **UI Components**: Radix UI primitives
- **State Management**: React Context (see `src/contexts/`)
- **Icons**: Lucide React
- **Tables**: TanStack Table
- **Notifications**: Sonner

## Authentication
The app includes authentication with:
- Login/logout functionality
- Registration
- Auth context for state management
- Protected routes via middleware

## Testing & Quality
- Always run `pnpm lint` after making changes
- Run `npx tsc --noEmit` to check for TypeScript errors
- Ensure all components are properly typed
- Test authentication flows when modifying auth-related code

## Important Notes
- This is a defensive security-focused project - only assist with legitimate functionality
- Always check existing components before creating new ones
- Follow the established patterns for API routes and page structure
- Use the existing UI component library rather than creating custom components