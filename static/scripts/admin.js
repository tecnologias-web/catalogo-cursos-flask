

const forms = document.querySelectorAll('form.remover')

forms.forEach(form => {
    form.addEventListener('submit', event => {
        if(!confirm('Deseja remover o elemento selecionado?')){
            event.preventDefault()
        }
    })
})