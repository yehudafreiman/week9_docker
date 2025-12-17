# תמונת בסיס
FROM python:3.11-slim

# תיקיית עבודה
WORKDIR /app

# העתקת requirements והתקנה
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קוד
COPY . .

# יצירת תיקייה למסד הנתונים
RUN mkdir -p /app/db

# פורט
EXPOSE 8000

# פקודת הרצה
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]