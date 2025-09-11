if ! mysql $mysql_flags -e "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_NAME = 'clients';" 2>&1 > /dev/null ;
then
  mysql $mysql_flags < /opt/app-root/src/init_db.sql
fi
