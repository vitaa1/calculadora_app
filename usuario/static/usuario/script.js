const campoSenha = document.getElementById("id_password1");
const textoAjuda = document.getElementById("ajuda-senha");

campoSenha.addEventListener("focus", () => {
    textoAjuda.classList.remove("hidden");
});

campoSenha.addEventListener("blur", () => {
    if (campoSenha.value.trim() === "") {
        textoAjuda.classList.add("hidden");
    }
});