<template>
  <div class="lk-main">
    <div class="lk">
      <div class="lk-user">
        <div class="lk-container">

          <div v-if="this.isUserExist() === true">
            <h1>Всего на счете <span class="badge bg-secondary">{{ moneyCount }} руб.</span></h1>
            <h1>Имя <span class="badge bg-secondary">{{ name }}</span></h1>
            <h1>Фамилия <span class="badge bg-secondary">{{ surName }}</span></h1>
            <h1>Email <span class="badge bg-secondary">{{ email }}</span></h1>
            <h1>Номер телефона <span class="badge bg-secondary">{{ phoneNumber }}</span></h1>
          </div>

          <div v-if="this.isUserExist() === false">
            <h1><span class="badge bg-secondary">Войдите или зарегистрируйтесь</span></h1>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "MainPage",
  data() {
    return {
      moneyCount: 0,
      name: "",
      surName: "",
      email: "",
      phoneNumber: "",
    }
  },
  mounted() {
    const userId = localStorage.getItem("user")
    this.$http.get("api/user/" + userId)
      .then(response => (
        this.moneyCount = response.data.moneyCount,
          this.name = response.data.name,
          this.surName = response.data.surName,
          this.email = response.data.email,
          this.phoneNumber = response.data.phoneNumber
      ));
  },

  methods: {
    isUserExist() {
      return localStorage.getItem("user") != null
    },
  }
}
</script>

<style scoped>

.lk-main {
  display: table;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}

.lk {
  display: table-cell;
  vertical-align: middle;
}

.lk-user {
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  height: 600px;
  display: flex;
}

.lk-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
}

.btn {
  width: 100px;
  padding: 5px;
  margin-bottom: 10px;
}

</style>