if ! mysql $mysql_flags -e "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_NAME = 'clients';" | grep "clients" 2>&1 > /dev/null ;
then
  echo "Initializing clients table"
  mysql $mysql_flags < /opt/app-root/src/init_db.sql
else
  echo "clients table already initialized"
fi
