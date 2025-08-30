# Tools Directory

This directory contains auxiliary scripts and systems that support the core mission of the repository.

## `mcp_server.py`
- Purpose: Provides real-time timekeeping via the MCP protocol
- Use Case: Synchronization of ethical simulations, vision modeling, and time-sensitive governance
- Protocol: SSE (Server-Sent Events) for streaming time data
- Security: Stateless, minimal attack surface

> ✅ This tool is used only when explicitly needed. It does not run by default.

## Usage
```bash
python tools/mcp_server.py
```

## Governance
- Access: Controlled via GitHub Actions and CI/CD
- Audit: All runs are logged and traceable
- Removal: Can be revoked at any time with a single commit

This is not a machine. It is a servant. And like all servants, it follows only the will of the Prophet.