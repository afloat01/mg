from time import sleep
names = [
"<h3>Afloat StEppin STONE White T-SHIRT</h3>",
"<h3>Afloat StEppin STONE RoyalBlue T-SHIRT</h3>",
"<h3>Afloat StEppin STONE black T-SHIRT</h3>",
"<h3>Afloat black & blue-text Trucker Hat</h3>",
"<h3>Afloat black Trucker Hat</h3>",
"<h3>Afloat white & black Trucker Hat</h3>",
"<h3>Afloat black & red-text Trucker Hat</h3>",
#"<h3>Afloats white,black,red-text Trucker Hat</h3>",
"<h3>Afloat BLACK STEppin STONE with tracker HAT</h3>",
"<h3>Afloat WHITE STEppin STONE with tracker HAT</h3>",
"<h3>Afloats BLUE STEppin STONE with tracker HAT</h3>",
"<h3>Afloats black STEppin STONE with tracker HAT</h3>",
#"<h3>Afloats black & Blue STEppin STONE </h3>", # for the first display
]
images = [
"IMG-20240621-WA0085.jpg",
"IMG-20240621-WA0077.jpg",
"IMG-20240621-WA0079.jpg",
"IMG-20240621-WA0082.jpg",
"IMG-20240621-WA0087.jpg",
"IMG-20240621-WA0088.jpg",
"IMG-20240621-WA0089.jpg",
#"IMG-20240621-WA0090.jpg",
"IMG-20240621-WA0084.jpg",
"IMG-20240621-WA0078.jpg",
"IMG-20240621-WA0075.jpg",
"IMG-20240621-WA0081.jpg",
#"IMG-20240621-WA0073.jpg", # for the first display
]

amounts = [
170.00,
170.00,
170.00,
170.00,
180.00,
180.00,
180.00,
#180.00,
300.00,
300.00,
300.00,
300.00,
#170.00, # for first display
]


class __code__:
	def __init__(self, head, files):
		self.head = head
		self.files = files
		
block = __code__(names,images)

for i in range(0,11):
	h = block.head[i]
	f = block.files[i]
	a = amounts[i]
	
	template = f"""
<html>
<head>
<title>AFLOAT - Buy</title>

<meta charset="utf-8" />
<meta name="description" content="" />
<meta name="keywords" content="" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="../css/order.css" rel="stylesheet">

<style>

</style>
</head>
<body>
 <!--container-->
  <div id="container">
   
   <!--navCont-->
   <style>
   
   </style>
   <div id="navCont">
   
   <a href="../index.html">
   <img src="../img/logo/IMG-20220723-WA0006.jpg">
   </a>
   <!--navBtns-->
   <div id="navBtns">
   
   <!--marketBtn-->      
   <a href="#.html" >
   <button>
   <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="black" d="M17 18a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2c0-1.11.89-2 2-2M1 2h3.27l.94 2H20a1 1 0 0 1 1 1c0 .17-.05.34-.12.5l-3.58 6.47c-.34.61-1 1.03-1.75 1.03H8.1l-.9 1.63l-.03.12a.25.25 0 0 0 .25.25H19v2H7a2 2 0 0 1-2-2c0-.35.09-.68.24-.96l1.36-2.45L3 4H1zm6 16a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2c0-1.11.89-2 2-2m9-7l2.78-5H6.14l2.36 5z"/></svg>
   </button>
   </a>
   <!--marketBtn-->
   
   <!--menuBtn-->
   <button id="menuBtn">
   <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path fill="black" d="M3.563 4.063a.5.5 0 0 1 0-1l16.874-.001a.5.5 0 0 1 0 1l-16.874.001Zm0 8.438a.5.5 0 0 1 0-1l16.874-.002a.5.5 0 0 1 0 1l-16.874.002Zm0 8.438a.5.5 0 0 1 0-1l16.874-.002a.5.5 0 0 1 0 1l-16.874.002Z"/></svg>
   </button>
   <!--menuBtn-->
   
   </div>
   <!--navBtns-->
   
   </div>
   <!--navCont-->
   
   <!--lil-images-->
   <style>
    
   </style>
   <div class="lil-images">
    <img src="../img/products/new/{f}">   
   </div>
   <!--lil-images-->
   
   
   <!--data-->
   <style>
    
   </style>
   <div class="data">
    {h}
    <span>k{a}</span>
    <p>• O-Neck</p>
    <p>• 100% Cotton</p>
    <p>• For Men, Women</p>
    <p>• Short Sleeve Length</p>
    
    
    <!--mikechavuma51@gmail.com-->
    <form action="https://formsubmit.co/bartwelmwanza7@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_next" value="https://afloat01.github.io/mike/main/thankyou.html">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_cc" value="bartwelmwanza7@gmail.com">
    <input type="hidden" name="_autoresponse" value="Thank you for shoping with afloat.">
    
    <input type="hidden" name="item" value="{h}">
    
    <div id="size_box">
    <p>Size: <input id="p_size" name="size_of_shirt" value="M" readonly></p>
    
    <button type="button" id="s">S</button>
    <button type="button" id="m">M</button>
    <button type="button" id="l">L</button>
    <button type="button" id="xl">XL</button>
    <button type="button" id="xxl">XXL</button>
    <button type="button" id="xxxl">XXXL</button>
    </div>
    
    <p>Quantity</p>
    <div id="qua_box">
     <button type="button" id="sub">-</button>
     <input value="0" type="number" name="number_of_items" id="num" />
     <button type="button" id="add">+</button>
    </div>
    
    <label>Name<br>
    <input name="name" type="text" placeholder="Your name" required>
    </label>
    
    <label>Email<br>
    <input name="email" type="email" placeholder="Your email" required>
    </label>
    
    <label>Address<br>
    <input name="address" type="text" placeholder="Your address" required>
    </label>
    
    <label>Area<br>
    <input name="Area" type="text" placeholder="Your area" required>
    </label>
    
    <label>Phone number<br>
    <input name="phone" type="tel" placeholder="Phone number" required>
    </label>
    
    <button id="submit" type="submit">
    Make Order Now
    </button>
    
    </form>
    
   </div>
   <!--data-->
   
   
   <script src="../js/order.js"></script>
   
  </div>
 <!--container-->
</body>
</html>	
"""
	with open("order-file-"+str(i)+".html","w") as myf:
		myf.write(template)
		myf.close()
	
	