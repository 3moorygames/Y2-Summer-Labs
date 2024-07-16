from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html> 
        <heading> 
        <p> Hello guys  
        <img src="https://cdn.britannica.com/23/130123-050-A88F5FE1/Monte-Carlo-Monaco.jpg"> 
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-coO6G2IuI734BMaQkhQk0NrYguFtEhJ8dw&s">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Shaheen_falcon.jpg"><br>
        <a href = \'food1\'> Go to food1 page </a>
        <a href = \'food3\'> Go to food3 page </a>
        <a href = \'pet2\'> Go to pet2 page </a><
        <a href = \'space1\'> Go to space1 page </a>
         </p> </heading> </html>''')
@app.route('/food1')
def food1():
    return ('<html> <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-LsPWwQ1wPMxNjLnBW7QDuAf3UQfDKb9toA&s"> <a href = \'/home\'> go back </a> <a href = \'/food2\'> go to food2 </a>  </html>')
@app.route('/food3')
def food3():
    return ('''<html> 
        <img src = "https://www.seriouseats.com/thmb/EW6j4ry5rLgY0vadAMeqlQsK0Js=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/20211201-msakhan-vicky-wasik-36-8583aa93caa4496c81497db85c96a905.jpg"> 
        <a href = \'/food2\'> 
        go to food 2 </a>
        <a href = \'/home\'> 
        go to home </a> </html>''')
@app.route('/food2')
def food2():
    return ('''<html> 
        <img src = "https://upload.wikimedia.org/wikipedia/commons/2/2d/Makluba.JPG"> 
        <a href = \'/food3\'> 
        go to food 3 </a> 
        <a href = \'/food1\'> 
        go to food 1 </a></html>''')
@app.route('/pet2')
def pet2():
    return ('''<html> 
        <img src = "https://ultra-pet.co.za/wp-content/uploads/2020/08/socialising-800x630.jpg"> 
        <a href = \'/pet1\'> 
        go to pet1 </a> 
        <a href = \'/pet3\'> 
        go to pet3 </a></html>
        <a href = \'/home\'> 
        go back to home page </a></html>''')
@app.route('/pet1')
def pet1():
    return ('''<html> 
        <img src = "https://d2zp5xs5cp8zlg.cloudfront.net/image-43761-800.jpg"> 
        <a href = \'/pet2\'> 
        go to pet2 </a> 
        </html>''')
@app.route('/pet3')
def pet3():
    return ('''<html> 
        <img src = "https://images.saymedia-content.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cq_auto:eco%2Cw_1200/MTk2OTY2NzAwMDk5MzE1MzQw/pet-turtle-or-tortoise.png"> 
        <a href = \'/pet2\'> 
        go to pet2 </a> 
        </html>''')
@app.route('/space1')
def space1():
    return ('''<html> 
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJpaWTviBwKxlBCAQujz_Jr3Fb2baDw7eRrg&s"> 
        <a href = \'/home\'> 
        go back to home </a> 
        <a href = \'/space2\'> 
        go to space2 </a>
        <a href = \'/space3\'> 
        go to space3 </a></html>''')
@app.route('/space2')
def space2():
    return ('''<html> 
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStufw8OwmVwqZRprN1R-tygkedMLlL_RR0ug&s"> 
        <a href = \'/space1\'> 
        go to space1 </a>
        <a href = \'/space3\'> 
        go to space3 </a></html>''')
@app.route('/space3')
def space3():
    return ('''<html> 
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSva80qn921XF6JDyEMAvAcAibZTDL4nIuOdA&s"> 
        <a href = \'/space1\'> 
        go to space1 </a>
        <a href = \'/space2\'> 
        go to space2 </a></html>''')




if __name__ == '__main__':
    app.run(debug=True)
