#!/bin/bash

echo -n "Enter database server IP address: "
read host
echo -n "Enter PostgreSQL admin's password on $host: "
read -s admin_password
echo -e "\n"

./automation.sh $host $admin_password  >> /dev/null
echo -e "End of scripts."
