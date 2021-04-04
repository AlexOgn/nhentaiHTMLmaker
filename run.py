from NHentai import NHentai

numbers_list = input()

l = numbers_list.split(" ")

finalString = ""
html = "<!DOCTYPE html><head><style>img{transition: filter .5s ease-in-out;-webkit-filter: grayscale(0%); /* Ch 23+, Saf 6.0+, BB 10.0+ */filter: grayscale(0%); /* FF 35+ */}img:hover {-webkit-filter: grayscale(100%); /* Ch 23+, Saf 6.0+, BB 10.0+ */filter: grayscale(100%); /* FF 35+ */}a{font-family: Verdana, Geneva, Tahoma, sans-serif;color:black;text-decoration: unset;}a:visited{color:purple}html { background: linear-gradient(to right top, #ffc75f, #ffae61, #ff966d, #ff807d, #ff6f91) no-repeat center center fixed; -webkit-background-size: cover; -moz-background-size: cover;-o-background-size: cover;background-size: cover;}</style><title>Document</title></head><body><center>"
print(f"Lenght of list: {len(l)}")

for i in range(len(l)):
    number = l[i]
    link = f"https://nhentai.net/g/{number}/"
    finalString += link
    try:
        nhentai = NHentai()
        obj = nhentai.search(query=str(number), sort='popular', page=1)

        non_ecoded_title = obj.title
        encoded_title = non_ecoded_title.encode("ascii", "ignore")
        title = encoded_title.decode()

        cover_link = obj.images[0]

        html += f"<a href='{link}'target='_blank'> <img src='{cover_link}'alt='{title}'style='max-width:400px;'> <br> {title}</a><br>"
    except:
        pass

html += "</center></body></html>"

html_f = open("index.html", "w")
html_f.write(html)
html_f.close()
    
    