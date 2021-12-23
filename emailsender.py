import smtplib


def sendMail(emailaddresses):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("lavizsecond123@gmail.com", "Laviz6969")
    server.sendmail("lavizsecond123@gmail.com", emailaddresses, "There is rainfall in your area")
    server.quit()
