###     copying files

#copyfile() = contents 
#copy() = copyfile()+permission mode+destination can be directory
#copy2() = copy() + metadata

import shutil
shutil.copyfile("aquelas.txt","copyB.txt") #source, destination