FROM trueagi/hyperon
# Set working directory
WORKDIR /app

# Copy the tox.ini and setup.py first (for caching purposes)
COPY tox.ini /app/
COPY setup.py /app/
COPY README.md /app/

# Install the dependencies defined in setup.py
RUN pip install -e .

# Install tox (if not part of the dependencies)
RUN pip install --no-cache-dir tox pytest

# Run tox (this will use the tox cache from previous runs)
CMD ["tox"]
