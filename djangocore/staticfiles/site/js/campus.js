document.getElementById("fim").addEventListener("click", function(event) {//ir para o fim
    event.preventDefault(); // Impede o comportamento padrão do link
    document.getElementById("final-da-pagina").scrollIntoView({ behavior: "smooth" });
});

document.getElementById('mostrar-mais').addEventListener('click', function(event) {
    event.preventDefault(); // Previne o comportamento padrão do link
    var maisQuadro = document.getElementById('mais-quadro');
    var icon = document.getElementById('icon');
    var textSpan = this.querySelector('span');

    // Verifica o estado de display do elemento no clique
    if (maisQuadro.style.display === "" || maisQuadro.style.display === "none") {
        maisQuadro.style.display = "flex"; // Usa flex para manter o layout
        textSpan.innerHTML = "Mostrar menos cursos<br>";

        // Altera o conteúdo do SVG para o novo ícone
        icon.innerHTML = '<path fill-rule="evenodd" d="M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708z"/>';
    } else {
        maisQuadro.style.display = "none";
        textSpan.innerHTML = "Mostrar mais cursos <br>";

        // Altera o conteúdo do SVG para o ícone original
        icon.innerHTML = '<path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/>';
    }
});

/* Links menu fixo */

document.getElementById("busque-curso-menu").addEventListener("click", function(event) {
    event.preventDefault(); 
    window.location.href = "../index.html#busque-seu-curso";
});

document.getElementById("menu-por-modalidade").addEventListener("click", function(event) {
    event.preventDefault();
    window.location.href = "../index.html#modalidades";
});

document.getElementById("menu-por-campus").addEventListener("click", function(event) {
    event.preventDefault(); 
    window.location.href = "../index.html#campus";
});

document.querySelectorAll('.dropdown-menu a').forEach(item => {
    item.addEventListener('click', function() {
        this.blur(); // Remove o foco do item após o clique
    });
});

document.getElementById("sobre-menu").addEventListener("click", function(event) {
    event.preventDefault(); 
    window.location.href = "../index.html#sobre-ifg";
});

document.getElementById("contato-menu").addEventListener("click", function(event) {
    event.preventDefault(); 
    document.getElementById("contato").scrollIntoView({ behavior: "smooth" });
});