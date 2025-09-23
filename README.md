# PDF Document Question Answering Agent

*YUJIA QIAN, September 2025*

## Overview

This is a full-stack multi-modal agent chatbot application that enables users to upload PDF documents and interact with them through natural language queries. The application consists of:

- **Backend**: FastAPI with Python 3.12+, featuring OpenAI Agent SDK integration, ChromaDB for vector storage, and WebSocket support for real-time communication
- **Frontend**: Next.js 15 with TypeScript, providing a modern React-based user interface with real-time chat capabilities

## RAG Implementation

The application implements a Retrieval-Augmented Generation (RAG) pipeline that enables intelligent document querying through semantic search and AI-powered responses.

### Key Highlights

**1. Multi-modal Data Extraction**  
Built a document parser to extract **text**, **image**, **table** data and create chunks with semantic descriptions via GPT-4.1-mini with custom Pydantic schemas. Optimized performance through **concurrent asynchronous processing** and **batched** database inserts.

**2. Retrieval (Chunking & Embedding)**  
Improved retrieval accuracy and reduced query latency by replacing page-level chunking with block-level chunking and content-based embeddings with **summary-based embeddings**, increasing top-3 hit rate and reducing token usage.

**3. Contextual Conversation**  
Integrated chat session history as context for AI agents, enabling continuous conversation flow and maintaining context across multiple queries for more coherent and personalized responses.
