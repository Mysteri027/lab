<template>
    <div class="registration-main">
    <div class="registration form-signin w-100 m-auto">
      <form class="registration-form">
        <h1 class="h3 mb-3 fw-normal">Зарегистрироваться</h1>
        <div class="form-floating mb-3">
          <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
          <label for="floatingInput">Email</label>
        </div>
        <div class="form-floating mb-3">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Пароль</label>
        </div>
        <div class="form-floating mb-3">
          <input type="password" class="form-control" id="floatingPasswordAgain" placeholder="Password">
          <label for="floatingPasswordAgain">Повторите пароль</label>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
    name: "RegistrationForm"
}
</script>

<style scoped>

.registration-main {
  display: table;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}

.registration{
  display: table-cell;
  vertical-align: middle;
}

.registration-form {
  margin-left: auto;
  margin-right: auto;
  width: 400px;
}
</style>