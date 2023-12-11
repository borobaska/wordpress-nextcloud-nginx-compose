root_password = input("Enter MySQL root password: ")

nextcloud_user = input("Enter Nextcloud username: ")
nextcloud_password = input("Enter Nextcloud password: ")
nextcloud_database = input("Enter Nextcloud database name: ")

wordpress_user = input("Enter MySQL Wordpress username: ")
wordpress_password = input("Enter Wordpress password: ")
wordpress_database = input("Enter Wordpress database name: ")

with open("./mariadb/01.sql", "w") as init_f:
    init_f.write(f"""
CREATE DATABASE IF NOT EXISTS `{wordpress_database}`;
CREATE USER {wordpress_user}@'%' IDENTIFIED BY '{wordpress_password}';

CREATE DATABASE IF NOT EXISTS `{nextcloud_database}`;
CREATE USER {nextcloud_user}@'%' IDENTIFIED BY '{nextcloud_password}';

GRANT ALL PRIVILEGES ON {wordpress_database}.* TO {wordpress_user}@'%';
GRANT ALL PRIVILEGES ON {nextcloud_database}.* TO {nextcloud_user}@'%';
    """)

with open("./.env", "w") as dotenv_f:
    dotenv_f.write(f"""
MYSQL_ROOT_PASSWORD: {root_password}

MYSQL_NEXTCLOUD_USER: {nextcloud_user}
MYSQL_NEXTCLOUD_PASSWORD: {nextcloud_password}
MYSQL_NEXTCLOUD_DATABASE: {nextcloud_database}

MYSQL_WORDPRESS_USER: {wordpress_user}
MYSQL_WORDPRESS_PASSWORD: {wordpress_password}
MYSQL_WORDPRESS_DATABASE: {wordpress_database}
    """)
