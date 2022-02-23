#test_zip
import zipfile
zname=r'X:\\tralala2.zip'
newzip=zipfile.ZipFile(zname,'w')
newzip.write(r'X:\\Pictures')
newzip.write(r'X:\\Radeon ReLive\\Instant GIF')
newzip.close()
