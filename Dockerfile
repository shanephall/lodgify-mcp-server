# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install uv for faster dependency management
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen

# Add uv's virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy application code
COPY lodgify_server.py main.py entrypoint.py ./

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

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Default command to run the MCP server
ENTRYPOINT ["python", "entrypoint.py"]
CMD ["--mode", "info"]
