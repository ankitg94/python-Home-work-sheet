
#answer-1
f =open('test.txt','r')
f.read()
f.close()
#answer-2
f=open('myfile.txt','w')
f.write("you are my crush ::::")
f.close()
#answer-3
f=open('myfile.txt','r+')
f.read()
f.close()
print(f)
#answer-4
f=open('cities.txt','w')
f.write("delhi ,bengluru,kolkata")
f.close()
#answer-5
f=open('cities.txt','a')
f.write(" ,cheenai , agra,")
f.close()
#answer-6
def search(filename,word):
   try:
       f=open(filename,'r')
       line_count =0
       for line in f.readlines():
           line_count+=1
           strlist = line.split(' ') 
           word_count= 0
           for w in strlist:
               word_count+=1
               if word==w:
                   return(line_count,word_count)
       else:
           return None
       f.close()
   except FileNotFoundError:
       print("file not found") 
x=search('cities.txt','delhi')       
print(x)

#answer-9
import pickle
bookfile={'r-chand':225,'rs.agrwal':90,'jeevan':320}
f=open('student','ab')
pickle.dump(bookfile,f)
f.close()
print(f)

#answer-10
import pickle
f=open.load('student','ab')
s=pickle.load(f)
for key in s:
    print(jeevan,'....',s[key])
f.close()    