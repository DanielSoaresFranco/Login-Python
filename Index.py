import mysql.connector as sql


def begin(cursor):
    cursor.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    Id INTEGER NOT NULL auto_increment,
    Name VARCHAR(30) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    User VARCHAR(15) NOT NULL,
    Password VARCHAR(20) NOT NULL,
    PRIMARY KEY(Id)
);""")


def register(cursor, Name, Email, User, Password):
    cursor.execute(f"""INSERT INTO userdata VALUES (default, '{Name}', '{Email}', '{User}', '{Password}')""")


def verify(data, user, password):
    for c in range(0, len(data)):
        if user == data[c][3] and data[c][4] == password:
            return 'You entered'
    else:
        return 'User or Password Incorrect'


def end(conn):
    conn.commit()
    conn.close()


db_connection = sql.connect(host='localhost', port='3307', database='users', user='root', password='')
executer = db_connection.cursor()
begin(executer)
executer.execute('SELECT * FROM userdata')
data = executer.fetchall()
print(data)
create = str(input('Create Account? [Y/N] ')).lower().split()[0]
while True:
    if create[0] in 'yn':
        break
    else:
        create = str(input('Create Account? [Y/N] ')).lower().split()[0]

if create[0] == 'y':
    name = str(input('Name: '))
    email = str(input('Email: '))
    user = str(input('Username: '))
    password = str(input('Password: '))
    create = 'n'
    register(executer, name, email, user, password)
else:
    print("""




Log In""")
    while True:
        user = str(input('Username: '))
        passwd = str(input('Password: '))
        print(verify(data, user, passwd))
        if verify(data, user, passwd) == 'You entered!':
            break
        break
end(db_connection)
