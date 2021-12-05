# NOTAS DEL CURSO PRÁCTICO DE FRONTEND DEVELOPER

<code><img height="80" src="https://static.platzi.com/media/achievements/badge-curso-practico-frontend-developer-d28c2eb0-cd3e-4951-bb96-5f1bcab2add5.png" alt="Sass"/></code>
## Live pages

 - [index](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/index.html)
 - [account](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/account.html)
 - [email-sent](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/email-sent.html)
 - [login](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/login.html)
 - [menu-desktop](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/menu-desktop.html)
 - [menu-mobile](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/menu-mobile.html)
 - [my-account](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/my-account.html)
 - [my-order](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/my-order.html)
 - [new-pass](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/new-pass.html)
 - [orders-history](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/orders-history.html)
 - [product-detail](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/product-detail.html)
 - [shopping-cart](https://pikyr.github.io/cursoFrontendDeveloper/yardSale/shopping-cart.html)

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
## 06. Email enviado

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
      justify-items: center;
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
    .email-image {
      width: 132px;
      height: 132px;
      border-radius: 50%;
      background-color: var(--text-input-field);
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: 24px;
    }
    .email-image img {
      width: 80px;
    }
    .resend {
      font-size: var(--sm);
    }
    .resend span {
      color: var(--very-light-pink);
    }
    .resend a {
      color: var(--hospital-green);
      text-decoration: none;
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

      <h1 class="title">Email has been sent!</h1>
      <p class="subtitle">Please check your inbox for instructions on how to reset the password</p>

      <div class="email-image">
        <img src="./icons/email.svg" alt="email">
      </div>

      <button class="primary-button login-button">Login</button>

      <p class="resend">
        <span>Didn't receive the email?</span>
        <a href="/">Resend</a>
      </p>
    </div>
  </div>
</body>
</html>
```
## 07 Login
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
    .form {
      display: flex;
      flex-direction: column;
    }
    .form a {
      color: var(--hospital-green);
      font-size: var(--sm);
      text-align: center;
      text-decoration: none;
      margin-bottom: 52px;
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
    .input-email {
      margin-bottom: 22px;
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
    .secondary-button {
      background-color: var(--white);
      border-radius: 8px;
      border: 1px solid var(--hospital-green);
      color: var(--hospital-green);
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

      <form action="/" class="form">
        <label for="email" class="label">Email address</label>
        <input type="text" id="email" placeholder="platzi@example.cm" class="input input-email">

        <label for="password" class="label">Password</label>
        <input type="password" id="password" placeholder="*********" class="input input-password">

        <input type="submit" value="Log in" class="primary-button login-button">
        <a href="/">Forgot my password</a>
      </form>

      <button class="secondary-button signup-button">Sign up</button>
    </div>
  </div>
</body>
</html>
```
## 08. Crear y editar mi cuenta
![](https://static.platzi.com/media/user_upload/p1Web-364ff802-7b69-4ad0-9cad-ce6ba943c596.jpg)
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
      margin-bottom: 36px;
      text-align: start;
    }
    .form {
      display: flex;
      flex-direction: column;
    }
    .form div {
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
    .input-name,
    .input-email,
    .input-password {
      margin-bottom: 22px;
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
      .form-container {
        height: 100%;
      }
      .form {
        height: 100%;
        justify-content: space-between;
      }
    }
  </style>
</head>
<body>
  <div class="login">
    <div class="form-container">
      <h1 class="title">My account</h1>

      <form action="/" class="form">
        <div>
          <label for="name" class="label">Name</label>
          <input type="text" id="name" placeholder="Teff" class="input input-name">

          <label for="email" class="label">Email</label>
          <input type="text" id="email" placeholder="platzi@example.com" class="input input-email">

          <label for="password" class="label">Password</label>
          <input type="password" id="password" placeholder="*********" class="input input-password">
        </div>

        <input type="submit" value="Create" class="primary-button login-button">
      </form>
    </div>
  </div>
</body>
</html>
```
## 09. Mi cuenta
![](https://static.platzi.com/media/user_upload/screenMyAccount-7750a719-dc6e-42bc-8023-56710aa0b4f0.jpg)
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
      margin-bottom: 36px;
      text-align: start;
    }
    .form {
      display: flex;
      flex-direction: column;
    }
    .form div {
      display: flex;
      flex-direction: column;
    }
    .label {
      font-size: var(--sm);
      font-weight: bold;
      margin-bottom: 4px;
    }
    .value {
      color: var(--very-light-pink);
      font-size: var(--md);
      margin: 8px 0 32px 0;
    }
    .secondary-button {
      background-color: var(--white);
      border-radius: 8px;
      border: 1px solid var(--hospital-green);
      color: var(--hospital-green);
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
      .form-container {
        height: 100%;
      }
      .form {
        height: 100%;
        justify-content: space-between;
      }
    }
  </style>
</head>
<body>
  <div class="login">
    <div class="form-container">
      <h1 class="title">My account</h1>

      <form action="/" class="form">
        <div>
          <label for="name" class="label">Name</label>
          <p class="value">Camila Yokoo</p>

          <label for="email" class="label">Email</label>
          <p class="value">camilayokoo@gmail.com</p>

          <label for="password" class="label">Password</label>
          <p class="value">*********</p>
        </div>

        <input type="submit" value="Edit" class="secondary-button login-button">
      </form>
    </div>
  </div>
</body>
</html>
```
## 10. Página de inicio: HTML
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
    .cards-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, 240px);
      gap: 26px;
      place-content: center;
    }
    .product-card {
      width: 240px;
    }
    .product-card img {
      width: 240px;
      height: 240px;
      border-radius: 20px;
      object-fit: cover;
    }
    .product-info {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 12px;
    }
    .product-info figure {
      margin: 0;
    }
    .product-info figure img {
      width: 35px;
      height: 35px;
    }
    .product-info div p:nth-child(1) {
      font-weight: bold;
      font-size: var(--md);
      margin-top: 0;
      margin-bottom: 4px;
    }
    .product-info div p:nth-child(2) {
      font-size: var(--sm);
      margin-top: 0;
      margin-bottom: 0;
      color: var(--very-light-pink);
    }
    @media (max-width: 640px) {
      .cards-container {
        grid-template-columns: repeat(auto-fill, 140px);
      }
      .product-card {
        width: 140px;
      }
      .product-card img {
        width: 140px;
        height: 140px;
      }
    }
  </style>
<body>
  <section class="main-container">
    <div class="cards-container">

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>
    </div>
  </section>
</body>
</html>
```
## 11. Página de inicio: CSS
![](https://static.platzi.com/media/user_upload/image-a6d065a2-16e0-4383-a7c6-5f0731fe3599.jpg)
![](https://static.platzi.com/media/user_upload/inicio-desktop-0f9c9c84-3fb4-45e1-84bb-4ad8797b20e7.jpg)
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
    .cards-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, 240px);
      gap: 26px;
      place-content: center;
    }
    .product-card {
      width: 240px;
    }
    .product-card img {
      width: 240px;
      height: 240px;
      border-radius: 20px;
      object-fit: cover;
    }
    .product-info {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 12px;
    }
    .product-info figure {
      margin: 0;
    }
    .product-info figure img {
      width: 35px;
      height: 35px;
    }
    .product-info div p:nth-child(1) {
      font-weight: bold;
      font-size: var(--md);
      margin-top: 0;
      margin-bottom: 4px;
    }
    .product-info div p:nth-child(2) {
      font-size: var(--sm);
      margin-top: 0;
      margin-bottom: 0;
      color: var(--very-light-pink);
    }
    @media (max-width: 640px) {
      .cards-container {
        grid-template-columns: repeat(auto-fill, 140px);
      }
      .product-card {
        width: 140px;
      }
      .product-card img {
        width: 140px;
        height: 140px;
      }
    }
  </style>
<body>
  <section class="main-container">
    <div class="cards-container">

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="">
        <div class="product-info">
          <div>
            <p>$120,00</p>
            <p>Bike</p>
          </div>
          <figure>
            <img src="./icons/bt_add_to_cart.svg" alt="">
          </figure>
        </div>
      </div>
    </div>
  </section>
</body>
</html>
```
## 12. Menú desktop
![](https://static.platzi.com/media/user_upload/p1-9850e0be-2f07-4b66-9114-7525c64a3c50.jpg)
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
    .desktop-menu {
      width: 100px;
      height: auto;
      border: 1px solid var(--very-light-pink);
      border-radius: 6px;
      padding: 20px 20px 0 20px;
    }
    .desktop-menu ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .desktop-menu ul li {
      text-align: end;
    }
    .desktop-menu ul li:nth-child(1),
    .desktop-menu ul li:nth-child(2) {
      font-weight: bold;
    }
    .desktop-menu ul li:last-child {
      padding-top: 20px;
      border-top: 1px solid var(--very-light-pink);
    }
    .desktop-menu ul li:last-child a {
      color: var(--hospital-green);
      font-size: var(--sm);
    }
    .desktop-menu ul li a {
      color: var(--back);
      text-decoration: none;
      margin-bottom: 20px;
      display: inline-block;
    }
  </style>
</head>
<body>
  <div class="desktop-menu">
    <ul>
      <li>
        <a href="/" class="title">My orders</a>
      </li>

      <li>
        <a href="/">My account</a>
      </li>

      <li>
        <a href="/">Sign out</a>
      </li>
    </ul>
  </div>
</body>
</html>
```
## 13. Menú mobile
![](https://static.platzi.com/media/user_upload/Captura%20de%20Pantalla%202021-10-01%20a%20la%28s%29%2010.07.05-ddce5cc6-0cfd-4574-b769-041ece34751c.jpg)
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
    .mobile-menu {
      padding: 24px;
    }
    .mobile-menu a {
      text-decoration: none;
      color: var(--black);
      font-weight: bold;
      /* margin-bottom: 24px; */
    }
    .mobile-menu ul {
      padding: 0;
      margin: 24px 0 0;
      list-style: none;
    }
    .mobile-menu ul:nth-child(1) {
      border-bottom: 1px solid var(--very-light-pink);
    }
    .mobile-menu ul li {
      margin-bottom: 24px;
    }
    .email {
      font-size: var(--sm);
      font-weight: 300 !important;
    }
    .sign-out {
      font-size: var(--sm);
      color: var(--hospital-green) !important;
    }
  </style>
</head>
<body>
  <div class="mobile-menu">
    <ul>
      <li>
        <a href="/">CATEGORIES</a>
      </li>
      <li>
        <a href="/">All</a>
      </li>
      <li>
        <a href="/">Clothes</a>
      </li>
      <li>
        <a href="/">Electronics</a>
      </li>
      <li>
        <a href="/">Furnitures</a>
      </li>
      <li>
        <a href="/">Toys</a>
      </li>
      <li>
        <a href="/">Other</a>
      </li>
    </ul>

    <ul>
      <li>
        <a href="/">My orders</a>
      </li>
      <li>
        <a href="/">My account</a>
      </li>
    </ul>

    <ul>
      <li>
        <a href="/" class="email">platzi@example.com</a>
      </li>
      <li>
        <a href="/" class="sign-out">Sign out</a>
      </li>
    </ul>
  </div>
</body>
</html>

```
## 14. Mi orden: HTML
![](https://static.platzi.com/media/user_upload/p1-fb3d0f20-c1b3-4c3a-ad5b-24fdb4056909.jpg)
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./styles.css">
    <title>My order | Platzi Yard Sale</title>
</head>
<body>
    <header>

    </header>
    <main>
        <div class="my-order">
            <div class="my-order-container">
                <h1 class="title-order">
                    My order
                </h1>
                <div class="my-order-content">
                    <div class="order">
                        <div>
                            <p>
                                <span>
                                    10.03.2021
                                </span>
                                <span>
                                    6 articles
                                </span>
                            </p>
                        </div>
                        <p>
                            $560.00
                        </p>
                    </div>
                    <div class="shopping-cart">
                        <figure>
                            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
                        </figure>
                        <p>Bike</p>
                        <p>$30,00</p>
                    </div>
                    <div class="shopping-cart">
                        <figure>
                            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
                        </figure>
                        <p>Bike</p>
                        <p>$30,00</p>
                    </div>
                    <div class="shopping-cart">
                        <figure>
                            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
                        </figure>
                        <p>Bike</p>
                        <p>$30,00</p>
                    </div>
                    <div class="shopping-cart">
                        <figure>
                            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
                        </figure>
                        <p>Bike</p>
                        <p>$30,00</p>
                    </div>
                    <div class="shopping-cart">
                        <figure>
                            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
                        </figure>
                        <p>Bike</p>
                        <p>$30,00</p>
                    </div>
                    <div class="shopping-cart">
                        <figure>
                            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
                        </figure>
                        <p>Bike</p>
                        <p>$30,00</p>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
```

## 15. Mi orden: CSS
![](https://static.platzi.com/media/user_upload/order-c4dff5b0-5ff0-4ca4-a77f-2b1de6b67fe0.jpg)
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
    .my-order {
      width: 100%;
      height: 100vh;
      display: grid;
      place-items: center;
    }
    .title {
      font-size: var(--lg);
      margin-bottom: 40px;
    }
    .my-order-container {
      display: grid;
      grid-template-rows: auto 1fr auto;
      width: 300px;
    }
    .my-order-content {
      display: flex;
      flex-direction: column;
    }
    .order {
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 16px;
      align-items: center;
      background-color: var(--text-input-field);
      margin-bottom: 24px;
      border-radius: 8px;
      padding: 0 24px;
    }
    .order p:nth-child(1) {
      display: flex;
      flex-direction: column;
    }
    .order p span:nth-child(1) {
      font-size: var(--md);
      font-weight: bold;
    }
    .order p span:nth-child(2) {
      font-size: var(--sm);
      color: var(--very-light-pink);
    }
    .order p:nth-child(2) {
      text-align: end;
      font-weight: bold;
    }
    .shopping-cart {
      display: grid;
      grid-template-columns: auto 1fr auto auto;
      gap: 16px;
      margin-bottom: 24px;
      align-items: center;
    }
    .shopping-cart figure {
      margin: 0;
    }
    .shopping-cart figure img {
      width: 70px;
      height: 70px;
      border-radius: 20px;
      object-fit: cover;
    }
    .shopping-cart p:nth-child(2) {
      color: var(--very-light-pink);
    }
    .shopping-cart p:nth-child(3) {
      font-size: var(--md);
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="my-order">
    <div class="my-order-container">
      <h1 class="title">My order</h1>

      <div class="my-order-content">
        <div class="order">
          <p>
            <span>03.25.21</span>
            <span>6 articles</span>
          </p>
          <p>$560.00</p>
        </div>

        <div class="shopping-cart">
          <figure>
            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
          </figure>
          <p>Bike</p>
          <p>$30,00</p>
        </div>

        <div class="shopping-cart">
          <figure>
            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
          </figure>
          <p>Bike</p>
          <p>$30,00</p>
        </div>

        <div class="shopping-cart">
          <figure>
            <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
          </figure>
          <p>Bike</p>
          <p>$30,00</p>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
 
```
## 16. Mis órdenes
![](https://static.platzi.com/media/user_upload/Selection_071-c34c18c9-1328-431e-b941-06d045419295.jpg)
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
    .my-order {
      width: 100%;
      height: 100vh;
      display: grid;
      place-items: center;
    }
    .title {
      font-size: var(--lg);
      margin-bottom: 40px;
    }
    .my-order-container {
      display: grid;
      grid-template-rows: auto 1fr auto;
      width: 300px;
    }
    .my-order-content {
      display: flex;
      flex-direction: column;
    }
    .order {
      display: grid;
      grid-template-columns: auto 1fr auto;
      gap: 16px;
      align-items: center;
      margin-bottom: 12px;
    }
    .order p:nth-child(1) {
      display: flex;
      flex-direction: column;
    }
    .order p span:nth-child(1) {
      font-size: var(--md);
      font-weight: bold;
    }
    .order p span:nth-child(2) {
      font-size: var(--sm);
      color: var(--very-light-pink);
    }
    .order p:nth-child(2) {
      text-align: end;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="my-order">
    <div class="my-order-container">
      <h1 class="title">My orders</h1>

      <div class="my-order-content">
        <div class="order">
          <p>
            <span>03.25.21</span>
            <span>6 articles</span>
          </p>
          <p>$560.00</p>
          <img src="./icons/flechita.svg" alt="arrow">
        </div>

        <div class="order">
          <p>
            <span>03.25.21</span>
            <span>6 articles</span>
          </p>
          <p>$560.00</p>
          <img src="./icons/flechita.svg" alt="arrow">
        </div>

        <div class="order">
          <p>
            <span>03.25.21</span>
            <span>6 articles</span>
          </p>
          <p>$560.00</p>
          <img src="./icons/flechita.svg" alt="arrow">
        </div>

        <div class="order">
          <p>
            <span>03.25.21</span>
            <span>6 articles</span>
          </p>
          <p>$560.00</p>
          <img src="./icons/flechita.svg" alt="arrow">
        </div>
      </div>
    </div>
  </div>
</body>
</html>
```
## 17. Navbar: HTML
```html
<body>
  <nav>
    <img src="./icons/icon_menu.svg" alt="menu" class="menu">

    <div class="navbar-left">
      <img src="./logos/logo_yard_sale.svg" alt="logo" class="logo">

      <ul>
        <li>
          <a href="/">All</a>
        </li>
        <li>
          <a href="/">Clothes</a>
        </li>
        <li>
          <a href="/">Electronics</a>
        </li>
        <li>
          <a href="/">Furnitures</a>
        </li>
        <li>
          <a href="/">Toys</a>
        </li>
        <li>
          <a href="/">Others</a>
        </li>
      </ul>
    </div>

    <div class="navbar-right">
      <ul>
        <li class="navbar-email">platzi@example.com</li>
        <li class="navbar-shopping-cart">
          <img src="./icons/icon_shopping_cart.svg" alt="shopping cart">
          <div>2</div>
        </li>
      </ul>
    </div>
  </nav>
</body>
```
## 18. Navbar: CSS
![](https://static.platzi.com/media/user_upload/mobile-aad99985-d4a7-4db6-a95c-587135421a7a.jpg)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
    nav {
      display: flex;
      justify-content: space-between;
      padding: 0 24px;
      border-bottom: 1px solid var(--very-light-pink);
    }
    .menu {
      display: none;
    }
    .logo {
      width: 100px;
    }
    .navbar-left ul,
    .navbar-right ul {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      align-items: center;
      height: 60px;
    }
    .navbar-left {
      display: flex;
    }
    .navbar-left ul {
      margin-left: 12px;
    }
    .navbar-left ul li a,
    .navbar-right ul li a {
      text-decoration: none;
      color: var(--very-light-pink);
      border: 1px solid var(--white);
      padding: 8px;
      border-radius: 8px;
    }
    .navbar-left ul li a:hover,
    .navbar-right ul li a:hover {
      border: 1px solid var(--hospital-green);
      color: var(--hospital-green);
    }
    .navbar-email {
      color: var(--very-light-pink);
      font-size: var(--sm);
      margin-right: 12px;
    }
    .navbar-shopping-cart {
      position: relative;
    }
    .navbar-shopping-cart div {
      width: 16px;
      height: 16px;
      background-color: var(--hospital-green);
      border-radius: 50%;
      font-size: var(--sm);
      font-weight: bold;
      position: absolute;
      top: -6px;
      right: -3px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 640px) {
      .menu {
        display: block;
      }
      .navbar-left ul {
        display: none;
      }
      .navbar-email {
        display: none;
      }
    }
  </style>
</head>
<body>
  <nav>
    <img src="./icons/icon_menu.svg" alt="menu" class="menu">

    <div class="navbar-left">
      <img src="./logos/logo_yard_sale.svg" alt="logo" class="logo">
 
      <ul>
        <li>
          <a href="/">All</a>
        </li>
        <li>
          <a href="/">Clothes</a>
        </li>
        <li>
          <a href="/">Electronics</a>
        </li>
        <li>
          <a href="/">Furnitures</a>
        </li>
        <li>
          <a href="/">Toys</a>
        </li>
        <li>
          <a href="/">Others</a>
        </li>
      </ul>
    </div>

    <div class="navbar-right">
      <ul>
        <li class="navbar-email">platzi@example.com</li>
        <li class="navbar-shopping-cart">
          <img src="./icons/icon_shopping_cart.svg" alt="shopping cart">
          <div>2</div>
        </li>
      </ul>
    </div>
  </nav>
</body>
</html>
```
## 19. Detalle de producto
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
    .product-detail {
      width: 360px;
      padding-bottom: 24px;
      position: absolute;
      right: 0;
    }
    .product-detail-close {
      background: var(--white);
      width: 14px;
      height: 14px;
      position: absolute;
      top: 24px;
      left: 24px;
      z-index: 2;
      padding: 12px;
      border-radius: 50%;
    }
    .product-detail-close:hover {
      cursor: pointer;
    }
    .product-detail > img:nth-child(2) {
      width: 100%;
      height: 360px;
      object-fit: cover;
      border-radius: 0 0 20px 20px;
    }
    .product-info {
      margin: 24px 24px 0 24px;
    }
    .product-info p:nth-child(1) {
      font-weight: bold;
      font-size: var(--md);
      margin-top: 0;
      margin-bottom: 4px;
    }
    .product-info p:nth-child(2) {
      color: var(--very-light-pink);
      font-size: var(--md);
      margin-top: 0;
      margin-bottom: 36px;
    }
    .product-info p:nth-child(3) {
      color: var(--very-light-pink);
      font-size: var(--sm);
      margin-top: 0;
      margin-bottom: 36px;
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
    .add-to-cart-button {
      display: flex;
      align-items: center;
      justify-content: center;
    }
    @media (max-width: 640px) {
      .product-detail {
        width: 100%;
      }
    }
  </style>
</head>
<body>
  <aside class="product-detail">
    <div class="product-detail-close">
      <img src="./icons/icon_close.png" alt="close">
    </div>
    <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
    <div class="product-info">
      <p>$35,00</p>
      <p>Bike</p>
      <p>With its practical position, this bike also fulfills a decorative function, add your hall or workspace.</p>
      <button class="primary-button add-to-cart-button">
        <img src="./icons/bt_add_to_cart.svg" alt="add to cart">
        Add to cart
      </button>
    </div>
  </aside>
</body>
</html>
```
## 20. Carrito de compras: HTML
![](https://static.platzi.com/media/user_upload/cart-7f027106-ffe0-4717-a1b9-a47b52db1d61.jpg)
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
    .product-detail {
      width: 360px;
      padding: 24px;
      box-sizing: border-box;
      position: absolute;
      right: 0;
    }
    .title-container {
      display: flex;
    }
    .title-container img {
      transform: rotate(180deg);
      margin-right: 14px;
    }
    .title {
      font-size: var(--lg);
      font-weight: bold;
    }
    .order {
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 16px;
      align-items: center;
      background-color: var(--text-input-field);
      margin-bottom: 24px;
      border-radius: 8px;
      padding: 0 24px;
    }
    .order p:nth-child(1) {
      display: flex;
      flex-direction: column;
    }
    .order p span:nth-child(1) {
      font-size: var(--md);
      font-weight: bold;
    }
    .order p:nth-child(2) {
      text-align: end;
      font-weight: bold;
    }
    .shopping-cart {
      display: grid;
      grid-template-columns: auto 1fr auto auto;
      gap: 16px;
      margin-bottom: 24px;
      align-items: center;
    }
    .shopping-cart figure {
      margin: 0;
    }
    .shopping-cart figure img {
      width: 70px;
      height: 70px;
      border-radius: 20px;
      object-fit: cover;
    }
    .shopping-cart p:nth-child(2) {
      color: var(--very-light-pink);
    }
    .shopping-cart p:nth-child(3) {
      font-size: var(--md);
      font-weight: bold;
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
    @media (max-width: 640px) {
      .product-detail {
        width: 100%;
      }
    }
  </style>
</head>
<body>
  <aside class="product-detail">
    <div class="title-container">
      <img src="./icons/flechita.svg" alt="arrow">
      <p class="title">My order</p>
    </div>

    <div class="my-order-content">
      <div class="shopping-cart">
        <figure>
          <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
        </figure>
        <p>Bike</p>
        <p>$30,00</p>
        <img src="./icons/icon_close.png" alt="close">
      </div>

      <div class="shopping-cart">
        <figure>
          <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
        </figure>
        <p>Bike</p>
        <p>$30,00</p>
        <img src="./icons/icon_close.png" alt="close">
      </div>

      <div class="shopping-cart">
        <figure>
          <img src="https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="bike">
        </figure>
        <p>Bike</p>
        <p>$30,00</p>
        <img src="./icons/icon_close.png" alt="close">
      </div>

      <div class="order">
        <p>
          <span>Total</span>
        </p>
        <p>$560.00</p>
      </div>

      <button class="primary-button">
        Checkout
      </button>
    </div>
  </div>
  </aside>
</body>
</html>
```
