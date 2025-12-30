# syntax=docker/dockerfile:1

# Use a versioned slim base image for reproducibility and small size.
FROM python:3.14-slim

# Define arguments for user and group IDs. This makes the build configurable.
ARG UID=10001
ARG GID=10001

# --- MODIFIED SECTION FOR DEBIAN ---
# 1. Create the user and group as before.
# 2. Immediately remove /var/log/faillog and /var/log/lastlog in the same
#    RUN command to prevent the sparse file bug.
RUN addgroup --system --gid "${GID}" appuser && \
    adduser --system --disabled-password --home /home/appuser --shell /bin/bash --uid "${UID}" --ingroup appuser appuser && \
    rm -f /var/log/faillog /var/log/lastlog
# --- END OF MODIFIED SECTION ---

# Set the working directory. This creates /app, which is initially owned by root.
WORKDIR /app

# Install matplotlib (Cached)
RUN pip install --no-cache-dir matplotlib

# Change the ownership of the working directory to the non-root user.
# This must be done before switching the user, while we still have root privileges.
RUN chown appuser:appuser /app

# Switch to the non-privileged user.
# All subsequent commands, including the ENTRYPOINT, will run as 'appuser'.
USER appuser

# Your container will idle by default, allowing you to attach a shell
CMD ["sleep", "infinity"]