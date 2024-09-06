document.getElementById("pesquisar-menu").addEventListener("click", function(event) {
    event.preventDefault(); // Impede o comportamento padrão do link
    var text = document.querySelector("#pesquisar-container .pesquisar-text");
    var input = document.getElementById("pesquisar-input");
    if (text && input) {
        text.style.display = "none"; // Oculta o texto "Pesquisar"
        input.style.display = "block"; // Exibe o campo de entrada
        input.focus(); // Coloca o cursor no campo de entrada automaticamente
    }
});

document.getElementById("fim").addEventListener("click", function(event) {//ir para o fim
    event.preventDefault(); // Impede o comportamento padrão do link
    document.getElementById("final-da-pagina").scrollIntoView({ behavior: "smooth" });
});

/* Links menu fixo */

document.getElementById("busque-curso-menu").addEventListener("click", function(event) {
    event.preventDefault(); 
    document.getElementById("busque-seu-curso").scrollIntoView({ behavior: "smooth" });
});

document.getElementById("menu-por-modalidade").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("modalidades").scrollIntoView({ behavior: "smooth" });
});

document.getElementById("menu-por-campus").addEventListener("click", function(event) {
    event.preventDefault(); 
    document.getElementById("campus").scrollIntoView({ behavior: "smooth" });
});

document.querySelectorAll('.dropdown-menu a').forEach(item => {
    item.addEventListener('click', function() {
        this.blur(); // Remove o foco do item após o clique
    });
});

document.getElementById("sobre-menu").addEventListener("click", function(event) {
    event.preventDefault(); 
    document.getElementById("sobre-ifg").scrollIntoView({ behavior: "smooth" });
});

document.getElementById("contato-menu").addEventListener("click", function(event) {
    event.preventDefault(); 
    document.getElementById("contato").scrollIntoView({ behavior: "smooth" });
});

//Busque seu curso

document.getElementById("bsc1").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("modalidades").scrollIntoView({ behavior: "smooth" });
});

document.getElementById("bsc2").addEventListener("click", function(event) {
    event.preventDefault(); 
    document.getElementById("campus").scrollIntoView({ behavior: "smooth" });
});

//Pointers do mapa
document.getElementById("aguaslindas-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("aguaslindas");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-aguaslindas").style.display = "block";
});

document.getElementById("aguaslindas-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("aguaslindas");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-aguaslindas").style.display = "none";
});

document.getElementById("anapolis-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("anapolis");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    pointerIcon.parentElement.style.zIndex = "10";
    document.getElementById("leg-anapolis").style.display = "block";
});

document.getElementById("anapolis-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("anapolis");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    pointerIcon.parentElement.style.zIndex = "";
    document.getElementById("leg-anapolis").style.display = "none";
});

document.getElementById("aparecida-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("aparecida");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    pointerIcon.parentElement.style.zIndex = "10";
    document.getElementById("leg-aparecida").style.display = "block";
});

document.getElementById("aparecida-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("aparecida");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    pointerIcon.parentElement.style.zIndex = "";
    document.getElementById("leg-aparecida").style.display = "none";
});

document.getElementById("cidadegoias-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("cidadegoias");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-cidadegoias").style.display = "block";
});

document.getElementById("cidadegoias-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("cidadegoias");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-cidadegoias").style.display = "none";
});

document.getElementById("formosa-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("formosa");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-formosa").style.display = "block";
});

document.getElementById("formosa-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("formosa");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-formosa").style.display = "none";
});

document.getElementById("goiania-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("goiania");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    pointerIcon.parentElement.style.zIndex = "10";
    document.getElementById("leg-goiania").style.display = "block";
});

document.getElementById("goiania-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("goiania");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    pointerIcon.parentElement.style.zIndex = "";
    document.getElementById("leg-goiania").style.display = "none";
});

document.getElementById("goianiaoeste-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("goianiaoeste");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-goianiaoeste").style.display = "block";
});

document.getElementById("goianiaoeste-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("goianiaoeste");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-goianiaoeste").style.display = "none";
});

document.getElementById("inhumas-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("inhumas");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-inhumas").style.display = "block";
});

document.getElementById("inhumas-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("inhumas");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-inhumas").style.display = "none";
});

document.getElementById("itumbiara-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("itumbiara");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-itumbiara").style.display = "block";
});

document.getElementById("itumbiara-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("itumbiara");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-itumbiara").style.display = "none";
});

document.getElementById("jatai-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("jatai");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-jatai").style.display = "block";
});

document.getElementById("jatai-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("jatai");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-jatai").style.display = "none";
});

document.getElementById("luziania-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("luziania");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-luziania").style.display = "block";
});

document.getElementById("luziania-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("luziania");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-luziania").style.display = "none";
});

document.getElementById("canedo-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("canedo");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-canedo").style.display = "block";
});

document.getElementById("canedo-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("canedo");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-canedo").style.display = "none";
});

document.getElementById("uruaçu-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("uruaçu");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    document.getElementById("leg-uruaçu").style.display = "block";
});

document.getElementById("uruaçu-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("uruaçu");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    document.getElementById("leg-uruaçu").style.display = "none";
});

document.getElementById("valparaiso-item").addEventListener("mouseover", function() {
    const pointerIcon = document.getElementById("valparaiso");
    pointerIcon.classList.add("hovered");
    pointerIcon.src = "icones/pointer-red.svg";
    pointerIcon.parentElement.style.zIndex = "10";
    document.getElementById("leg-valparaiso").style.display = "block";
});

document.getElementById("valparaiso-item").addEventListener("mouseout", function() {
    const pointerIcon = document.getElementById("valparaiso");
    pointerIcon.classList.remove("hovered");
    pointerIcon.src = "icones/pointer-green.svg";
    pointerIcon.parentElement.style.zIndex = "";
    document.getElementById("leg-valparaiso").style.display = "none";
});