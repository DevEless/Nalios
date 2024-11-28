function HelloNalios(){


    //stock dans une variable la methode qui va transformer le code ASCII en lettre et caractere
    let message = String.fromCharCode(
        72, 101, 108, 108, 111, 44, // "Hello,"
        32, 78, 97, 108, 105, 111, 115, // " Nalios"
        32, 33 // "!"
    );
// affiche le message dans la console
    console.log(message)
}

HelloNalios()
//lance la fonction