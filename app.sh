#!/bin/bash

clear

cat > start_server.command <<EOF
python /Users/$USER/AntiFraudProject/manage.py runserver
EOF

chmod +x start_server.command
open start_server.command

while [[ $(lsof -i :8000 | wc -l) -lt 1 ]]; do
        echo "waiting"
        sleep 0.5
done

rm -rf start_server.command

/usr/bin/open -e "http://127.0.0.1:8000/"
