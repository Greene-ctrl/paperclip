FROM node:20-slim

# In node images, UID 1000 is typically already assigned to 'node'.
# We can just change its name or use the existing node user, but HF expects a 'user' name
# actually HF expects the user running the process to have UID 1000. It doesn't matter what it's named.
# We will just use the pre-existing 'node' user or rename it. Let's just create 'user' with a different UID or reuse node.
# Let's rename the node user to 'user' or just use the node user directly.
# Let's just use the 'node' user which is UID 1000.

# Install necessary packages (like git for some adapters)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

USER node
WORKDIR /home/node/app

# HF Spaces listens on 7860
ENV PORT=7860
ENV HOST=0.0.0.0
# The server requires PAPERCLIP_HOME, and it must be writable by user
ENV PAPERCLIP_HOME=/home/node/app/data

# Create data directory
RUN mkdir -p /home/node/app/data

# Use `npx paperclipai onboard --yes` to onboard and `npx paperclipai run` to start
CMD ["sh", "-c", "npx --yes paperclipai onboard --yes && npx --yes paperclipai run"]
