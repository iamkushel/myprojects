fw = open('sample.txt', 'w')
fw.write('I am kushel\n')
fw.write('I am in United states\n')
fw.write('To be or not be and To do or not to, is a choice')
fw.close()

fr = open('sample.txt', 'r')
txt = fr.read()
print(txt)
fr.close()
