CREATE DATABASE IF NOT EXISTS `wordpress_db`;
CREATE USER wordpress_u@'%' IDENTIFIED BY 'sureway__wp_pwd';

CREATE DATABASE IF NOT EXISTS `nextcloud_db`;
CREATE USER nextcloud_u@'%' IDENTIFIED BY 'sureway__nc_pwd';

GRANT ALL PRIVILEGES ON wordpress_db.* TO wordpress_u@'%';
GRANT ALL PRIVILEGES ON nextcloud_db.* TO nextcloud_u@'%';