let hasloL = 1;

    function zmienL(){
        hasloL += 1;
        if(hasloL %2==0){
            document.getElementById('hasloToggle').innerHTML = "Ukryj";
            document.getElementById('haslo').type = "text";
        }
        else{
            document.getElementById('hasloToggle').innerHTML = "Pokaż";
            document.getElementById('haslo').type = "password";
        }
    }

    let hasloR = 1;

    function zmienR(){
        hasloR += 1;
        if(hasloR %2==0){
            document.getElementById('hasloToggle').innerHTML = "Ukryj";
            document.getElementById('znaki').type = "text";
            document.getElementById('dlugosc').type = "text";
        }
        else{
            document.getElementById('hasloToggle').innerHTML = "Pokaż";
            document.getElementById('znaki').type = "password";
            document.getElementById('dlugosc').type = "password";
            document.getElementById('dlugosc').type = "password";
        }
    }