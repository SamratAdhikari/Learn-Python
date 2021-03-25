# Email Extractor

string_email = """"
samratmetaladhikari@gmail.com    Samart Adhikari    ||| I love Anime
narutoshuppuden.samrat Naruto Shippuden, naruto.uzumaki@hotmail.com haha
onepiece luffy_monkey@yahoo.com     ?? :: luffy

"""

import re
#                      samrat_metal    @ gmail            .   com
email = re.findall(r"[0-9a-zA-Z._+%?]+@[0-9a-zA-Z._+%?]+[.][a-zA-Z.0-9]+", string_email)
print(email)





