function insertCard(){
    let card = document.createElement('li');
    let slidOut = document.createElement('span');
    let slidIn = document.createElement('span');
    //card.setAttribute("class","slider");
    //slidOut.setAttribute("class","slider-out");
    slidIn.setAttribute("class","slider-in");
    card.appendChild(slidOut);
    slidOut.appendChild(slidIn);
    let wrapper = document.getElementById("demoView");
    wrapper.appendChild(card);
}