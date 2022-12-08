<template>
  <div class="login-main">
    <div class="login form-signin w-100 m-auto">
      <form class="login-form" @submit="login">
        <h1 class="h3 mb-3 fw-normal">Войти</h1>

        <div class="form-floating mb-3">
          <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com"
                 required v-model="email">
          <label for="floatingInput">Email</label>
        </div>

        <div class="form-floating mb-3">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password"
                 required v-model="password">
          <label for="floatingPassword">Пароль</label>
        </div>

        <button class="w-100 btn btn-lg btn-primary" type="submit">Войти</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    login(event) {
      this.$http.post('api/login/', JSON.stringify({email: this.email, password: this.password}))
        .then((response) => {
          localStorage.setItem("user", JSON.stringify(response.data.success))
          this.$router.push({name: "home"})
        })
      event.preventDefault()
    },
  }
}
</script>

<style scoped>

.login-main {
  display: table;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}

.login {
  display: table-cell;
  vertical-align: middle;
}

.login-form {
  margin-left: auto;
  margin-right: auto;
  width: 400px;
}

</style>