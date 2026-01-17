<h1>This is a 5th year Alt4 project</h1>

It took me about a week to complete
I used a RaspberryPie,The PiCamera and a PIR motion sensor

When the PIR sensor detects motion the PiCamera begins recording (as a .h264 file) once the motion has stopped an email is sent to 
the reciever with the time motion was detected and the video clip captured from the PiCamera

I created the function send_mail in the SendingEmailsWithAttachments file

To allow python access to your gmail account u must provide a security key

You can create one of these in your gmail account

This program can only send mail to gmail accoounts as that is the server it is conncted to


Note:To open .h264 files you may need to install a media player such as VLC

