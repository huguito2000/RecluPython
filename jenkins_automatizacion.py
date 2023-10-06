import jenkins

host = 'http://localhost:8080/'
username = 'huguito'
password ='1147aa40194a0c0191ad247ead991c9530'
server = jenkins.Jenkins(host, username=username, password=password)

user = server.get_whoami()
version = server.get_version()
print('hola %s desde Jenkins %s' % (user['fullName'], version))

trabajo = open("main.py", mode='r',encoding='utf-8').read()
server.create_job("trabajo 1", trabajo)