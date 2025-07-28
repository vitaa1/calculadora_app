let entradaAtual = "";
let operacao = "";
let primeiroNumero = "";
let novoOperador = false;

function adicionar(value) {
    if (novoOperador) {
        entradaAtual = "";
        primeiroNumero = "";
        operacao = "";
        novoOperador = false;
    }

    if (entradaAtual === "0" && value !== ".") {
        entradaAtual = value;
    } else {
        entradaAtual += value;
    }

    if (operacao !== "" && primeiroNumero !== "") {
        let visualOperator = operacao;
        if (operacao === "*") visualOperator = "×";
        else if (operacao === "/") visualOperator = "÷";
        atualizarTela(primeiroNumero + " " + visualOperator + " " + entradaAtual);
    } else {
        atualizarTela(entradaAtual);
    }
}

function setarOperador(op) {
    if (entradaAtual === "") {
        return;
    }

    operacao = op;
    primeiroNumero = entradaAtual;
    entradaAtual = "";

    let visualOperator = op;
    if (op === "*") {
        visualOperator = "×";
    } else if (op === "/") {
        visualOperator = "÷";
    }
    atualizarTela(primeiroNumero + " " + visualOperator);
    novoOperador = false;
}

function alternarSinal() {
    if (entradaAtual !== "") {
        if (entradaAtual.startsWith("-")) {
            entradaAtual = entradaAtual.slice(1);
        } else {
            entradaAtual = "-" + entradaAtual;
        }

        atualizarTela(entradaAtual);
    }
}

function setarPorcentagem() {
    if (entradaAtual === "") {
        return;
    }

    operacao = "%";
    primeiroNumero = entradaAtual;
    entradaAtual = "";
    novoOperador = false;

    atualizarTela(primeiroNumero + " %");
}

function atualizarTela(value) {
    document.getElementById("display").innerText = value || "0";
}

function limparTela() {
    entradaAtual = "";
    primeiroNumero = "";
    operacao = "";
    novoOperador = false;
    atualizarTela("0");
}

document.getElementById("calculadora").addEventListener("submit", function (e) {
    if (operacao === "" || entradaAtual === "") {
        e.preventDefault(); 
        return;
    }
    if (operacao === '+/-') {
        document.getElementById("numero1").value = primeiroNumero || entradaAtual;
        document.getElementById("numero2").value = 0;
    } else {
        document.getElementById("numero1").value = primeiroNumero;
        document.getElementById("numero2").value = entradaAtual;
    }

    document.getElementById("operacao").value = operacao;
    novoOperador = true;
});

window.addEventListener("load", function () {
    const visor = document.getElementById("display").innerText.trim();
    if (!isNaN(visor) && visor !== "") {
        primeiroNumero = visor;
        entradaAtual = visor;
    }
});
