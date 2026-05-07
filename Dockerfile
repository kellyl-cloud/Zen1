FROM heartexlabs/label-studio:latest

# Expose the port Railway will use
EXPOSE 8080

# Label Studio reads these env vars automatically
ENV LABEL_STUDIO_HOST=0.0.0.0
ENV LABEL_STUDIO_PORT=8080
