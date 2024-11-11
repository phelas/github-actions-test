FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt
COPY . .

EXPOSE 8060

CMD ["gunicorn", "-b", "0.0.0.0:8060", "--timeout", "120", "--workers", "4", "app:server"]