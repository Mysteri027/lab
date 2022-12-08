<template>
  <div class="registration-main">
    <div class="registration form-signin w-100 m-auto">
      <form class="registration-form" @submit="registration">
        <h1 class="h3 mb-3 fw-normal">Зарегистрироваться</h1>

        <div class="form-floating mb-3">
          <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" required
                 v-model="user_info.email">
          <label for="floatingInput">Email</label>
        </div>

        <div class="form-floating mb-3">
          <input type="text" class="form-control" placeholder="Password" required
                 v-model="user_info.phoneNumber">
          <label for="floatingPassword">Номер телефона</label>
        </div>

        <div class="form-floating mb-3">
          <input type="text" class="form-control" placeholder="Password" required
                 v-model="user_info.name">
          <label for="floatingPassword">Имя</label>
        </div>

        <div class="form-floating mb-3">
          <input type="text" class="form-control" placeholder="Password" required
                 v-model="user_info.surName">
          <label for="floatingPassword">Фамилия</label>
        </div>

        <div class="form-floating mb-3">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password" required
                 v-model="user_info.password">
          <label for="floatingPassword">Пароль</label>
        </div>

        <div class="form-floating mb-3">
          <input type="password" class="form-control" id="floatingPasswordAgain" placeholder="Password" required
                 v-model="user_info.secondPassword">
          <label for="floatingPasswordAgain">Повторите пароль</label>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegistrationForm",
  data() {
    return {
      user_info: {
        email: "",
        phoneNumber: "",
        name: "",
        surName: "",
        password: "",
        secondPassword: "",
      }
    }
  },
  methods: {
    // вот так отправляй post запросы
    registration(event) {
      this.$http.post('api/registration/', JSON.stringify({
        email: this.user_info.email,
        phoneNumber: this.user_info.phoneNumber,
        name: this.user_info.name,
        surName: this.user_info.surName,
        password: this.user_info.password,
        secondPassword: this.user_info.secondPassword,
      }))
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

.registration-main {
  display: table;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}

.registration {
  display: table-cell;
  vertical-align: middle;
}

.registration-form {
  margin-left: auto;
  margin-right: auto;
  width: 400px;
}
</style>