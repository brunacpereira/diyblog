function buscarBlog() {
  console.log('Entrou buscarBlog');

  fetch('/api/blogs/')
    .then(data => {
      if (!data.ok) throw Error(data.status);
      return data.json();
    })
    .then(update => console.log(update))
    .catch(e => console.log(e));
}


function criarBlog() {
  console.log('Entrou criarBlog')

  const update = {
  title: 'Teste via API',
  blogger: 'Bruna',
  description: 'Teste criação blog a partir da api',
  };

  const options = {
  method: 'POST',
  headers: {
  'Content-Type': 'application/json',
  },
  body: JSON.stringify(update),
  };

  fetch('/api/blogs/', options)
  .then(data => {
      if (!data.ok) {
        throw Error(data.status);
       }
       return data.json();
      }).then(update => {
      console.log(update);
      
      }).catch(e => {
      console.log(e);
      });
}

