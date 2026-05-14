#!/bin/bash
echo ""
echo "╔══════════════════════════════════════╗"
echo "║   Portfólio — Gilberto Júnior        ║"
echo "╚══════════════════════════════════════╝"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt --quiet
python manage.py makemigrations core
python manage.py migrate
python seed.py
echo ""
echo "╔══════════════════════════════════════╗"
echo "║  Para rodar:                         ║"
echo "║  source .venv/bin/activate           ║"
echo "║  python manage.py runserver          ║"
echo "║                                      ║"
echo "║  Site:  http://localhost:8000        ║"
echo "║  Admin: http://localhost:8000/admin  ║"
echo "║  Login: admin / admin123             ║"
echo "╚══════════════════════════════════════╝"
