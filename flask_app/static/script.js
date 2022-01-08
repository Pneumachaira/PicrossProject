function change(element){
    if (element.value=="0"){
        element.value="1"
        element.style.backgroundColor = "black"
        element.style.color = "black"
    }
    else {
        element.value="0"
        element.style.backgroundColor = "ghostwhite"
        element.style.color = "ghostwhite"
    }
    element.blur();
}

function markOut(e, element){
    e.preventDefault()
    if (element.style.backgroundColor == "tomato"){
        element.style.backgroundColor = "ghostwhite"
        element.style.color = "ghostwhite"
    }
    else{
        element.value = "0"
        element.style.backgroundColor = "tomato"
        element.style.color = "tomato"
    }
    element.blur();
}

function changeText(element){
    if (element.style.color == "black"){
        element.style.color = "red"
    }
    else {
        element.style.color = "black"
    }
}

function check(e, aString){
    setTimeout(() => {
        e.preventDefault()
        var picross = document.getElementById("picross")
        var form = new FormData(picross)
        var gstring = ""
        gstring += form.get("1")
        gstring += form.get("2")
        gstring += form.get("3")
        gstring += form.get("4")
        gstring += form.get("5")
        gstring += form.get("6")
        gstring += form.get("7")
        gstring += form.get("8")
        gstring += form.get("9")
        gstring += form.get("10")
        gstring += form.get("11")
        gstring += form.get("12")
        gstring += form.get("13")
        gstring += form.get("14")
        gstring += form.get("15")
        gstring += form.get("16")
        gstring += form.get("17")
        gstring += form.get("18")
        gstring += form.get("19")
        gstring += form.get("20")
        gstring += form.get("21")
        gstring += form.get("22")
        gstring += form.get("23")
        gstring += form.get("24")
        gstring += form.get("25")
        // console.log("gString is:", gstring)
        // console.log("aString is:", aString)
        if (gstring.trim() == aString.trim()){
            alert("You win!")
        }
    }
    , 50)
}