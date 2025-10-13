if ! mysql $mysql_flags -e "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_NAME = 'clients';" | grep "clients" 2>&1 > /dev/null ;
then
  echo "Initializing clients table"
  echo "USE ${MYSQL_DATABASE};" > /opt/app-root/src/tmp_init_db.sql
  cat /opt/app-root/src/init_db.sql >> /opt/app-root/src/tmp_init_db.sql
  mysql $mysql_flags < /opt/app-root/src/tmp_init_db.sql
else
  echo "clients table already initialized"
fi
