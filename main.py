import aiml

#criar o kernel e aprender arquivos aiml
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

#Pressione CTRL-C para quebrar o loop
while True:
	resposta = kernel.respond(raw_input("Voce: "))
	print "Megatrop:", resposta