$( "#celular" ).keypress(function() {
    $(this).mask('(000) 00000-0000');
});
function mascaraCelular(telefone){
    const textoAtual = telefone.value;
    const isValido = textoAtual.length === 12;

    let textoAjustado;
        const parte1 = textoAtual.slice(0,3);
        const parte2 = textoAtual.slice(3,8);
        const parte3 = textoAtual.slice(8,12);
        textoAjustado = `(${parte1}) ${parte2}-${parte3}`
    
    telefone.value = textoAjustado;
}
function tiraHifen(telefone){
    const textoAtual = telefone.value;
    const textoAjustado = textoAtual.replace(/\-/g, '');
    telefone.value = textoAjustado;
}

