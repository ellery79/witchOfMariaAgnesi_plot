# syntax=docker/dockerfile:1

# Use a versioned slim base image for reproducibility and small size.
FROM dhi.io/python:3-sfw-dev

# Define arguments for user and group IDs. This makes the build configurable.
ARG UID=10001
ARG GID=10001

# --- FIX FOR GIT PAGER ERROR ---
# Forces git to print output directly to stdout instead of looking for 'less'.
ENV GIT_PAGER=cat

# --- MODIFIED SECTION FOR DEBIAN ---
# 1. Create the user and group as before.
# 2. Immediately remove /var/log/faillog and /var/log/lastlog in the same
#    RUN command to prevent the sparse file bug.
RUN apt-get update && apt-get install -y passwd adduser openssh-client curl ca-certificates gzip && \
    mkdir -p /usr/local/bin && \
    curl -sS https://starship.rs/install.sh | sh -s -- -y && \
    rm -rf /var/lib/apt/lists/* && \
    addgroup --system --gid "${GID}" appuser && \
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
RUN ldconfig
USER appuser

# Activate Starship for the appuser
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc

# Your container will idle by default, allowing you to attach a shell
CMD ["sleep", "infinity"]