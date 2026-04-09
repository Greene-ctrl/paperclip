FROM node:20-slim

# Setup unprivileged user for Hugging Face Spaces
RUN useradd -m -u 1000 user

# Install necessary packages (like git for some adapters)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

USER user
WORKDIR /home/user/app

# HF Spaces listens on 7860
ENV PORT=7860
ENV HOST=0.0.0.0
# The server requires PAPERCLIP_HOME, and it must be writable by user
ENV PAPERCLIP_HOME=/home/user/app/data

# Create data directory
RUN mkdir -p /home/user/app/data

# Use `npx paperclipai onboard --yes` to onboard and `npx paperclipai run` to start
# The user wants "npx paperclipai onboard --yes     and then streams the ui into the huggingface frontend port on 7860 and is interactive henceforth"
CMD ["sh", "-c", "npx --yes paperclipai onboard --yes && npx --yes paperclipai run"]
