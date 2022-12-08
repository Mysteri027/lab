<template>
  <header id="header" class="fixed-top">
    <div class="container">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <router-link to="/">
            <a class="navbar-brand" href="#">OnlineBank</a>
          </router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                  data-bs-target="#navbarSupportedContent"
                  aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">

              <li class="nav-item">
                <router-link to="/">
                  <a class="nav-link active" aria-current="page">Личный кабинет</a>
                </router-link>
              </li>

              <li class="nav-item">
                <router-link to="/moneytransfer">
                  <a class="nav-link active" aria-current="page">Перевод</a>
                </router-link>
              </li>

              <li class="nav-item">
                <router-link to="/transferhistory">
                  <a class="nav-link active" aria-current="page">История платежей</a>
                </router-link>
              </li>

            </ul>

            <div v-if="this.isUserExist() === false">
              <router-link to="/login">
              <button class="btn btn-outline-success me-3">Войти</button>
            </router-link>

            <router-link to="/registration">
              <button class="btn btn-outline-success">Зарегистрироваться</button>
            </router-link>
            </div>

            <div v-if="this.isUserExist() === true">
              <button class="btn btn-outline-success" @click="deleteUserFromLocalStorage">Выйти</button>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "NavigationBar",
  methods: {
    isUserExist() {
      return localStorage.getItem("user") != null
    },

    deleteUserFromLocalStorage() {
      localStorage.removeItem("user")
      this.$router.push({name: "home"})
      this.$forceUpdate();
    }
  }
}
</script>

<style scoped>
header {
  background-color: rgb(33, 37, 41);
}

a {
  text-decoration: none;
}

button {
  text-decoration-color: white;
}
</style>