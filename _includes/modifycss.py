def main():
	infile = open("main.css")
	outfile = open("mmain.css",'w')
	input = infile.read()
	i=0
	ch = input[i]
	while(ch!='\n'):
		if(ch=='}'):
			outfile.write('\n')
			outfile.write('}')
			outfile.write('\n')
			outfile.write('\n')
		
		elif(ch==';' or ch=='{'):
			outfile.write(ch)
			outfile.write('\n')
		else:
			outfile.write(ch)
		i += 1;
		ch = input[i]
main()