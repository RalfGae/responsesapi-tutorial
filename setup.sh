#!/bin/bash

echo "📦 Starting setup..."

# Check if venv exists
if [ ! -d "venv" ]; then
  echo "🔧 Creating virtual environment..."
  python3 -m venv venv

  echo "📥 Installing dependencies from requirements.txt..."
  source venv/bin/activate
  pip install -r requirements.txt
else
  echo "✅ Virtual environment already exists. Skipping creation."
fi

echo ""
echo "✅ Setup complete."

echo ""
echo "📌 Next steps:"
echo "➡️  Run: source venv/bin/activate"
echo "➡️  Then: python3 lesson-1.py (or another lesson file)"
