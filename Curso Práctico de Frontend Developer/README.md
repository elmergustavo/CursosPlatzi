# NOTAS DEL CURSO PRÁCTICO DE FRONTEND DEVELOPER

## 01. ¿Ya tomaste el Curso de Frontend Developer?
Lecturas recomendadas

* https://platzi.com/cursos/flexbox-css-grid/
* https://platzi.com/cursos/frontend-developer/
* https://github.com/platzi/curso-frontend-developer-practico

## 02. Identifica las pantallas de tu proyecto
Lecturas recomendadas
* https://scene.zeplin.io/project/60afeeed20af1378ed046538
* https://www.figma.com/proto/bcEVujIzJj5PNIWwF9pP2w/Platzi_YardSale?node-id=0%3A684&amp%3Bscaling=scale-down&amp%3Bpage-id=0%3A1&amp%3Bstarting-point-node-id=0%3A719
* https://www.figma.com/proto/bcEVujIzJj5PNIWwF9pP2w/Platzi_YardSale?node-id=3%3A2112&amp%3Bscaling=scale-down&amp%3Bpage-id=0%3A998&amp%3Bstarting-point-node-id=5%3A2808

## 03. Sistema de diseño, assets y variables de CSS
Lecturas recomendadas
* https://platzi.com/cursos/diseno-desarrolladores/
* https://polaris.shopify.com/design/design
* https://fonts.google.com/specimen/Quicksand

```css
:root{
    --white: #FFFFFF;
    --black: #000000;
    --dark: #232830;
    --very-light-pink: #C7C7C7;
    --text-input-field: #F7F7F7;
    --hospital-green: #ACD9B2;
}

body{
    font-family: 'Quicksand', sans-serif;
}

```

## 04. Crear nueva contraseña: HTML
En este curso decidimos NO crear archivos con extensión .css para guardar nuestros estilos, sino guardarlos en los mismos archivos .html (dentro de la etiqueta <style>).

Si lo prefieres, puedes hacer esta división con tus propios archivos .css. De hecho, es la forma más recomendada de trabajar profesionalmente con HTML y CSS.

Pero con nuestra profesora Estefanny Aguilar lo haremos sin esta separación para facilitar la migración a componentes en el Curso Práctico de React.js (que muy pronto tomarás si continúas con la Escuela de JavaScript).

¡Mucha suerte durante tu maquetación!
  
* atajos en HTML: https://coderslink.com/talento/blog/ahorra-tiempo-al-escribir-codigo-html-en-visual-studio-code-utilizando-emmet/
  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap" rel="stylesheet">
  <title>Document</title>
  <style>
    :root {
      --white: #FFFFFF;
      --black: #000000;
      --very-light-pink: #C7C7C7;
      --text-input-field: #F7F7F7;
      --hospital-green: #ACD9B2;
      --sm: 14px;
      --md: 16px;
      --lg: 18px;
    }
    body {
      margin: 0;
      font-family: 'Quicksand', sans-serif;
    }
    .login {
      width: 100%;
      height: 100vh;
      display: grid;
      place-items: center;
    }
    .form-container {
      display: grid;
      grid-template-rows: auto 1fr auto;
      width: 300px;
    }
    .logo {
      width: 150px;
      margin-bottom: 48px;
      justify-self: center;
      display: none;
    }
    .title {
      font-size: var(--lg);
      margin-bottom: 12px;
      text-align: center;
    }
    .subtitle {
      color: var(--very-light-pink);
      font-size: var(--md);
      font-weight: 300;
      margin-top: 0;
      margin-bottom: 32px;
      text-align: center;
    }
    .form {
      display: flex;
      flex-direction: column;
    }
    .label {
      font-size: var(--sm);
      font-weight: bold;
      margin-bottom: 4px;
    }
    .input {
      background-color: var(--text-input-field);
      border: none;
      border-radius: 8px;
      height: 30px;
      font-size: var(--md);
      padding: 6px;
      margin-bottom: 12px;
    }
    .primary-button {
      background-color: var(--hospital-green);
      border-radius: 8px;
      border: none;
      color: var(--white);
      width: 100%;
      cursor: pointer;
      font-size: var(--md);
      font-weight: bold;
      height: 50px;
    }
    .login-button {
      margin-top: 14px;
      margin-bottom: 30px;
    }
    @media (max-width: 640px) {
      .logo {
        display: block;
      }
    }
  </style>
</head>
<body>
  <div class="login">
    <div class="form-container">
      <img src="./logos/logo_yard_sale.svg" alt="logo" class="logo">

      <h1 class="title">Create a new password</h1>
      <p class="subtitle">Enter a new passwrd for yue account</p>

      <form action="/" class="form">
        <label for="password" class="label">Password</label>
        <input type="password" id="password" placeholder="*********" class="input input-password">

        <label for="new-password" class="label">Password</label>
        <input type="password" id="new-password" placeholder="*********" class="input input-password">

        <input type="submit" value="Confirm" class="primary-button login-button">
      </form>
    </div>
  </div>
</body>
</html>
```
## 05. Crear nueva contraseña: CSS
```css
    .login {
      width: 100%;
      height: 100vh;
      display: grid;
      place-items: center;
    }
    .form-container {
      display: grid;
      grid-template-rows: auto 1fr auto;
      width: 300px;
    }
    .logo {
      width: 150px;
      margin-bottom: 48px;
      justify-self: center;
      display: none;
    }
    .title {
      font-size: var(--lg);
      margin-bottom: 12px;
      text-align: center;
    }
    .subtitle {
      color: var(--very-light-pink);
      font-size: var(--md);
      font-weight: 300;
      margin-top: 0;
      margin-bottom: 32px;
      text-align: center;
    }
    .form {
      display: flex;
      flex-direction: column;
    }
    .label {
      font-size: var(--sm);
      font-weight: bold;
      margin-bottom: 4px;
    }
    .input {
      background-color: var(--text-input-field);
      border: none;
      border-radius: 8px;
      height: 30px;
      font-size: var(--md);
      padding: 6px;
      margin-bottom: 12px;
    }
    .primary-button {
      background-color: var(--hospital-green);
      border-radius: 8px;
      border: none;
      color: var(--white);
      width: 100%;
      cursor: pointer;
      font-size: var(--md);
      font-weight: bold;
      height: 50px;
    }
    .login-button {
      margin-top: 14px;
      margin-bottom: 30px;
    }
    @media (max-width: 640px) {
      .logo {
        display: block;
      }
    }
```

