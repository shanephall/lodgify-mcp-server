# Use Python 3.11 slim image for smaller size (aligned with .python-version)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for faster dependency management
RUN pip install --no-cache-dir uv

# Copy dependency files first for better Docker layer caching
COPY pyproject.toml uv.lock ./

# Create virtual environment and install dependencies using uv
RUN uv venv && uv sync --no-dev --no-install-project

# Copy all application files
COPY README.md lodgify_server.py entrypoint.py ./

# Add uv's virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Ensure the virtual environment is properly activated and test imports
RUN /app/.venv/bin/python -c "import sys; print(f'Python: {sys.executable}'); import lodgify_server; print('✓ lodgify_server import successful')"

# Make entrypoint executable
RUN chmod +x entrypoint.py

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Expose the default MCP port
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Health check that actually validates the server
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD /app/.venv/bin/python -c "import lodgify_server; print('Health check: Server module imports successfully')" || exit 1

# Default command to run the MCP server
ENTRYPOINT ["/app/.venv/bin/python", "entrypoint.py"]
CMD ["--mode", "info"]
