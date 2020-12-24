#!/bin/bash

clear

pip install -r /Users/$USER/AntiFraudProject/requirements.txt

cat > start_server.command <<EOF
python /Users/$USER/AntiFraudProject/manage.py runserver
EOF

cat > start_gen.command <<EOF
cd /Users/$USER/AntiFraudProject/Gen
python main.py
EOF

chmod +x start_gen.command
open start_gen.command

chmod +x start_server.command
open start_server.command

while [[ $(lsof -i :8000 | wc -l) -lt 1 ]]; do
        echo "waiting"
        sleep 0.5
done

rm -rf start_server.command
rm -rf start_gen.command

/usr/bin/open -a "Google Chrome" "http://127.0.0.1:8000/"
