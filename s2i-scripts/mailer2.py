import mailer

message = mailer.Message()
message.From = "marocsosinfo@gmail.com"
message.To = "marocsosinfo@gmail.com"
message.Subject = "My Vacation"
message.Body = open("letter.txt", "rb").read()


sender = mailer.Mailer('marocsosinfo@gmail.com')
sender.send(message)
