from pyscript import display, document

store_name = "Lunar Cafe Order Form!"

display (store_name, target = "storename") 

def info(e):

    name = document.getElementById("info1").value # get the value of info1

    address = document.getElementById("info2").value # get the value of info2

    number = document.getElementById("info3").value   #get the value of info3

    ord1 = int(document.getElementById("input1").value or 0)   #get the value of input1

    ord2 = int(document.getElementById("input2").value or 0)  #get the value of input2

    ord3 = int(document.getElementById("input3").value or 0)  #get the value of input3

    ord4 = int(document.getElementById("input4").value or 0)  #get the value of input4

    cos1 = ord1 * 120  #price of item 1

    cos2 = ord2 * 150  #price of item 2

    cos3 = ord3 * 200  #price of item 3

    cos4 = ord4 * 225  #price of item 4

    fcost = cos1 + cos2 + cos3 + cos4 #final cost

    document.getElementById("Name").innerHTML = "Lunar Cafe Order Confirmation!"  

    document.getElementById("output1").innerHTML = f"Order For : {name}"

    document.getElementById("output2").innerHTML = f"Address : {address}"

    document.getElementById("output3").innerHTML = f"Contact : {number}"

    document.getElementById("output4").innerHTML = f"Price : {fcost} PHP."

    e.preventDefault()  # Prevent the default form submission behavior