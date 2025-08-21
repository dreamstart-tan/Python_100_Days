-- 创建用户
-- Create User 'wangdachui'@'%' identified by 'Wang.618';
 
-- 上面的 SQL 创建了名为 wangdachui 的用户，它的访问口令是 Wang.618，该用户可以从任意主机访问数据库服务器，因为 @ 后面使用了可以表示任意多个字符的通配符 %。如果要限制 wangdachui 这个用户只能从 192.168.0.x 
-- 这个网段的主机访问数据库服务器，可以按照下面的方式来修改 SQL 语句。

-- Drop USER IF exists 'wangdachui'@'%';
-- create user 'wangdachui'@'192.168.0.%' identified by 'Wang.618';
-- 此时，如果我们使用 wangdachui 这个账号访问数据库服务器，我们几乎不能做任何操作，
-- 因为该账号没有任何操作权限。

--  授予权限
--  我们用下面的语句为 wangdachui 授予查询 school 数据库学院表（tb_college）的权限。

GRANT SELECT ON `school`.`tb_college`TO'wangdachui'@'192.168.0.%';

-- 我们也可以让 wangdachui 对 school 数据库的所有对象都具有查询权限，代码如下所示。

Grant select on `school`.* TO 'wangdachui'@'192.168.0.%';

-- 如果我们希望 wangdachui 还有 insert、delete 和 update 权限，可以使用下面的方式进行操作。

Grant insert,delete,update on `school`.* TO 'wangdachui'@'192.168.0.%';

-- 如果我们还想授予 wangdachui 执行 DDL 的权限，可以使用如下所示的 SQL。
Grant Create,drop,Alter on `school`.* to'wangdachui'@'192.168.0.%';

-- 如果我们希望 wangdachui 账号对所有数据库的所有对象都具备所有的操作权限，可以执行如下所示的操作，但是一般情况下，
-- 我们不会这样做，因为我们之前说过，权限刚刚够用就行，一个普通的账号不应该拥有这么大的权限。

GRANT ALL PRIVILEGES ON *.* TO 'wangdachui'@'192.168.0.%';

-- 召回权限 
-- 如果要召回 wangdachui 对 school 数据库的 insert、delete 和 update 权限，可以使用下面的操作。

REVOKE INSERT, DELETE, UPDATE ON `school`.* FROM 'wangdachui'@'192.168.0.%';

-- 如果要召回所有的权限，可以按照如下所示的方式进行操作。

Revoke all privileges on *.* from 'wangdachui'@'192.168.0.%';

-- 需要说明的是，由于数据库可能会缓存用户的权限，可以在授予或召回权限后执行下面的语句使新的权限即时生效。

FLUSH PRIVILEGES;




